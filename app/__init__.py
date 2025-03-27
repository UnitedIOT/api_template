from flask import Flask
from flask_migrate import Migrate
from .extensions import db, jwt
from .routes.auth import auth_bp
from .routes.users import users_bp

def print_routes(app):
    """优雅地打印所有路由信息"""
    routes = []
    for rule in app.url_map.iter_rules():
        # 过滤掉静态文件路由
        if "static" not in rule.endpoint:
            methods = ','.join(rule.methods)
            routes.append({
                "Endpoint": rule.endpoint,
                "Path": str(rule),
                "Methods": methods
            })

    # 格式化输出
    print("\n\033[94mRegistered Routes:\033[0m")
    print("-" * 70)
    print(f"\033[93m{'Endpoint':<30} | {'Path':<30} | {'Methods':<10}\033[0m")
    print("-" * 70)
    for route in routes:
        print(f"{route['Endpoint']:<30} | {route['Path']:<30} | {route['Methods']:<10}")
    print("\n")

def create_app(config_class="app.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)
    
    # 注册蓝图
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    # 仅在开发环境显示路由
    if app.config['ENV'] == 'development':
        with app.app_context():
            print_routes(app)
    
    return app