from datetime import date, datetime
from app.models.user import UserLibraryProgress
from app import db
from sqlalchemy import and_

def merge_progress_records(progress_list: list):
    """
    progress_list 形如:
    [
      {
        "user_id": 2,
        "library_id": 1,
        "word_id": 1234,
        "proficiency": 50,
        "last_review": "2025-01-09",
        "next_review": "2025-01-10",
        "review_count": 3,
        "ease_factor": 0
      },
      ...
    ]
    对于每一个条目:
      1. 根据 (user_id, library_id, word_id) 在 user_library_progress 中查找
      2. 如果存在 => UPDATE
      3. 如果不存在 => INSERT
    """
    count_insert = 0
    count_update = 0

    for item in progress_list:
        user_id = item["user_id"]
        word_id = item["word_id"]
        proficiency = item["proficiency"]
        last_review = item.get("last_review")
        next_review = item.get("next_review")
        review_count = item["review_count"]
        ease_factor = item.get("ease_factor", 0)  # 如果没有则默认0

        def parse_date(d):
            if d:
                return datetime.strptime(d, "%Y-%m-%d").date()
            return None

        lr = parse_date(last_review)
        nr = parse_date(next_review)

        # 查找
        existing = UserLibraryProgress.query.filter(
            and_(
                UserLibraryProgress.user_id == user_id,
                UserLibraryProgress.word_id == word_id,
            )
        ).first()

        if existing:
            # Update
            existing.proficiency = proficiency
            existing.last_review = lr
            existing.next_review = nr
            existing.review_count = review_count
            existing.ease_factor = ease_factor
            count_update += 1
        else:
            # Insert
            new_rec = UserLibraryProgress(
                user_id=user_id,
                word_id=word_id,
                proficiency=proficiency,
                last_review=lr,
                next_review=nr,
                review_count=review_count,
                ease_factor=ease_factor
            )
            db.session.add(new_rec)
            count_insert += 1

    db.session.commit()
    return {"inserted": count_insert, "updated": count_update}

def fetch_progress_for_user(uid: int):
    """
    返回某用户的 user_library_progress 全部(或按需过滤)的数据，用于下载给前端
    """
    recs = (
        UserLibraryProgress.query
        .filter(UserLibraryProgress.user_id == uid)
        .all()
    )
    # 转成可序列化的列表
    result_list = []
    for r in recs:
        result_list.append({
            "user_id": r.user_id,
            "word_id": r.word_id,
            "proficiency": r.proficiency,
            "last_review": r.last_review.strftime("%Y-%m-%d") if r.last_review else None,
            "next_review": r.next_review.strftime("%Y-%m-%d") if r.next_review else None,
            "review_count": r.review_count,
            "ease_factor": r.ease_factor,
        })
    return result_list