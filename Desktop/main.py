from PySide6 import QtWidgets

from Desktop.interfaces.auth_app import AuthApp

Gapp = QtWidgets.QApplication([])
win = AuthApp()
win.show()
Gapp.exec()
