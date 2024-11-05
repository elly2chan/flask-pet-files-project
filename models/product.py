from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from db import db


class ProductModel(db.Model):
    """
    Represents a product in the system.

    Attributes:
        id (int): Unique identifier for the product.
        title (str): The title of the product, which must be unique.
        description (str): A description of the product.
        amount (int): The quantity of the product available in stock. Defaults to 0.
        added_on (datetime): The timestamp when the product was added. Defaults to the current time.
        updated_on (datetime): The timestamp when the product was last updated. Automatically set on update.
        photo_url (str): The URL of the product image. This field is optional.
    """

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    amount: Mapped[int] = mapped_column(db.Integer, nullable=False, default=0)
    added_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    updated_on: Mapped[datetime] = mapped_column(db.DateTime, onupdate=func.now())
    photo_url: Mapped[str] = mapped_column(db.String(255), nullable=True)
