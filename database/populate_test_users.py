from database.db import SessionLocal
from database.models import User

def populate_users():
    session = SessionLocal()

    users = [
        User(telegram_id="1001", username="test_user1", language="ru"),
        User(telegram_id="1002", username="test_user2", language="en", has_deposit=True),
        User(telegram_id="1003", username="test_user3", language="tr", is_registered=True),
    ]

    session.add_all(users)
    session.commit()
    session.close()
    print("Тестовые пользователи добавлены!")

if __name__ == "__main__":
    populate_users()