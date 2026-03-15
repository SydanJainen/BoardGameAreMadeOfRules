import time
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import requests
from PyPDF2 import PdfReader

from src.core.models import RawContent


class PDFAdapter:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            reader = PdfReader(str(self.file_path))
            text_parts = []

            for page in reader.pages:
                page_text = page.extract_text()
                text_parts.append(page_text)
            text = "\n\n".join(text_parts)

            return RawContent(
                text=text,
                source_type="pdf",
                metadata={
                    "file_path": str(self.file_path),
                    "file_size": self.file_path.stat().st_size,
                    "page_count": len(reader.pages),
                },
            )
        except Exception as e:
            raise IOError(f"Error reading PDF {self.file_path}: {e}")


class PdfPlumberAdapter:
    def __init__(self, file_path: str, pages: tuple = None):
        self.file_path = Path(file_path)
        self.pages = pages

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            import pdfplumber
        except ImportError:
            raise ImportError(
                "Layout-aware PDF extraction requires pdfplumber: pip install pdfplumber"
            )

        try:
            text_parts = []
            with pdfplumber.open(str(self.file_path)) as pdf:
                page_count = len(pdf.pages)
                pages_to_process = pdf.pages
                if self.pages:
                    start, end = self.pages
                    pages_to_process = pdf.pages[start - 1 : end]

                for page in pages_to_process:
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)

            text = "\n\n".join(text_parts)

            return RawContent(
                text=text,
                source_type="pdf",
                metadata={
                    "file_path": str(self.file_path),
                    "file_size": self.file_path.stat().st_size,
                    "page_count": page_count,
                    "extraction_method": "plumber",
                },
            )
        except ImportError:
            raise
        except Exception as e:
            raise IOError(f"Error reading PDF with pdfplumber {self.file_path}: {e}")


class TablePDFAdapter:
    def __init__(self, file_path: str, output_dir: str = None, pages: tuple = None):
        self.file_path = Path(file_path)
        self.output_dir = Path(output_dir) if output_dir else None
        self.pages = pages

    def _table_to_markdown(self, table):
        if not table or len(table) < 1:
            return ""
        rows = []
        header = table[0]
        cols = [str(c) if c else "" for c in header]
        rows.append("| " + " | ".join(cols) + " |")
        rows.append("| " + " | ".join("---" for _ in cols) + " |")
        for row in table[1:]:
            cells = [str(c) if c else "" for c in row]
            while len(cells) < len(cols):
                cells.append("")
            rows.append("| " + " | ".join(cells[:len(cols)]) + " |")
        return "\n".join(rows)

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            import pdfplumber
        except ImportError:
            raise ImportError(
                "Table PDF extraction requires pdfplumber: pip install pdfplumber"
            )

        try:
            text_parts = []
            tables_found = 0
            csv_files = []

            with pdfplumber.open(str(self.file_path)) as pdf:
                page_count = len(pdf.pages)
                pages_to_process = pdf.pages
                if self.pages:
                    start, end = self.pages
                    pages_to_process = pdf.pages[start - 1 : end]

                for page_idx, page in enumerate(pages_to_process, start=1):
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)

                    tables = page.extract_tables()
                    for t_idx, table in enumerate(tables, start=1):
                        tables_found += 1
                        md_table = self._table_to_markdown(table)
                        if md_table:
                            text_parts.append(f"\n[Table {tables_found} - Page {page_idx}]\n{md_table}")

                        if self.output_dir:
                            import csv
                            tables_dir = self.output_dir / self.file_path.stem / "tables"
                            tables_dir.mkdir(parents=True, exist_ok=True)
                            csv_path = tables_dir / f"page{page_idx}_table{t_idx}.csv"
                            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                                writer = csv.writer(f)
                                for row in table:
                                    writer.writerow([str(c) if c else "" for c in row])
                            csv_files.append(str(csv_path))

            text = "\n\n".join(text_parts)
            if not text.strip():
                text = f"[Document contains {tables_found} table(s), no extractable text]"

            metadata = {
                "file_path": str(self.file_path),
                "file_size": self.file_path.stat().st_size,
                "page_count": page_count,
                "extraction_method": "tables",
                "tables_count": tables_found,
            }
            if csv_files:
                metadata["table_files"] = csv_files

            return RawContent(text=text, source_type="pdf", metadata=metadata)

        except ImportError:
            raise
        except Exception as e:
            raise IOError(f"Error extracting tables from PDF {self.file_path}: {e}")


