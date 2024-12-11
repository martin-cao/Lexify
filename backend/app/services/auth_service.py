from backend.app.models.user import User
from backend.app import db

def register_user(user_data):
    """
    注册用户
    :param user_data: 用户输入的数据
    :return: 操作结果
    """
    # 示例实现：检查用户名是否已存在，保存用户数据到数据库
    # 这里用简单的字典模拟数据库
    username=user_data.get('username')
    password=user_data.get('password')
    if not username or not password:
        return "用户名和密码不能为空"

    if User.query.filter_by(username=username).first():
        return "用户已存在"

def login_user(username, password):
    """
    用户登录
    :param username: 用户名
    :param password: 密码
    :return: 登录结果
    """
    user=User.query.filter_by(username=username).first()
    if not user:
        return("用户名不存在")
    if not user.check_password(password):
        return "密码错误"
    return True
def logout_user():
    """
    用户登出
    :return: 登出结果
    """
    return True
def edit_user(user_data):
    """# 编辑用户信息逻辑"""
    username = user_data.get('username')
    new_password = user_data.get('password')

    if not username or not new_password:
        return "用户名和密码不能为空"

    # 查找用户
    user = User.query.filter_by(username=username).first()
    if not user:
        return "用户不存在"

    # 更新密码
    user.set_password(new_password)
    db.session.commit()

    return True
