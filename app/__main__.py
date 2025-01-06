from app.crews import order_crew
from app.db import init_db



init_db()
result = order_crew.kickoff(inputs={
    "user_input": "I want Margherita pizza.",
    "user_id": 2
})
print(result)

