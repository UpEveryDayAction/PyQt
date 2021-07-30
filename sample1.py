import sys
import PyQt5.QtWidgets
 
app = PyQt5.QtWidgets.QApplication([])
w = PyQt5.QtWidgets.QWidget()
w.resize(300, 200)
w.setWindowTitle('foo')
w.show()
sys.exit(app.exec())
