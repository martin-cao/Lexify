from flask import Blueprint, request, jsonify
# from app.models.user import User
# from app import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    # 注册逻辑
    pass

@user_bp.route('/login', methods=['POST'])
def login():
    # 登录逻辑
    pass

@user_bp.route('/logout', methods=['POST'])
def logout():
    # 注销逻辑
    pass

@user_bp.route('/edit', methods=['POST'])
def edit_user():
    # 编辑用户信息逻辑
    pass