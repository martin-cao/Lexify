from flask import Blueprint,render_template, request, jsonify

import app.services.auth_service as service
import app.models.user as user


user_bp = Blueprint('user', __name__)

@user_bp.route('/api/register', methods=['POST'])
def register():
    try:
        # Parse request body
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        # new_user = user.User(username=username, password_sha256=password)

        # Validate parameters
        if not username or not password:
            return jsonify({'status': 'error', 'message': 'Username and password are required', 'uid': None}), 400

        # Call the sign-up service
        # result, msg = service.register_user(new_user)
        result, msg, uid = service.register_user(username, password)
        # print(f'[BACKEND DEBUG] UID: {uid}')
        if result:
            return jsonify({'status': 'success', 'message': msg, 'uid': uid}), 201
        else:
            return jsonify({'status': 'error', 'message': msg, 'uid': None}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@user_bp.route('/api/login', methods=['POST'])
def login():
    try:
        # Parse request body
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        the_user = user.User(username=username, password_sha256=password)

        # Validate input
        if not username or not password:
            return jsonify({'status': 'error', 'message': 'Username and password are required', 'uid': None}), 400

        # Call the service to authenticate the user
        result, msg, uid = service.login_user(the_user)
        # print(f'[BACKEND DEBUG] UID: {uid}')
        if result == True:
            return jsonify({'status': 'success', 'message': msg, 'uid': uid}), 200
        else:
            return jsonify({'status': 'error', 'message': msg, 'uid': None}), 401

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'uid': None}), 500

@user_bp.route('/api/logout', methods=['POST'])
def logout():
    # 注销逻辑
    return 200

@user_bp.route('/api/edit', methods=['POST'])
def edit_user():
    try:
        # Parse request body and headers
        data = request.get_json()
        username = data.get('username')
        old_password = data.get('password')
        new_password = data.get('new_password')
        old_user = user.User(username=username, password_sha256=old_password)

        # Validate input
        if not new_password:
            return jsonify({'status': 'error', 'message': 'At least one field to update is required'}), 400

        # Call the service to update user information
        result, msg = service.edit_user(old_user, new_password)
        if result == True:
            return jsonify({'status': 'success', 'message': msg}), 200
        else:
            return jsonify({'status': 'error', 'message': msg}), 400
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500