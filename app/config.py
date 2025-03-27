import os
from dotenv import load_dotenv

load_dotenv()  # 加载.env文件

class Config:
    ENV = 'development'
    # SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")

    #     python -c "import os; print repr(os.urandom(24));"
    SECRET_KEY = b'\xc9\xf6&\x1c\xfeD\x1f\xee~\xa3P\xf6\x0b\xf3\x1b\xe2\xb8\xe9\x01\xdb3\x0e\xac\x10'

    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")