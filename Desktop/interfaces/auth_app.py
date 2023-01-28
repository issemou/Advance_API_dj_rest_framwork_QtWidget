from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap

from Desktop.Remote.Dao.PostDao import PostDao
from Desktop.interfaces.post_app import App


class AuthApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AUTHENTICATION")
        self.setup_ui()
        self.setup_css()
        self.setup_connections()
        self.resize(400, 50)

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_username = QtWidgets.QLineEdit()
        self.le_username.setPlaceholderText("Username@gmail.com")
        self.img = QtWidgets.QLabel(self)
        pic = QPixmap('assets/images/icons8-utilisateur-50 (1).png')
        self.img.setPixmap(pic)
        self.le_password = QtWidgets.QLineEdit()
        self.le_password.setPlaceholderText("Password")
        self.le_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.error_str = QtWidgets.QLabel("")
        self.btn_login = QtWidgets.QPushButton("Login")

        self.main_layout.addWidget(self.img)
        self.main_layout.addWidget(self.le_username)
        self.main_layout.addWidget(self.le_password)
        self.main_layout.addWidget(self.btn_login)

    def setup_connections(self):
        self.btn_login.clicked.connect(self.check_and_get_user_auth)
        self.le_username.returnPressed.connect(self.check_and_get_user_auth)
        self.le_password.returnPressed.connect(self.check_and_get_user_auth)

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        border: none;
        """)

        self.img.setStyleSheet("""
                padding-left: 6px;
                margin-left: 150px
        """)
        self.le_username.setStyleSheet("""
        background-color: white;
        color: black;
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        """)
        self.le_password.setStyleSheet("""
        background-color: white;
        color: black;
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        """)

        self.error_str.setStyleSheet("""
        background-color: red;
        color: black;
        border-style: outset;
        border-width: 2px;
        border-color: beige;
        font: bold 14px;
        padding: 6px;
        """)

        self.btn_login.setStyleSheet("""
        background-color: green;
        color: rgb(240, 240, 240);
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        margin-top: 10px
        """)

    def check_and_get_user_auth(self):
        username = self.le_username.text()
        password = self.le_password.text()
        if not username or not password:
            return False
        else:
            self.clear_input()
            PostDao().auth(username=username, password=password, on_server_data=self.on_server_data,
                           on_server_error=self.on_server_error,
                           on_request_faillure=self.on_server_faillure)

    def on_server_data(self, user):
        self.show_post_window(user)

    def on_server_error(self, error):
        self.error_str.setText(str(error))
        self.main_layout.addWidget(self.error_str)

    def on_server_faillure(self, error):
        self.error_str.setText(error)
        self.main_layout.addWidget(self.error_str)

    def show_post_window(self, user):
        if user:
            self.w = App()
            self.close()
        self.w.show()

    def clear_input(self):
        self.le_username.setText("")
        self.le_password.setText("")
