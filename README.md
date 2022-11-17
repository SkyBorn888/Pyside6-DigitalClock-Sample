# Pyside6-DigitalClock-Sample

Ahh, fix the design yourself... :3
デザインは自分で修正してくれ... :3

#### There is two samples of Digital Clock
EN :7-segment display digital clock usring QLCDNumber <- official reference recommended
JP :7セグメントディスプレイ表示デジタル時計 <- 公式リファレンス推奨
```
DigitalClock_QLCDNumber.py
```
![Screenshot 2022-11-15 at 0.23.34.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1212967/7f4f47e1-b88c-6221-5a1e-8320da568615.png)

EN :Digital clock using label widget <- Recommended by contributor
JP :ラベルを使ったデジタル時計 <- 投稿主推奨
```
DigitalClock_Label.py
```
![Screenshot 2022-11-15 at 0.44.48.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/1212967/cfd30769-d24a-ce57-a60f-f9991ec87e95.png)

### Development environment
Python==3.8.9
PySide6==6.4.0.1
PySide6-Addons==6.4.0.1
PySide6-Essentials==6.4.0

macOS ventura CPU Intel
Winodws 11 CPUs Intel



### 公式リファレンス推奨の7セグメントディスプレイ表示デジタル時計
[公式リファレンス](https://doc.qt.io/qtforpython/overviews/qtwidgets-widgets-digitalclock-example.html)を元に
QLCDNumberを呼び出して作成する方法になります。

QLCDNumberウィジェットは7セグメントLCDに映し出されるような数字を表示するウィジェットになります。見た目が良く、数字が見やすいUIを用意することができます。

ネットに上がっているサンプルコードはほとんどデジタル時計の単体として使っているところが多く見られています。しかし開発者によっては、時計と一緒に他のウィジェットをくっつけたかったり、インプットした数字を表示するためだけに使いたいと思われます。
今回のお題はデジタル時計なので前者の時計と一緒に他のウィジェットをくっつけるコードを記述します。

また今回、記述したコードはQwidegetで作成したウィンドウの中にQLCDNumberウィジェット作成して汎用性を高くする様に作成しました。






再び言いますがQLCDnumberは数字を表示する際に7セグメントLCDな数字を表示するためにあります。

なので、時計の機能部分の実装はタイマーを設定して1秒ごとにパネルのテキストを書き換えるというコードが必要になります。

これは、次の「ラベルで作成したデジタル時計」も同じ内容です。

では、なぜラベルでデジタル時計を作成する必要があるのでしょうか


### ラベルで作成したデジタル時計
###### ラベルで作成する意味とは?
QLCDnumberで作った時計だと、
###### 7セグメントディスプレイ表示
に限られてしまいます。
こいう場合は、ラベルに取り替えると汎用性が高くなります。

### 最後に
結局どっちを使うかは、使用者の勝手になるでしょう。
個人的には、ラベルで作成する方が汎用性が高いと思います。
しかし、QLCDnumberは見た目がカッコよく
普通に時計として作成するなら断然こちらを選びますね。


### 参考文献
[Qt for Python - Qt Documentation](https://doc.qt.io/qtforpython/)

