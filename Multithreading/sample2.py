#197
 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import requests

class WorkerSignals(QObject):

    data = pyqtSignal(tuple)

class Worker(QRunnable):
    def __init__(self, id, url):
        super(Worker, self).__init__()
        self.id = id
        self.url = url
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        r = requests.get(self.url)
        for line in r.text.splitlines():
            self.signals.data.emit((self.id, line))

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.urls = [
        'http://www.example.com',
        'https://www.mfitzp.com',
        'https://www.google.com',
        'https://www.udemy.com/create-simple-gui-applications-with-python-a\
        nd-qt/',
        'https://books.mfitzp.com/create-simple-gui-applications/'
        ]
        layout = QVBoxLayout()
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)
        button = QPushButton("GO GET EM!")
        button.pressed.connect(self.execute)
        layout.addWidget(self.text)
        layout.addWidget(button)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        self.show()
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    def execute(self):
        for n, url in enumerate(self.urls):
            worker = Worker(n, url)
            worker.signals.data.connect(self.display_output)
        # Execute
            self.threadpool.start(worker)
    def display_output(self, data):
        id, s = data
        self.text.appendPlainText("WORKER %d: %s" % (id, s))

app = QApplication([])
window = MainWindow()
app.exec_()