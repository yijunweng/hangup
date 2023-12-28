import sys
from dxc import dbdl, xkly
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QGroupBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("东部大陆信息")
        self.setGeometry(100, 100, 400, 200)

        # 创建主布局
        main_layout = QVBoxLayout()

        # 创建组
        group_dbdl = QGroupBox("东部大陆")
        group_layout_dbdl = QVBoxLayout(group_dbdl)
        group_xkly = QGroupBox("虚空领域")
        group_layout_xkly = QVBoxLayout(group_xkly)
        group_bfdl = QGroupBox("冰封大陆")
        group_layout_bfdl = QVBoxLayout(group_bfdl)
        group_yszd = QGroupBox("元素之地")
        group_layout_yszd = QVBoxLayout(group_yszd)
        group_mwdl = QGroupBox("迷雾大陆")
        group_layout_mwdl = QVBoxLayout(group_mwdl)

        # 1. 东部大陆数据
        # 创建横向布局，用于容纳多选框
        checkboxes_layout_dbdl = QHBoxLayout()

        # 创建多选框并绑定数据
        self.checkboxes = []  # 存储多选框的列表，以便在其他方法中访问
        for index, item in enumerate(dbdl):  # 16个多选框，每行最多8个
            checkbox = QCheckBox(item.name)
            data = {"position1": item.position1, "posisiton2": item.position2}
            checkbox.setProperty("data", data)

            checkboxes_layout_dbdl.addWidget(checkbox)
            self.checkboxes.append(checkbox)

            # 每8个多选框换一行
            if (index + 1) % 8 == 0:
                group_layout_dbdl.addLayout(checkboxes_layout_dbdl)
                checkboxes_layout_dbdl = QHBoxLayout()

        # 添加剩余的多选框布局
        if checkboxes_layout_dbdl.count() > 0:
            group_layout_dbdl.addLayout(checkboxes_layout_dbdl)

        # 2. 虚空领域数据
        # 创建横向布局，用于容纳多选框
        checkboxes_layout_xkly = QHBoxLayout()

        # 创建多选框并绑定数据
        self.checkboxes = []  # 存储多选框的列表，以便在其他方法中访问
        for index, item in enumerate(xkly):  # 16个多选框，每行最多8个
            checkbox = QCheckBox(item.name)
            data = {"position1": item.position1, "posisiton2": item.position2}
            checkbox.setProperty("data", data)

            checkboxes_layout_xkly.addWidget(checkbox)
            self.checkboxes.append(checkbox)

            # 每8个多选框换一行
            if (index + 1) % 8 == 0:
                group_layout_xkly.addLayout(checkboxes_layout_xkly)
                checkboxes_layout_xkly = QHBoxLayout()

        # 添加剩余的多选框布局
        if checkboxes_layout_xkly.count() > 0:
            group_layout_xkly.addLayout(checkboxes_layout_xkly)

        # 将组添加到主布局
        main_layout.addWidget(group_dbdl)
        main_layout.addWidget(group_xkly)
        main_layout.addWidget(group_bfdl)
        main_layout.addWidget(group_yszd)
        main_layout.addWidget(group_mwdl)
        # 创建按钮
        button = QPushButton("获取数据")
        main_layout.addWidget(button)

        # 设置主布局
        self.setLayout(main_layout)

        # 连接按钮的点击事件
        button.clicked.connect(self.get_checked_checkbox_data)

    def get_checked_checkbox_data(self):
        # 获取选中的多选框的数据
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                data = checkbox.property("data")
                print(f"选中的多选框文本: {checkbox.text()}, 绑定的数据: {data}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
