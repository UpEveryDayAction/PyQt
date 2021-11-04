from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
import sys
import plotly.express as px
import pandas as pd

class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QtWidgets.QPushButton('Plot', self)
        self.browser = QtWebEngineWidgets.QWebEngineView(self)

        vlayout = QtWidgets.QVBoxLayout(self)
        vlayout.addWidget(self.button, alignment=QtCore.Qt.AlignHCenter)
        vlayout.addWidget(self.browser)
        # 機能を止めるときにボタンを押すと、フィードバックが出る感じ
        self.button.clicked.connect(self.show_graph)
        self.resize(800,600)

    def show_graph(self):
        # df = px.data.tips()
        df = pd.DataFrame({
            'time':[0, 0.5, 1.7, 3.3, 4.5, 6.1],
            'detect_count':[1,1,1,1,1,1],
            'direct':['right','left','right','left','right','right']
        })
        # fig = px.box(df, x="day", y="total_bill", color="smoker")
        fig = px.pie(df, values='detect_count', names='direct')
        # fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        self.browser.setHtml(fig.to_html(include_plotlyjs='cdn'))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())