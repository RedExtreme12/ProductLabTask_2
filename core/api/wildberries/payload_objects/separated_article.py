from pydantic import BaseModel


class SeparatedArticle(BaseModel):
    volume: str
    part: str
    full_article: str
