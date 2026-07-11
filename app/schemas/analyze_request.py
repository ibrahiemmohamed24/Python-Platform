from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    file_path: str