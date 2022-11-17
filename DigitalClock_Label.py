from PySide6.QtWidgets import *  #QWidget
from PySide6.QtCore import * #Qttimer
from PySide6.QtGui import * #QApplication
import datetime
import sys

class Mainwindow(QWidget):
    def __init__(self):
        
        super().__init__()
        self.setGeometry(400,180, 570, 405)
        self.setWindowTitle("Digital Clock in label") #Title
        self.setStyleSheet('background-color: #444444;') #いい感じの黒色にする
        self.digitalClock()
        
    def digitalClock(self):
        
        self.label = QLabel("QLCDNumber デジタル時計", self)#ラベル作成
        self.label.setGeometry(183, 40, 200, 57) 
        self.label.setStyleSheet('color:white;')#白色
        
        now_time = self.nowTime()#変数内に時間を格納 # #現在時刻
        self.label = QLabel(now_time, self)#ラベル作成
        self.label.setGeometry(180, 150, 200, 57)
        self.label.setStyleSheet('color:white;')

        self.timer = QTimer(self) #timerをセット
        self.timer.timeout.connect(self.Change_Time) #時間終了後にChange_Time関数を実行
        self.timer.start(1000) #1000 -> 1

    def Change_Time(self):
        now_time = self.nowTime()
        print(now_time)
        self.label.move(180, 150)
        self.label.setText(now_time) #書き換え
    
    def nowTime(self):
        dt = datetime.datetime.now()
        #now_time = dt.strftime('%Y年%m月%d日 %H:%M:%S') <- こちらもあり
        now_time ="""{0}年{1}月{2}日{3}時{4}分{5}秒""" .format(str(dt.year),str(dt.month),str(dt.day),str(dt.hour),str(dt.minute),str(dt.second))
        return now_time

def main():
    app = QApplication(sys.argv)
    main = Mainwindow()
    main.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()