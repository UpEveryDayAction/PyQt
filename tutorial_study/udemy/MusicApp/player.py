import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt
import random
from pygame import mixer
import time

#########global
musicList=[]
mixer.init() #グローバルにするためにここでinit
muted=False

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
        self.previousButton.setIconSize(QSize(48,48)) # アイコンの大きさを変更
        self.previousButton.setToolTip("Play Previous")

        self.playButton=QToolButton()
        self.playButton.setIcon(QIcon("icons/play.png"))
        self.playButton.setIconSize(QSize(64,64))
        self.playButton.setToolTip("Play")
        self.playButton.clicked.connect(self.playSounds)

        self.nextButton=QToolButton()
        self.nextButton.setIcon(QIcon("icons/next.png"))
        self.nextButton.setIconSize(QSize(48,48))
        self.nextButton.setToolTip("Play Next")

        self.muteButton=QToolButton()
        self.muteButton.setIcon(QIcon("icons/mute.png"))
        self.muteButton.setIconSize(QSize(24,24))
        self.muteButton.setToolTip("Mute") #
        self.muteButton.clicked.connect(self.muteSound)

        ###########################vlume Slider
        self.volumeSlider=QSlider(Qt.Horizontal)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.setValue(70)
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        mixer.music.set_volume(0.7)
        self.volumeSlider.valueChanged.connect(self.setVolume)

        ############################Play List
        self.playList=QListWidget()
        self.playList.doubleClicked.connect(self.playSounds)



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
        ######open music file
        directory=QFileDialog.getOpenFileName(self,"Add Sound","","Sound Files (*.mp3 *.ogg *.wav)")
        print(directory)
        #オーディオファイルはyoutubeフリー素材より
        #https://studio.youtube.com/
        filename=os.path.basename(directory[0])
        print(filename)
        self.playList.addItem(filename) # L61あたりで作成したQListWidget
        # musicList.append(directory[0])
        musicList.append(directory[0]) # グローバルリストに追加

    def shufflePlayList(self):
        # random.shuffle
        random.shuffle(musicList)
        print(musicList)
        self.playList.clear()
        for song in musicList:
            fname=os.path.basename(song)
            self.playList.addItem(fname)
    
    def playSounds(self):
        index=self.playList.currentRow()
        print(index)
        print(musicList[index])

        try:
            mixer.music.load(musicList[index])
            mixer.music.play()
            time.sleep(5)
            # mixer.music.pause()
            # time.sleep(5)
            # mixer.music.unpause()
            # 一時停止とそこからの再生をテスト
            #http://westplain.sakuraweb.com/translate/pygame/Music.cgi
        except:
            pass

    def setVolume(self):
        self.volume=self.volumeSlider.value()
        # print(self.volume)
        mixer.music.set_volume(self.volume/100)
        
    def muteSound(self):
        global muted
        if muted == False:
            mixer.music.set_volume(0.0)
            muted = True
            self.muteButton.setIcon(QIcon('icons/unmute.png'))
            self.muteButton.setToolTip("UnMute")
            self.volumeSlider.setValue(0)

def main():
    #モジュールの名前を引数にQpplicationのインスタンスを作成
    App=QApplication(sys.argv) 
    window=Player()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()