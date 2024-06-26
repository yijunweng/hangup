import sys
from constant import dbdl, xkly, bfdl, yszd, mwdl, aydl, roles
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton, QGroupBox, QLabel, QLineEdit
from operate import start

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("异世界勇者自动地下城脚本")
        self.setGeometry(100, 100, 400, 200)

        # 创建主布局
        main_layout = QVBoxLayout()

        # 存储所有多选框的列表
        all_checkboxes_lists = []

        # 数据列表和组名的对应关系
        data_lists = {
            "东部大陆": dbdl,
            "虚空领域": xkly,
            "冰封大陆": bfdl,
            "元素之地": yszd,
            "迷雾大陆": mwdl,
            "暗影大陆": aydl
        }

        # 创建时长输入框和标签
        duration_label = QLabel("时长（秒）:")
        self.duration_input = QLineEdit()
        self.duration_input.setPlaceholderText("输入时长")
        
        # 添加输入框和标签到横向布局
        duration_layout = QHBoxLayout()
        duration_layout.addWidget(duration_label)
        duration_layout.addWidget(self.duration_input)

        # 添加横向布局到主布局
        main_layout.addLayout(duration_layout)

        # 创建角色多选框
        role_groupbox = QGroupBox("角色选择")
        role_layout = QVBoxLayout()

        self.role_checkboxes = []

        # 每行显示的角色个数
        roles_per_row = 5
        role_row_layout = None

        for i, role in enumerate(roles):
            if i % roles_per_row == 0:
                if role_row_layout is not None:
                    role_layout.addLayout(role_row_layout)
                role_row_layout = QHBoxLayout()

            checkbox = QCheckBox(role["role"])
            checkbox.setProperty("data", role)
            role_row_layout.addWidget(checkbox)
            self.role_checkboxes.append(checkbox)

        if role_row_layout is not None:
            role_layout.addLayout(role_row_layout)

        role_groupbox.setLayout(role_layout)
        main_layout.addWidget(role_groupbox)

        for group_name, data_list in data_lists.items():
            # 创建组
            group = QGroupBox(group_name) # 创建group，并赋值name
            group_layout = QVBoxLayout(group)

            # 创建横向布局，用于容纳多选框
            checkboxes_layout = QHBoxLayout()

            # 存储多选框的列表
            checkboxes_list = []

            for index, item in enumerate(data_list):
                checkbox = QCheckBox(item.name)
                data = {
                    "region_name": item.region["regionName"],
                    "regionPosition": item.region["position"], 
                    "dxc_name": item.name,
                    "dxcPosition": item.dxcPosition,
                    "index": item.index
                    }
                checkbox.setProperty("data", data)

                checkboxes_layout.addWidget(checkbox)
                checkboxes_list.append(checkbox)

                # 每8个多选框换一行
                if (index + 1) % 8 == 0:
                    group_layout.addLayout(checkboxes_layout)
                    checkboxes_layout = QHBoxLayout()

            # 添加剩余的多选框布局
            if checkboxes_layout.count() > 0:
                group_layout.addLayout(checkboxes_layout)

            # 添加组到主布局
            main_layout.addWidget(group)

            # 存储多选框列表
            all_checkboxes_lists.append(checkboxes_list)

        # 创建按钮
        button_hangup = QPushButton("开始挂机")
        main_layout.addWidget(button_hangup)

        # 设置主布局
        self.setLayout(main_layout)

        # 连接按钮的点击事件
        button_hangup.clicked.connect(self.get_checked_checkbox_data)

        # 存储所有多选框的列表
        self.all_checkboxes_lists = all_checkboxes_lists

    # 获取用户输入的时长和选中的角色
    def get_checked_checkbox_data(self):
        duration = self.duration_input.text()
        try:
            duration = int(duration)
            # 验证时长在30到200之间
            if not 30 <= duration <= 200:
                raise ValueError("时长应在30到200之间")
        except ValueError as e:
            print(f"无效的时长：{e}")
            return

        # 存储被选中的地下城
        selected_options = []

        # 遍历选中的地下城多选框
        for checkboxes_list in self.all_checkboxes_lists:
            for checkbox in checkboxes_list:
                if checkbox.isChecked():
                    data = checkbox.property("data")
                    print(f"选中的多选框文本: {checkbox.text()}, 绑定的数据: {data}")
                    selected_options.append(data)

        # 存储被选中的角色
        selected_roles = []
        for checkbox in self.role_checkboxes:
            if checkbox.isChecked():
                data = checkbox.property("data")
                print(f"选中的多选框文本: {checkbox.text()}, 绑定的数据: {data}")
                selected_roles.append(data)

        print("选中的角色：", selected_roles)

        start(selected_options, duration, selected_roles)
        print("所选地下城已完成！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
