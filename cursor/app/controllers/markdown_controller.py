from fastapi import APIRouter, UploadFile, File, Depends
from cursor.app.services.markdown_service import MarkdownService

router = APIRouter()


@router.post("/convert-to-markdown")
async def convert_to_markdown(
    file: UploadFile = File(...), service: MarkdownService = Depends(MarkdownService)
):
    markdown_content = service.convert_pdf_to_markdown(file)
    return {"result": markdown_content} 