import datetime

from sqlmodel import SQLModel, Field


class Pizza(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    address: str | None = None
    wallet: float = 10.0


class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: int
    pizza_id: int
    date_created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    assigned_to: str | None = None
    is_delivered: bool = False
    status: str = "pending" # pending, confirmed, accepted, cooking, ready, delivered
    delivery_boy_id: int | None = None
    review: str | None = None


class Chef(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    is_free: bool = True
    current_order_id: int | None = Field(default=None, foreign_key="order.id")


class DeliveryBoy(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    is_free: bool = True
    current_order_id: int | None = Field(default=None, foreign_key="order.id")