from PySide6.QtWidgets import QMessageBox


def show_popup_message(
        message: str,
        title: str = "提示",
        msg_type: str = "info"
) -> bool:
    """
    通用弹窗接口:
      - message: 弹窗中要显示的具体文本内容
      - title: 弹窗窗口标题
      - msg_type: 可选值 {info, warning, error, question}，决定弹窗图标和默认标题
    Usage:
      show_popup_message("登录失败，请重试", "登录错误", "error")
    """
    msg_box = QMessageBox()

    # 1) 设置默认图标（根据类型）
    if msg_type.lower() == "info":
        msg_box.setIcon(QMessageBox.Information)
        default_title = "信息"
    elif msg_type.lower() == "warning":
        msg_box.setIcon(QMessageBox.Warning)
        default_title = "警告"
    elif msg_type.lower() == "error":
        msg_box.setIcon(QMessageBox.Critical)
        default_title = "错误"
    elif msg_type.lower() == "question":
        msg_box.setIcon(QMessageBox.Question)
        default_title = "询问"
    else:
        # 如果传入了未知类型，就不设置图标
        msg_box.setIcon(QMessageBox.NoIcon)
        default_title = "提示"

    # 2) 如果没有传自定义标题，就用 default_title
    if not title:
        title = default_title

    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    # 3) 根据 msg_type 设定按钮并执行弹窗
    if msg_type.lower() == "question":
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        clicked_button = msg_box.exec()
        # 如果用户点了 Yes，返回 True；否则返回 False
        return (clicked_button == QMessageBox.Yes)
    else:
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
        # 非 question 类型，弹窗只有 OK，一律返回 True
        return True