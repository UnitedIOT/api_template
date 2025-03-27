from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# 初始化扩展对象（先创建实例，后关联app）
db = SQLAlchemy()
jwt = JWTManager()

# 可选：其他扩展（如邮件、缓存等）
# mail = Mail()
# cache = Cache()