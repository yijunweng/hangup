import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from operate import start_ad

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("异世界勇者自动看广告")
        self.setGeometry(100, 100, 400, 200)

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建广告输入框和按钮
        ad_layout = QHBoxLayout()
        self.ad_values = []  # 用于存储输入框中的数字

        for i in range(1, 5):
            label = QLabel(f"广告{i}:")
            ad_edit = QLineEdit(self)
            ad_edit.setText("0")  # 设置默认值为 "0"
            ad_layout.addWidget(label)
            ad_layout.addWidget(ad_edit)
            setattr(self, f'ad_edit_{i}', ad_edit)
            self.ad_values.append(ad_edit)  # 将输入框添加到数组

        main_layout.addLayout(ad_layout)

        # 创建按钮
        button_ad = QPushButton("看广告")
        main_layout.addWidget(button_ad)

        # 设置主布局
        self.setLayout(main_layout)

        # 连接按钮的点击事件
        button_ad.clicked.connect(self.watch_ad)

    def watch_ad(self):
        ad_array = [int(ad.text()) for ad in self.ad_values]
        print("广告数组:", ad_array)
        # 在这里可以使用 ad_array 进行你的逻辑处理
        start_ad(ad_array)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
