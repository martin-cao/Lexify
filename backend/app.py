from flask import Blueprint, request, jsonify
from app.services.auth_service import (
    register_user,
    login_user,
    logout_user
)

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['POST'])
def register():

    # 注册逻辑
    # 获取用户输入数据
    # 调用 register_user 函数
    # 返回JSON结果
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # 登录逻辑
    # 获取用户名密码
    # 调用 login_user 函数
    # 返回是否成功（本项目中登陆等权限相关操作不作token验证 太复杂了图省事吧）
    pass

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # 调用 logout_user 函数
    pass

@auth_bp.route('/edit', methods=['POST'])
def edit_user():
    # 编辑用户信息逻辑
    pass