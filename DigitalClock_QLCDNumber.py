from PySide6.QtWidgets import *  #QWidget
from PySide6.QtCore import * #Qttimer
from PySide6.QtGui import * #QApplication QLCDNumber
import datetime
import sys
import math


class Mainwindow(QWidget):
    #__init__ parent=None 継承元QWidgetの環境変数を呼び出す
    def __init__(self):
        #super()で登録されている環境変数の値を振り込む
        super().__init__()
        self.setGeometry(270,230, 850, 405) #winodw位置、サイズを指定
        self.setWindowTitle("QLCDNumber ウィジェット") #title
        self.setStyleSheet('background-color: #444444;') #背景をいい感じの黒にします
        self.home() #home関数を実行する

    def home(self): #home関数を作成ここにデジタル時計を作る
        
        self.label = QLabel("QLCDNumber デジタル時計", self)#ラベル作成
        self.label.setGeometry(340, 40, 200, 57) 
        self.label.setStyleSheet('color:white;')#白色
        
        
        now_time = self.nowTime() #現在時刻 <- 環境変数にしない
        self.digital_clock = QLCDNumber(self) #QLCNumberクラスでdigital_clockというインスタンス変数を作成 selfを引数をつけることでQWidgetを継承した環境変数の元にウィジェット作成することになる
        self.digital_clock.setGeometry(180, 150, 500, 50)  #winodwの中での位置、サイズを指定
        self.digital_clock.setDigitCount(19)
        self.digital_clock.display(now_time) 
        
        self.timer = QTimer(self) #timerをセット
        self.timer.timeout.connect(self.Change_Time) #時間終了後にChange_Time関数を実行
        self.timer.start(1000) #1000 -> 1秒
        
    def Change_Time(self):
        now_time = self.nowTime() #現在時刻 
        self.digital_clock.move(180, 150)         
        self.digital_clock.display(now_time) #書き換え
    
    #現在時刻を引き出す関数
    def nowTime(self):
        now = datetime.datetime.now()
        now_time = now.strftime('%Y-%m-%d %H:%M:%S')
        print(now_time)
        #return now_time
        return now_time
        
#Mainwindowクラスを実行する
def main():
    app = QApplication(sys.argv)
    main = Mainwindow()
    main.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()