class OCRPDFAdapter:
    def __init__(self, file_path: str, language: str = "eng", dpi: int = 300, pages: tuple = None):
        self.file_path = Path(file_path)
        self.language = language
        self.dpi = dpi
        self.pages = pages

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            import pytesseract
            from pdf2image import convert_from_path
        except ImportError:
            raise ImportError(
                "OCR PDF extraction requires: pip install pytesseract Pillow pdf2image\n"
            )

        try:
            kwargs = {"dpi": self.dpi}
            if self.pages:
                kwargs["first_page"] = self.pages[0]
                kwargs["last_page"] = self.pages[1]

            images = convert_from_path(str(self.file_path), **kwargs)
            text_parts = []
            for img in images:
                page_text = pytesseract.image_to_string(img, lang=self.language)
                if page_text and page_text.strip():
                    text_parts.append(page_text.strip())

            text = "\n\n".join(text_parts)
            if not text.strip():
                text = "[OCR extraction produced no readable text from this document]"

            return RawContent(
                text=text,
                source_type="pdf",
                metadata={
                    "file_path": str(self.file_path),
                    "file_size": self.file_path.stat().st_size,
                    "page_count": len(images),
                    "extraction_method": "ocr",
                    "ocr_language": self.language,
                    "ocr_dpi": self.dpi,
                },
            )
        except ImportError:
            raise
        except Exception as e:
            raise IOError(f"Error performing OCR on PDF {self.file_path}: {e}")


class ImagePDFAdapter:
    def __init__(self, file_path: str, output_dir: str = "results/extracted", pages: tuple = None):
        self.file_path = Path(file_path)
        self.output_dir = Path(output_dir)
        self.pages = pages

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            import fitz
        except ImportError:
            raise ImportError(
                "Image PDF extraction requires PyMuPDF: pip install PyMuPDF"
            )

        try:
            doc = fitz.open(str(self.file_path))
            page_count = len(doc)
            text_parts = []
            image_files = []

            images_dir = self.output_dir / self.file_path.stem / "images"
            images_dir.mkdir(parents=True, exist_ok=True)

            pages_range = range(len(doc))
            if self.pages:
                start, end = self.pages
                pages_range = range(start - 1, min(end, len(doc)))

            for page_idx in pages_range:
                page = doc[page_idx]
                page_num = page_idx + 1

                page_text = page.get_text()
                if page_text and page_text.strip():
                    text_parts.append(page_text.strip())

                image_list = page.get_images(full=True)
                for img_idx, img_info in enumerate(image_list, start=1):
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    if base_image:
                        img_ext = base_image.get("ext", "png")
                        img_filename = f"page{page_num}_img{img_idx}.{img_ext}"
                        img_path = images_dir / img_filename

                        with open(img_path, "wb") as f:
                            f.write(base_image["image"])

                        image_files.append(str(img_path))
                        text_parts.append(f"[Image: {img_filename}]")

            doc.close()

            text = "\n\n".join(text_parts)
            if not text.strip():
                text = f"[Document contains {len(image_files)} image(s), no extractable text]"

            return RawContent(
                text=text,
                source_type="pdf",
                metadata={
                    "file_path": str(self.file_path),
                    "file_size": self.file_path.stat().st_size,
                    "page_count": page_count,
                    "extraction_method": "images",
                    "images_dir": str(images_dir),
                    "images_count": len(image_files),
                    "image_files": image_files,
                },
            )
        except ImportError:
            raise
        except Exception as e:
            raise IOError(f"Error extracting images from PDF {self.file_path}: {e}")


class TextAdapter:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> RawContent:
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        text = self.file_path.read_text(encoding="utf-8")
        return RawContent(
            text=text,
            source_type="text",
            metadata={
                "file_path": str(self.file_path),
                "file_size": self.file_path.stat().st_size,
            },
        )


class InlineAdapter:
    def __init__(self, text: str, metadata: dict = None):
        self.text = text
        self.metadata = metadata or {}

    def load(self) -> RawContent:
        return RawContent(text=self.text, source_type="inline", metadata=self.metadata)


BGG_BASE_HEADERS = {
    "User-Agent": "BoardgameRulesAnalyser/1.0 (Python; Educational Project)",
    "Accept": "application/xml",
}


