from backend.app.models.user import User, check_password
from backend.app import db

def register_user(user: User):
    """
    注册用户
    :param user
    :return: 操作结果
    """
    # Check whether username exists, then save the data into the database
    username = user.username
    password = user.password_sha256

    if not username or not password:
        return False, "用户名和密码不能为空"

    if User.query.filter_by(username=username).first():
        return False, "用户已存在"

    new_user = User(username=username, password_sha256=password)
    db.session.add(new_user)
    try:
        db.session.commit()
        return True, "注册成功"
    except Exception as e:
        db.session.rollback()
        return False, f"发生了一个错误：{str(e)}"


def login_user(user: User):
    """
    用户登录
    :param user
    :return: 登录结果
    """
    username = user.username
    password = user.password_sha256

    user=User.query.filter_by(username=username).first()
    if not user:
        return False, "用户名不存在"
    if not user.check_password(password):
        return False, "密码错误"
    return True

def logout_user():
    """
    用户登出
    This function is currently not used, since there is no log in data stored in the backend database.
    :return: 登出结果
    """
    return True

def edit_user(user: User, new_password):
    """
    编辑用户信息
    :param user:
    :return:
    """

    username = user.username
    password = user.password_sha256

    if not username or not password or not new_password:
        return "用户名和密码不能为空"

    # 查找用户
    user = User.query.filter_by(username=username).first()
    if not user:
        return False, "用户不存在"

    # Check if the old password is correct
    if not check_password(username, password):
        return False, "密码错误"

    # 更新密码
    user.set_password(new_password)
    try:
        db.session.commit()
        return True, "修改成功"
    except Exception as e:
        db.session.rollback()
        return False, f"发生了一个错误：{str(e)}"
