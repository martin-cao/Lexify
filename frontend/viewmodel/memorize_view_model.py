from PySide6.QtWidgets import QWidget, QStackedWidget, QMainWindow, QLabel, QPushButton, QComboBox, QGridLayout, QGraphicsBlurEffect
from PySide6.QtCore import QTimer
import random

from viewmodel.message import show_popup_message

from database.database import DatabaseConnection

from controller.learning_controller import start_learning, start_reviewing

class MemorizeViewModel:
    def __init__(self, view: QWidget, main_window: QMainWindow, is_review: bool = False):
        self.main_window = main_window
        self.db_conn = DatabaseConnection()
        self.session = self.db_conn.get_session()

        # Get stackedWidget to switch views
        self.stackedWidget = main_window.findChild(QStackedWidget, "stackedWidget")
        # Get elements on the memorising view
        self.label_word = view.findChild(QLabel, "label_memorize_word")
        self.button_back = view.findChild(QPushButton, "pushButton_memorize_back")
        self.button_option_1 = view.findChild(QPushButton, "pushButton_memorize_option_1")
        self.button_option_2 = view.findChild(QPushButton, "pushButton_memorize_option_2")
        self.button_option_3 = view.findChild(QPushButton, "pushButton_memorize_option_3")
        self.button_option_4 = view.findChild(QPushButton, "pushButton_memorize_option_4")
        self.button_forgot = view.findChild(QPushButton, "pushButton_memorize_forgot")

        self.comboBox_lib = view.findChild(QComboBox, "comboBox_lib")

        # Connect buttons with slot functions
        # self.button_back.clicked.connect(self.exit_memorize_view)
        # 4+1 options' connections
        self.button_option_1.clicked.connect(lambda: self.on_option_clicked(0))
        self.button_option_2.clicked.connect(lambda: self.on_option_clicked(1))
        self.button_option_3.clicked.connect(lambda: self.on_option_clicked(2))
        self.button_option_4.clicked.connect(lambda: self.on_option_clicked(3))
        self.button_forgot.clicked.connect(lambda: self.on_option_clicked('forgot'))

        # 把4个选项按钮放进列表，以便统一操作
        self.buttons = [
            self.button_option_1,
            self.button_option_2,
            self.button_option_3,
            self.button_option_4
        ]

        # All memorize data for current round
        self.memorize_data = [] # List[dict]
        '''
        # self.memorize_data = [
        #   {
        #       "progress_id": 12,
        #       "word": "apple",
        #       "definition": "...",
        #       "proficiency": 0,
        #       "mode": "new" or "review",
        #       "n": 0 or 3 or something,  # 用于记录“本轮背诵的状态”，表示本轮中单词的熟练度
        #       "done": False,            # 是否本轮已完成
        #       "attempt_count": 0,       # 用户总共答了几次(含看答案/忘了)
        #       "correct_count": 0,       # 用户正确次数
        #       "see_answer_count": 0,    # 用户看答案次数
        #   },
        #   ... 
        # ]
        '''
        # Current index of word displayed
        self.current_index = 0
        # Index of the right answer
        self.right_index = 0

    # def exit_memorize_view(self):
    #     confirm = show_popup_message(
    #         message="确定退出吗？这会丢失本次背词进度",
    #         title="你确定吗",
    #         msg_type="question"
    #     )
    #     if confirm:
    #         self.stackedWidget.setCurrentIndex(2)
    #     else:
    #         pass

    def load_memorize_data(self, word_list: list):
        """
        word_list: 来自 learning_controller.learn_new_words() 或 review_words() 的返回值
           形如: [
             {"progress_id": 1, "word":"apple", "definition":"...", "proficiency":0, "mode":"new"},
             {"progress_id": 2, "word":"banana","definition":"...", "proficiency":30,"mode":"review"},
             ...
           ]

        fix: word_list 就是单纯的[Word]
        """
        self.memorize_data.clear()
        for item in word_list:
            self.memorize_data.append({
                "progress_id": item["progress_id"], # -1 if newly learn
                "word": item["word"],
                "definition": item["definition"],
                "proficiency": item["proficiency"],
                "mode": item["mode"],
                "n": 0,  # 对 new: 一开始 n=0; 对 review: 我们先留在 0, 由第一次判断来决定
                "done": False,
                "attempt_count": 0,
                "correct_count": 0,
                "see_answer_count": 0,
            })

        print("[DEBUG] load_memorize_data() ran.")

        self.current_index = 0
        # 展示第一个单词到UI
        self.show_current_word()

    def show_current_word(self):
        if self.current_index >= len(self.memorize_data):
            all_done = True
            for progress in self.memorize_data:
                if progress["done"] == False:
                    all_done = False
            if all_done:
                # 说明已经没有单词可显示了 => 本轮结束
                self.finish_memorize_session()
                return
            else:
                self.current_index = 0

        current_item = self.memorize_data[self.current_index]
        # 如果已 done，则跳到下一个
        if current_item["done"]:
            self.current_index += 1
            self.show_current_word()
            return

        # 随机决定题型：True = (看释义，选单词)，False = (看单词，选释义)
        # 你也可以加一个百分比几率，比如 random.random()<0.5
        is_definition_prompt = random.choice([True, False])

        if is_definition_prompt:
            # 题型: 显示“释义”，让用户从4个“单词”中选
            prompt_text = current_item["definition"]
        else:
            # 题型: 显示“单词”，让用户从4个“释义”中选
            prompt_text = current_item["word"]

        # 设置题干显示
        self.label_word.setText(f"# {prompt_text}")

        # 决定正确按钮索引
        self.right_index = random.randint(0, 3)  # 0,1,2,3

        # 获取 3 个干扰选项
        distractors = self._get_distractors_for_current_item(current_item, count=3,
                                                             is_definition_prompt=is_definition_prompt)

        # 按钮列表，便于后续批量操作
        buttons = [
            self.button_option_1,
            self.button_option_2,
            self.button_option_3,
            self.button_option_4
        ]

        # 设置 4 个按钮文本
        for idx, btn in enumerate(buttons):
            if idx == self.right_index:
                # 正确选项
                if is_definition_prompt:
                    # 用户看到释义，要选单词 => 正确按钮显示 current_item["word"]
                    btn.setText(current_item["word"])
                else:
                    # 用户看到单词，要选释义 => 正确按钮显示 current_item["definition"]
                    btn.setText(current_item["definition"])
            else:
                # 干扰项
                distractor = distractors.pop()  # 随机取一个
                btn.setText(distractor)

        # 题目已设置完毕，等用户点击某个按钮时，会进入 on_option_clicked()

    def _get_distractors_for_current_item(self, current_item, count=3, is_definition_prompt=True):
        """
        从 self.memorize_data 中随机选出 'count' 个与 current_item 不同的干扰项。
        如果 is_definition_prompt = True，就返回单词(Word) 作为干扰；
        否则返回释义(Definition) 作为干扰。
        """
        # 拿当前正确答案
        correct_word = current_item["word"]
        correct_def = current_item["definition"]

        # 做一个候选池: 直接从 self.memorize_data 中拿
        # 也可改成全局词库/别的随机逻辑
        if is_definition_prompt:
            # 我们想要干扰项是“单词”
            # 先收集所有 memorize_data 的 word
            pool = [item["word"] for item in self.memorize_data if item["word"] != correct_word]
        else:
            # 想要干扰项是“释义”
            pool = [item["definition"] for item in self.memorize_data if item["definition"] != correct_def]

        # 如果干扰池里元素不足 count 个，可以自行补一些“假数据”或再做其他处理
        random.shuffle(pool)
        distractors = pool[:count]

        # 如果不够，就用一些占位
        while len(distractors) < count:
            distractors.append("???")

        return distractors

    def on_option_clicked(self, user_choice):
        """
        user_choice: 可能是 1,2,3,4(用户选的选项) 或者 'forgot'
        在此判断正确与否，并更新 n。
        """
        if self.current_index >= len(self.memorize_data):
            return  # 没有单词可处理

        item = self.memorize_data[self.current_index]

        # 判断第一次操作(复习模式时，可能决定 n=3 或 n=1)
        # 先判断是否已是第一次( attempt_count==0 ) 并且是 review 模式
        is_first_attempt = (item["attempt_count"] == 0)

        # 判断对错
        is_correct = (user_choice == self.right_index)

        if item["mode"] == "review" and is_first_attempt:
            # 如果用户选择正确 => n=3 (本轮结束)；否则 => n=1
            # 你需要知道哪一个选项才是正确的，这里先假设 user_choice=1 永远是正确，纯演示
            if is_correct:
                # 直接 n=3 => done
                item["n"] = 3
                item["done"] = True
                item["correct_count"] += 1
                # self.next_word()
            else:
                # n=1
                item["n"] = 1
                if user_choice == 'forgot':
                    item["see_answer_count"] += 1
                elif user_choice != 1:
                    # 选错了
                    pass  # 这里看你要不要记录错误次数
                # 找到正确按钮并高亮
                correct_button = self.buttons[self.right_index]
                correct_button.setStyleSheet("background: rgba(1, 179, 165, 0.7)")
                # # 3秒后自动跳到下一题
                # self.highlight_correct_button(self.buttons[self.right_index])
                # QTimer.singleShot(3000, self.next_word)
        else:
            # 其余情况(新学 or 复习中第二遍之后)
            # 逻辑：选对 => n+1; 选错/看答案 => n-1
            if is_correct:
                # 选对
                item["n"] += 1
                item["correct_count"] += 1
                # self.next_word()
            else:
                # 选错/看答案
                item["n"] -= 1
                if user_choice == 'forgot':
                    item["see_answer_count"] += 1
                else:
                    # 选项2/3/4也算错
                    pass
                # # 找到正确按钮并高亮
                # self.highlight_correct_button(self.buttons[self.right_index])
                # QTimer.singleShot(3000, self.next_word)
                # time.sleep(3)
                # self.proceed_to_next_word()

        item["attempt_count"] += 1

        # 判断是否达到结束条件
        if item["n"] >= 3:
            # 背够 3 遍，本轮背诵完成
            item["done"] = True
        elif item["n"] < 0:
            # 可能越背越减到负数，你看业务需求要不要干脆清0
            item["n"] = 0

        # 切到下一个单词
        if is_correct:
            self.highlight_correct_button(None)  # 或者不需要高亮
            self.next_word()
        else:
            self.highlight_correct_button(self.buttons[self.right_index])
            QTimer.singleShot(3000, self.next_word)

    def highlight_correct_button(self, btn):
        # 先恢复所有按钮样式
        for b in self.buttons:
            b.setStyleSheet("""
                QPushButton {
                    background: rgba(98, 0, 238, 0.7); /* 设置为 70% 不透明 */
                    color: #FFFFFF;
                    padding: 8px 16px;
                    border: none;
                    border-radius: 14px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background: rgba(55, 0, 179, 0.7); /* 加深主色，保持 70% 不透明 */
                }
                QPushButton:pressed {
                    background: rgba(49, 27, 146, 0.7); /* 更深一层，保持 70% 不透明 */
                }
                QPushButton:disabled {
                    background: rgba(189, 189, 189, 0.7); /* 禁用状态，保持 70% 不透明 */
                    color: rgba(224, 224, 224, 0.7);
                }
                
                /* 次级强调色按钮（不透明度设置同样适用） */
                QPushButton.secondary {
                    background: rgba(3, 218, 198, 0.7);
                    color: #000000;
                }
                QPushButton.secondary:hover {
                    background: rgba(1, 179, 165, 0.7);
                }
                QPushButton.secondary:pressed {
                    background: rgba(1, 140, 132, 0.7);
                }
            """)
        # 若传了btn，就设置高亮
        if btn:
            btn.setStyleSheet("background: rgba(1, 179, 165, 0.7)")

    def next_word(self):
        # 恢复样式
        self.highlight_correct_button(None)
        self.current_index += 1
        self.show_current_word()

    def finish_memorize_session(self):
        """
        当本轮背诵全部结束时，统计各单词的实际背诵情况 => 计算 proficiency => 调用 learning_controller.finish_review()
        """
        # 如果 memorize_data 为空说明没内容
        if not self.memorize_data:
            show_popup_message("本轮没有单词背诵", "提示", "info")
            self.stackedWidget.setCurrentIndex(2)
            return

        new_proficiencies = []
        for item in self.memorize_data:
            p_id = item["progress_id"]
            old_pf = item["proficiency"]
            mode = item["mode"]
            # 计算新的 proficiency
            # 举例：背的次数越少 => 熟练度越高增量
            #       看答案次数越多 => 减少增量
            # 这里仅做非常简化的示例
            total_attempts = item["attempt_count"]
            correct_times = item["correct_count"]
            see_answers = item["see_answer_count"]

            # 你可以自己定义更复杂的公式
            # 例如：base_gain = 10 - total_attempts
            #       if base_gain < 0: base_gain = 0
            base_gain = max(0, 10 - total_attempts)
            # 如果看答案了，就再减一些
            penalty = 2 * see_answers
            delta = base_gain - penalty

            new_pf = old_pf + delta
            if new_pf < 0:
                new_pf = 0
            if new_pf > 100:
                new_pf = 100

            new_proficiencies.append({item["word"]: new_pf})

        from controller.config_controller import load_config
        conf = load_config()
        uid = int(conf["uid"])

        # 调用后端 finish_review，统一更新数据库
        from controller.learning_controller import finish_learning
        finish_learning(progresses=self.memorize_data, new_proficiencies=new_proficiencies, uid=uid)

        # 弹窗提示
        show_popup_message("恭喜你完成了本轮背诵!", "提示", "info")
        # 返回主界面
        self.stackedWidget.setCurrentIndex(2)

    def learn_pressed(self):
        from controller.config_controller import load_config
        conf = load_config()
        uid = int(conf["uid"])
        if "lib_id" not in conf:
            show_popup_message("请先选择一个单词库！", "提示", "warning")
            return
        library_id = conf["lib_id"]

        new_list = start_learning(uid=uid, library_id=library_id, limit=20)
        if not new_list:
            # learn_new_words里已有弹窗提示"没有新单词可以背了"
            return

        print(new_list)
        self.load_memorize_data(new_list)
        print(f"[DEBUG] Loaded {len(new_list)} new words from library_id={library_id}.")

    def review_pressed(self):
        from controller.config_controller import load_config
        conf = load_config()
        uid = int(conf["uid"])
        if "lib_id" not in conf:
            show_popup_message("请先选择一个单词库！", "提示", "warning")
            return
        library_id = conf["lib_id"]

        new_list = start_reviewing(uid=uid, library_id=library_id, limit=20)
        if not new_list:
            # learn_new_words里已有弹窗提示"没有新单词可以背了"
            return

        print(new_list)
        self.load_memorize_data(new_list)
        print(f"[DEBUG] Loaded {len(new_list)} new words from library_id={library_id}.")