from flask import Flask, render_template, request, redirect
from database.db import SessionLocal, init_db
from database.models import User

app = Flask(__name__)
init_db()

@app.route("/admin")
def admin():
    session = SessionLocal()
    users = session.query(User).order_by(User.created_at.desc()).all()
    return render_template("admin.html", users=users)

@app.route("/signal", methods=["POST"])
def send_signal():
    text = request.form.get("message")
    # логика рассылки сигнала
    return redirect("/admin")