import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(450,150,480,700)
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self): #レイアウトに追加するウィジェットを作成する　
        ###############progress bar
        self.progressBar=QProgressBar() 
        ###############buttons
        self.addButton = QToolButton()
        self.addButton.setIcon(QIcon("icons/add.png")) #tip ターミナルのディレクトリ
        self.addButton.setIconSize(QSize(48,48))
        self.addButton.setToolTip("Add a Song")
        self.addButton.clicked.connect(self.addSound)


        self.shuffleButton=QToolButton()
        self.shuffleButton.setIcon(QIcon("icons/shuffle.png"))
        self.shuffleButton.setIconSize(QSize(48,48))
        self.shuffleButton.setToolTip("Shuffle The list")
        self.shuffleButton.clicked.connect(self.shufflePlayList)


        self.previousButton=QToolButton()
        self.previousButton.setIcon(QIcon("icons/previous.png"))
        self.previousButton.setIconSize(QSize(48,48))
        self.previousButton.setToolTip("Play Previous")

        self.playButton=QToolButton()
        self.playButton.setIcon(QIcon("icons/play.png"))
        self.playButton.setIconSize(QSize(64,64))
        self.playButton.setToolTip("Play")

        self.nextButton=QToolButton()
        self.nextButton.setIcon(QIcon("icons/next.png"))
        self.nextButton.setIconSize(QSize(48,48))
        self.nextButton.setToolTip("Play Next")

        self.muteButton=QToolButton()
        self.muteButton.setIcon(QIcon("icons/mute.png"))
        self.muteButton.setIconSize(QSize(24,24))
        self.muteButton.setToolTip("Mute")

        ###########################vlume Slider
        self.volumeSlider=QSlider(Qt.Horizontal)
        self.volumeSlider.setToolTip("Volume")

        ############################Play List
        self.playList=QListWidget()





    def layouts(self):
        ############Creating Layouts
        self.mainLayout=QVBoxLayout()
        self.topMainLayout=QVBoxLayout()
        self.topGroupBox=QGroupBox("Music Player",self)
        self.topGroupBox.setStyleSheet("background-color:#fcc324")
        self.topLayout=QHBoxLayout()
        self.middleLayout=QHBoxLayout()
        self.buttonLayout=QVBoxLayout()

        ##############Adding Widgets
        ##############Top layout widgets
        self.topLayout.addWidget(self.progressBar) #point レイアウトにウィジェットを追加


        ##############Middle layout widgets
        self.middleLayout.addStretch() #右による
        self.middleLayout.addWidget(self.addButton)
        self.middleLayout.addWidget(self.shuffleButton)
        self.middleLayout.addWidget(self.playButton)
        self.middleLayout.addWidget(self.previousButton)
        self.middleLayout.addWidget(self.nextButton)
        self.middleLayout.addWidget(self.volumeSlider)
        self.middleLayout.addWidget(self.muteButton)
        self.middleLayout.addStretch() #左による

        #################Bottom layout widgets
        self.buttonLayout.addWidget(self.playList)
        
        self.topMainLayout.addLayout(self.topLayout)
        self.topMainLayout.addLayout(self.middleLayout)
        #topGroupBoxにレイアウトを適用する
        self.topGroupBox.setLayout(self.topMainLayout)
        self.mainLayout.addWidget(self.topGroupBox,25) # point 画面のアスペクト比を制御。VerticalなLayoutなので縦の比を決める
        self.mainLayout.addLayout(self.buttonLayout,75)
        self.setLayout(self.mainLayout)

    def addSound(self):
        directory=QFileDialog.getOpenFileName(self,"Add Sound","","Sound Files (*.mp3 *.ogg *.wav)")
        print(directory)
        #オーディオファイルはyoutubeフリー素材より
        #https://studio.youtube.com/
        filename=os.path.basename(directory[0])
        print(filename)
        self.playList.addItem(filename)
        # musicList.append(directory[0])

    def shufflePlayList(self):
        # random.shuffle
        pass
        
def main():
    #モジュールの名前を引数にQpplicationのインスタンスを作成
    App=QApplication(sys.argv) 
    window=Player()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()