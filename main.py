# File: main.py
import sys
import os

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = os.path.join(os.path.dirname(__file__), "form.ui")
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec_())

## This Python file uses the following encoding: utf-8
#import sys
#import os


#from PySide2.QtWidgets import QApplication, QMainWindow
#from PySide2.QtCore import QFile
#from PySide2.QtUiTools import QUiLoader


#class MainWindow(QMainWindow):
#    def __init__(self):
#        super(MainWindow, self).__init__()
#        self.load_ui()

#    def load_ui(self):
#        loader = QUiLoader()
#        path = os.path.join(os.path.dirname(__file__), "form.ui")
#        ui_file = QFile(path)
#        ui_file.open(QFile.ReadOnly)
#        loader.load(ui_file, self)
#        ui_file.close()

#if __name__ == "__main__":
#    app = QApplication([])
#    widget = MainWindow()
#    widget.show()
#    sys.exit(app.exec_())
