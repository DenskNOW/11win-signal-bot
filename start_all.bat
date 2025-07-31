@echo off
echo [1/3] Создание таблиц в базе данных...
python -c "from database.db import Base, engine; Base.metadata.create_all(engine)"

echo [2/3] Добавление тестовых пользователей...
python database\populate_test_users.py

echo [3/3] Запуск Flask сервера (панель и postback)...
start cmd /k "python web\app.py"

echo Готово! Открой http://localhost:5000/admin
pause
