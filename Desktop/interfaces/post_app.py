from PySide6 import QtWidgets, QtCore

from Desktop.Remote.Dao.PostDao import PostDao


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Post Crud API")
        self.setup_ui()
        self.setup_css()
        self.is_update = False
        self.setup_connections()
        self.show_posts()
        self.resize(400, 400)

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.le_postTitle = QtWidgets.QLineEdit()
        self.le_postDescription = QtWidgets.QLineEdit()
        self.btn_addPost = QtWidgets.QPushButton("Ajouter un Post")
        self.lw_posts = QtWidgets.QListWidget()
        self.lw_posts.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removePost = QtWidgets.QPushButton("Supprimer le(s) Post(s)")
        self.btn_updatePost = QtWidgets.QPushButton("Edite le Post")

        self.main_layout.addWidget(self.le_postTitle)
        self.main_layout.addWidget(self.le_postDescription)
        self.main_layout.addWidget(self.btn_addPost)
        self.main_layout.addWidget(self.lw_posts)
        self.main_layout.addWidget(self.btn_removePost)
        self.main_layout.addWidget(self.btn_updatePost)

    def setup_connections(self):
        self.btn_addPost.clicked.connect(self.add_post)
        self.le_postTitle.returnPressed.connect(self.add_post)
        self.le_postDescription.returnPressed.connect(self.add_post)
        self.btn_removePost.clicked.connect(self.remove_post)
        self.btn_updatePost.clicked.connect(self.edite_post)

    def populate_post(self, posts):
        self.lw_posts.clear()
        for p in posts:
            lw_item = QtWidgets.QListWidgetItem(p.title)
            lw_item.setData(QtCore.Qt.UserRole, p)
            self.lw_posts.addItem(lw_item)

    def show_posts(self):
        PostDao().get_list_post(on_server_data=self.populate_post,
                                on_server_error=self.on_server_error,
                                on_request_faillure=self.on_server_faillure)

    def add_post(self):
        post_title = self.le_postTitle.text()
        post_description = self.le_postDescription.text()

        if not post_title or not post_description:
            return False
        else:
            if self.is_update:
                PostDao().update_post(id=self.curpost, title=post_title, description=post_description,
                                      on_server_data=self.on_server_data,
                                      on_server_error=self.on_server_error,
                                      on_request_faillure=self.on_server_faillure)
                self.clear_input()
            else:
                PostDao().create_post(title=post_title, description=post_description,
                                      on_server_data=self.on_server_data,
                                      on_server_error=self.on_server_error,
                                      on_request_faillure=self.on_server_faillure)
                self.clear_input()

    def clear_input(self):
        self.le_postTitle.setText("")
        self.le_postDescription.setText("")
        self.show_posts()
        self.is_update = False

    def remove_post(self):
        for selected_item in self.lw_posts.selectedItems():
            post = selected_item.data(QtCore.Qt.UserRole)
            PostDao().delete_post(id=post.id,
                                  on_server_data=self.on_server_data,
                                  on_server_error=self.on_server_error,
                                  on_request_faillure=self.on_server_faillure
                                  )
            self.lw_posts.takeItem(self.lw_posts.row(selected_item))

    def edite_post(self):
        for selected_item in self.lw_posts.selectedItems():
            post = selected_item.data(QtCore.Qt.UserRole)
            self.curpost = post.id
            self.le_postTitle.setText(post.title)
            self.le_postDescription.setText(post.description)
            self.lw_posts.takeItem(self.lw_posts.row(selected_item))
            self.is_update = True

    def on_server_data(self, message):
        self.server_sucess = message

    def on_server_error(self, error):
        self.error_str = error.text

    def on_server_faillure(self, error):
        self.error_faillure = error.text


    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30, 30, 30);
        color: rgb(240, 240, 240);
        padding: 6px;
        border: none;
        """)
        self.le_postDescription.setStyleSheet("""
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
        self.le_postTitle.setStyleSheet("""
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

        self.btn_addPost.setStyleSheet("""
        background-color: green;
        color: rgb(240, 240, 240);
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        """)

        self.btn_removePost.setStyleSheet("""
        background-color: red;
        color: rgb(240, 240, 240);
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        """)

        self.btn_updatePost.setStyleSheet("""
        background-color: grey;
        color: rgb(240, 240, 240);
        border-style: outset;
        border-width: 2px;
        border-radius: 10px;
        border-color: beige;
        font: bold 14px;
        min-width: 10em;
        padding: 6px;
        """)

        self.lw_posts.setStyleSheet("""
        background-color: white;
        color: black;
        border-style: outset;
        border-width: 2px;
        border-radius: 5px;
        border-color: beige;
        font: bold 14px;
        min-width: .5em;
        padding: 6px;
        QListView {
         show-decoration-selected: 1; /* make the selection span the entire width of the view */
        }
        
        QListView::item:alternate {
            background: #EEEEEE;
        }
        
        QListView::item:selected {
            border: 1px solid #6a6ea9;
        }
        
        QListView::item:selected:!active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #ABAFE5, stop: 1 #8588B2);
        }
        
        QListView::item:selected:active {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #6a6ea9, stop: 1 #888dd9);
        }
        
        QListView::item:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                        stop: 0 #FAFBFE, stop: 1 #DCDEF1);
        }
        """)
