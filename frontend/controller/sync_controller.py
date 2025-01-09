from services import sync_service

from viewmodel.message import show_popup_message

def sync_up_down(uid: int, pwd: str):
    """
    一次性先把本地进度上传到后端，再从后端下载最新进度合并到本地。
    """
    # print(f"[DEBUG] sync_controller: uid {uid} pwd {pwd}")
    try:
        print("[SYNC] Start upload...")
        sync_service.sync_upload(uid, pwd)
        print("[SYNC] Start download...")
        sync_service.sync_download(uid, pwd)
        print("[SYNC] All done!")
        show_popup_message("同步成功！", "同步成功", "info")
    except Exception as e:
        print("[SYNC] Error occurred:", e)
        # 可以在这里做 UI 提示或 logging
        show_popup_message(f"同步失败，{e}", "同步失败", "error")