class BGGAdapter:
    def __init__(
        self,
        game_id: Optional[int] = None,
        game_name: Optional[str] = None,
        api_token: Optional[str] = None,
        cache_dir: str = "cache/bgg",
        cache_expiry_days: int = 30,
        rate_limit_seconds: float = 5.0,
    ):
        if game_id is None and game_name is None:
            raise ValueError("Either game_id or game_name must be provided")

        self.game_id = game_id
        self.game_name = game_name
        self.api_token = api_token
        self._resolved_id: Optional[int] = None
        self.cache_dir = Path(cache_dir)
        self.cache_expiry_days = cache_expiry_days
        self.rate_limit_seconds = rate_limit_seconds
        self.base_url = "https://boardgamegeek.com/xmlapi2"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.headers = {**BGG_BASE_HEADERS, "Authorization": f"Bearer {api_token}"}

    def _search_by_name(self, name: str) -> int:
        time.sleep(self.rate_limit_seconds)

        try:
            response = requests.get(
                f"{self.base_url}/search",
                params={"query": name, "type": "boardgame", "exact": 1},  # type: ignore[arg-type]
                headers=self.headers,
                timeout=10,
            )
            response.raise_for_status()

            root = ET.fromstring(response.text)
            items = root.findall("item")

            if items:
                game_id = int(items[0].get("id"))
                print(f"Found exact match: {items[0].find('name').get('value')} (ID: {game_id})")
                return game_id

            time.sleep(self.rate_limit_seconds)
            response = requests.get(
                f"{self.base_url}/search",
                params={"query": name, "type": "boardgame"},
                headers=self.headers,
                timeout=10,
            )
            response.raise_for_status()

            root = ET.fromstring(response.text)
            items = root.findall("item")

            if not items:
                raise ValueError(f"No game found with name: {name}")

            game_id = int(items[0].get("id"))
            game_name = items[0].find("name").get("value")
            print(f"Found match: {game_name} (ID: {game_id})")
            return game_id

        except requests.RequestException as e:
            raise IOError(f"BGG search failed for '{name}': {e}")

    def _get_game_id(self) -> int:

        if self.game_id is not None:
            return self.game_id

        if self._resolved_id is None:
            self._resolved_id = self._search_by_name(self.game_name)

        return self._resolved_id

    def load(self) -> RawContent:

        game_id = self._get_game_id()
        cache_file = self.cache_dir / f"{game_id}.xml"

        if cache_file.exists():
            cache_age = datetime.now() - datetime.fromtimestamp(cache_file.stat().st_mtime)
            if cache_age < timedelta(days=self.cache_expiry_days):
                xml_data = cache_file.read_text(encoding="utf-8")
                return self._parse_xml(xml_data, from_cache=True, game_id=game_id)

        time.sleep(self.rate_limit_seconds)

        try:
            response = requests.get(
                f"{self.base_url}/thing",
                params={"id": game_id, "stats": 1},
                headers=self.headers,
                timeout=10,
            )
            response.raise_for_status()
            xml_data = response.text

            cache_file.write_text(xml_data, encoding="utf-8")

            return self._parse_xml(xml_data, from_cache=False, game_id=game_id)

        except requests.RequestException as e:
            raise IOError(f"Fetch BGG fallito per gioco {game_id}: {e}")

    def _parse_xml(self, xml_data: str, from_cache: bool, game_id: int) -> RawContent:
        try:
            root = ET.fromstring(xml_data)
            item = root.find("item")

            if item is None:
                raise ValueError("XML BGG invalido: nessun item trovato")

            name_elem = item.find("name[@type='primary']")
            name = name_elem.get("value") if name_elem is not None else "Unknown"

            mechanics = []
            for link in item.findall("link[@type='boardgamemechanic']"):
                mech = link.get("value", "")
                if mech:
                    mechanics.append(mech)

            stats = item.find("statistics/ratings")
            complexity = 0.0
            if stats is not None:
                avg_weight = stats.find("averageweight")
                if avg_weight is not None:
                    try:
                        complexity = float(avg_weight.get("value", 0.0))
                    except ValueError:
                        complexity = 0.0

            try:
                minplayers_elem = item.find("minplayers")
                min_players = int(minplayers_elem.get("value", 0)) if minplayers_elem is not None else 0
                maxplayers_elem = item.find("maxplayers")
                max_players = int(maxplayers_elem.get("value", 0)) if maxplayers_elem is not None else 0
            except ValueError:
                min_players = 0
                max_players = 0

            try:
                playingtime_elem = item.find("playingtime")
                playing_time = int(playingtime_elem.get("value", 0)) if playingtime_elem is not None else 0
            except ValueError:
                playing_time = 0

            text = f"""Game: {name}
Mechanics: {', '.join(mechanics)}
Complexity: {complexity}/5
Players: {min_players}-{max_players}
Duration: {playing_time} minutes"""

            return RawContent(
                text=text,
                source_type="bgg",
                metadata={
                    "game_id": game_id,
                    "name": name,
                    "mechanics": mechanics,
                    "complexity": complexity,
                    "min_players": min_players,
                    "max_players": max_players,
                    "duration": playing_time,
                    "from_cache": from_cache,
                },
            )

        except (ET.ParseError, ValueError, AttributeError) as e:
            raise IOError(f"Parsing XML BGG fallito: {e}")


class ConceptAdapter:
    def __init__(self, text: str):
        self.text = text

    def load(self) -> RawContent:
        return RawContent(
            text=self.text, source_type="concept", metadata={"source": "user_input"}
        )
