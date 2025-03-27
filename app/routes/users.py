# app/routes/users.py
from flask import Blueprint

users_bp = Blueprint("users", __name__)  # 变量名必须为 users_bp

@users_bp.route("/")
def get_users():
    return "User List"