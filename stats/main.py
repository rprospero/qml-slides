from PySide2.QtQuick import QQuickView
import model
from PySide2.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
view = QQuickView()
view.setSource("view.qml")
view.show()
app.exec_()
