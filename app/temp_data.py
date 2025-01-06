from sqlalchemy.orm import Session
from app.models import Pizza, User, Chef, DeliveryBoy
from app.db import engine, session

def populate_pizza_db():
    # Define 10 pizzas
    pizzas = [
        Pizza(name="Margherita", description="Classic Margherita with fresh basil and mozzarella.", price=8.99),
        Pizza(name="Pepperoni", description="Pepperoni with mozzarella and tomato sauce.", price=10.99),
        Pizza(name="Veggie", description="Loaded with vegetables like bell peppers, onions, and olives.", price=9.99),
        Pizza(name="BBQ Chicken", description="BBQ sauce with chicken, onions, and mozzarella.", price=12.99),
        Pizza(name="Hawaiian", description="Ham and pineapple on a mozzarella base.", price=11.99),
        Pizza(name="Cheese Burst", description="Extra cheesy pizza with a crispy crust.", price=9.49),
        Pizza(name="Tandoori Paneer", description="Indian-style pizza with paneer and spices.", price=11.49),
        Pizza(name="Mexican Wave", description="Spicy pizza with jalapeños, onions, and corn.", price=10.49),
        Pizza(name="Peri Peri", description="Spicy Peri-Peri chicken with bell peppers.", price=12.49),
        Pizza(name="Farmhouse", description="Loaded with vegetables and a cheese burst base.", price=10.99),
    ]
    with Session(engine) as session:
    # Add the pizzas to the database
        session.add_all(pizzas)
        session.commit()

    print("Pizza database populated with 10 entries!")

def populate_users():
    users = [
        User(id=1, name="Emma Johnson", address="123 Maple Street, Springfield", wallet=50.0),
        User(id=2, name="Liam Smith", address="456 Oak Avenue, Rivertown", wallet=75.0),
        User(id=3, name="Olivia Williams", address="789 Pine Road, Lakeview", wallet=60.0),
        User(id=4, name="Noah Brown", address="321 Birch Lane, Hillcrest", wallet=80.0),
        User(id=5, name="Ava Jones", address="654 Cedar Drive, Brookside", wallet=55.0),
        User(id=6, name="William Garcia", address="987 Spruce Street, Meadowbrook", wallet=90.0),
        User(id=7, name="Sophia Martinez", address="147 Elm Avenue, Fairview", wallet=65.0),
        User(id=8, name="James Rodriguez", address="258 Willow Road, Greenfield", wallet=70.0),
        User(id=9, name="Isabella Davis", address="369 Aspen Street, Sunnyvale", wallet=85.0),
        User(id=10, name="Benjamin Hernandez", address="159 Cherry Lane, Pleasantville", wallet=95.0),
    ]
    session.add_all(users)
    session.commit()
    print("Users added.")

def populate_delivery_boys():
    delivery_boys = [
        DeliveryBoy(id=1, name="Michael Wilson"),
        DeliveryBoy(id=2, name="Alexander Anderson"),
        DeliveryBoy(id=3, name="Elijah Thomas"),
        DeliveryBoy(id=4, name="Daniel Taylor"),
        DeliveryBoy(id=5, name="Matthew Moore"),
        DeliveryBoy(id=6, name="Henry Jackson"),
        DeliveryBoy(id=7, name="Jackson Martin"),
        DeliveryBoy(id=8, name="Sebastian Lee"),
        DeliveryBoy(id=9, name="Aiden Perez"),
        DeliveryBoy(id=10, name="Samuel Thompson"),
    ]
    session.add_all(delivery_boys)
    session.commit()
    print("DeliveryBoys added.")

def populate_chefs():
    chefs = [
        Chef(id=1, name="Charlotte White"),
        Chef(id=2, name="Amelia Harris"),
        Chef(id=3, name="Mia Clark"),
        Chef(id=4, name="Harper Lewis"),
        Chef(id=5, name="Evelyn Walker"),
        Chef(id=6, name="Abigail Young"),
        Chef(id=7, name="Emily King"),
        Chef(id=8, name="Ella Wright"),
        Chef(id=9, name="Madison Scott"),
        Chef(id=10, name="Scarlett Green"),
    ]
    session.add_all(chefs)
    session.commit()
    print("Chefs added.")
