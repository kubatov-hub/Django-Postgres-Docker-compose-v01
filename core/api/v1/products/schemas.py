from datetime import datetime
from ninja import Schema


class ProductSchema(Schema):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None
    

ProductListSchema = list[ProductSchema]