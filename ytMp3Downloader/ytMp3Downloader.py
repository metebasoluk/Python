import sys
from pytube import YouTube
import os
from PyQt5 import QtWidgets,QtGui,QtCore
from bs4 import BeautifulSoup

app=QtWidgets.QApplication(sys.argv)
win=QtWidgets.QWidget()

win.setWindowTitle("Youtube Mp3 Downloader")
win.setWindowIcon(QtGui.QIcon("ytLogo.ico"))
win.setGeometry(600,200,800,512)
win.setMaximumSize(800,512)
win.setMinimumSize(800,512)

logo=QtWidgets.QLabel(win)
logo.setPixmap(QtGui.QPixmap("logo.png"))
logo.setGeometry(19,0,762,180)


input_link=QtWidgets.QLineEdit(win)
input_link.setPlaceholderText("Youtube Linkini Yapıştırın.")
input_link.move(50,250)
input_link.setFixedSize(350,40)

download_button=QtWidgets.QPushButton(win)
download_button.setText("İndir")
download_button.move(400,250)
download_button.setFixedHeight(40)

directory_button=QtWidgets.QPushButton(win)
directory_button.setText("Dosya Konumunu Seç")
directory_button.move(50,300)
directory_button.setFixedSize(155,40)


directory_label=QtWidgets.QLabel(win)
directory_label.move(210,300)
directory_label.setFixedSize(590,40)

mp3_name_label=QtWidgets.QLabel(win)
mp3_name_label.move(0,360)
mp3_name_label.setFixedSize(800,30)
mp3_name_label.setAlignment(QtCore.Qt.AlignCenter)

info_label=QtWidgets.QLabel(win)
info_label.move(0,390)
info_label.setFixedSize(800,30)
info_label.setAlignment(QtCore.Qt.AlignCenter)


def sender():
    sender=win.sender().text()
    if sender=="Dosya Konumunu Seç":
        filepath = QtWidgets.QFileDialog.getExistingDirectory(win, 'Bir Dizin Seç')
        filepath.replace("\\","/")
        directory_label.setText(f'<font color="green" size="5">{filepath}</font>')
    elif sender=="İndir":
        link=input_link.text()
        try:
            yt=YouTube(link)
            mp3=yt.streams.filter(only_audio=True).first()
            output = mp3.download(BeautifulSoup(directory_label.text(), "html.parser").text)
            base, ext = os.path.splitext(output)
            to_mp3 = base + ".mp3"
            os.rename(output, to_mp3)
            video_name=base.split("\\")
            mp3_name_label.setText(f'<font color="orange" size="5">{video_name[1]}</font>')
            info_label.setText('<font color="green" size="5">İndirme İşlemi Başarılı</font>')
        except:
            mp3_name_label.setText(f'<font color="orange" size="5"></font>')
            info_label.setText('<font color="red" size="5">BAŞARISIZ</font>')

download_button.clicked.connect(sender)
directory_button.clicked.connect(sender)

win.show()
sys.exit(app.exec_())