from crewai import Agent, Task

from app.llm import llm
from app.tools.orders import get_pizzas, order_confirm, create_order, update_order_status

user_agent = Agent(role="Customer Support Agent", goal="Help users choose and order pizzas",
    backstory=("You are a friendly customer service agent for a pizza delivery service. "
               "Your job is to make the ordering process seamless and keep the user informed."), llm=llm)

user_task = Task(description=("Help the user choose a pizza from the menu \n"
                              "<USER_INPUT>{user_input}</USER_INPUT> \n"
                              "List all pizza using get_pizzas tool. Check match pizza name with user input. \n"
                              "<USER_ID>{user_id}</USER_ID> \n"
                              "Ask user to confirm the order using order_confirm tool, Remember ask user to confirm the order before creating order. \n"
                              "Use create_order function to create order use provided user_id from input & pizza_id from user's selection. \n"
                              "change order status to 'confirmed' using update_order_status tool, use order_id from previous & status. \n"

), expected_output="Greet customer, Return User ID, Order ID, Pizza ID, Pizza Name, Price, and Order Status", agent=user_agent,
    tools=[order_confirm, get_pizzas, create_order, update_order_status], )
