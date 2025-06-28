import shutil
from uuid import uuid4
from fastapi import UploadFile
from markitdown import MarkItDown

md = MarkItDown()


class MarkdownService:
    def convert_pdf_to_markdown(self, file: UploadFile) -> str:
        unique_id = uuid4()
        temp_dir = f"./temp/{unique_id}"

        shutil.os.makedirs(temp_dir, exist_ok=True)

        file_path = f"{temp_dir}/{file.filename}"
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        result = md.convert(file_path)
        content = result.text_content

        shutil.rmtree(temp_dir)

        return content 