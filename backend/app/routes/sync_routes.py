from flask import Blueprint, request, jsonify

from app.services.sync_service import merge_progress_records, fetch_progress_for_user

from app.models.user import check_password, get_user_by_id

sync_bp = Blueprint("sync_bp", __name__)

def authenticate_user(uid: int, pwd: str) -> bool:
    """
    验证用户身份，调用 check_password() 函数。
    uid: 用户ID
    pwd: 用户密码
    返回值: True 或 False
    """
    # 假设 check_password 接收 (username, password) 参数
    # 这里假设你有一个方法根据 uid 获取 username
    username = get_user_by_id(uid).username
    if not username:
        return False
    return check_password(username, pwd)

@sync_bp.route("/api/sync/upload", methods=["POST"])
def upload_progress():
    uid = request.args.get("uid", type=int)
    pwd = request.args.get("pwd", type=str)

    if not uid or not pwd:
        return jsonify({"error": "uid and pwd required"}), 400

    # 验证用户身份
    if not authenticate_user(uid, pwd):
        return jsonify({"error": "Authentication failed"}), 401

    data = request.get_json()
    progress_list = data.get("progresses", [])
    result = merge_progress_records(progress_list)
    return jsonify({
        "status": "ok",
        "inserted": result["inserted"],
        "updated": result["updated"]
    }), 200

@sync_bp.route("/api/sync/download", methods=["GET"])
def download_progress():
    uid = request.args.get("uid", type=int)
    pwd = request.args.get("pwd", type=str)

    if not uid or not pwd:
        return jsonify({"error": "uid and pwd required"}), 400

    # 验证用户身份
    if not authenticate_user(uid, pwd):
        return jsonify({"error": "Authentication failed"}), 401

    recs = fetch_progress_for_user(uid)
    return jsonify({
        "progresses": recs
    }), 200