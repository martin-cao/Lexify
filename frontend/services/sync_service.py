import requests
from datetime import datetime

from controller.config_controller import load_config
from model.user import LearningProgress

from database.database import DatabaseConnection

db_conn = DatabaseConnection()
session = db_conn.get_session()

# 这个URL视情况而定，你可以放在 config 中

conf = load_config()
SYNC_URL = f"{conf['SERVER_URL']}/sync"

def gather_local_progresses_to_sync(uid: int):
    """
    从本地 learning_progress 表里获取 需要上传/更新到后端的数据
    """
    progresses = (
        session.query(LearningProgress)
        .filter(LearningProgress.user_id == uid)
        .all()
    )

    # 转成可JSON序列化的 dict
    data_list = []
    for p in progresses:
        data_list.append({
            "user_id": p.user_id,
            "word_id": p.word_id,
            "proficiency": p.proficiency,
            "last_review": str(p.last_review) if p.last_review else None,
            "next_review": str(p.next_review) if p.next_review else None,
            "review_count": p.review_count,
            # ease_factor 在前端没有，或者默认0
            "ease_factor": 0
        })
    return data_list

def sync_upload(uid: int, pwd: str):
    """
    把本地 learning_progress 数据发送到后端 /api/sync/upload
    """
    local_data = gather_local_progresses_to_sync(uid)

    # 调用后端API
    url = f"{SYNC_URL}/upload?uid={uid}&pwd={pwd}"
    resp = requests.post(url, json={"progresses": local_data})
    resp.raise_for_status()  # 如果非200会抛异常

    result = resp.json()
    print("[SYNC] Upload result:", result)
    # 也可以根据后端返回的信息进行记录，比如server端有无报错等

def sync_download(uid: int, pwd: str):
    """
    从后端获取服务器端 user_library_progress 的数据，同步到本地 learning_progress
    """
    url = f"{SYNC_URL}/download?uid={uid}&pwd={pwd}"
    resp = requests.get(url)
    resp.raise_for_status()
    server_data = resp.json().get("progresses", [])

    # 合并到本地
    for item in server_data:
        user_id = item["user_id"]
        word_id = item["word_id"]
        proficiency = item["proficiency"]
        last_review = item.get("last_review")
        next_review = item.get("next_review")
        review_count = item.get("review_count")
        # ease_factor = item.get("ease_factor") # 前端不一定用

        # 转为 Date 对象
        def parse_date(d):
            if d:
                return datetime.strptime(d, "%Y-%m-%d").date()
            return None

        lr = parse_date(last_review)
        nr = parse_date(next_review)

        # 根据 (user_id, library_id, word_id) 找本地记录
        local_progress = (
            session.query(LearningProgress)
            # .filter(LearningProgress.library_id == library_id) # 如果有 library_id 字段
            .filter(LearningProgress.user_id == user_id)
            .filter(LearningProgress.word_id == word_id)
            .first()
        )
        if local_progress:
            # 更新
            local_progress.proficiency = proficiency
            local_progress.last_review = lr
            local_progress.next_review = nr
            local_progress.review_count = review_count
        else:
            # 新建
            lp = LearningProgress(
                user_id=user_id,
                word_id=word_id,
                proficiency=proficiency,
                last_review=lr,
                next_review=nr,
                review_count=review_count
            )
            session.add(lp)

    session.commit()
    print("[SYNC] Download & merge done. Got:", len(server_data), "records from server.")