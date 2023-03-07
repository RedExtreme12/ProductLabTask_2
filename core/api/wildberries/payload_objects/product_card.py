from pydantic import BaseModel


class ProductCard(BaseModel):
    article: str
    supplier_name: str
    trademark: str
