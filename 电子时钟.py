#修改窗口LOGO
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget,QLCDNumber,QApplication,QVBoxLayout
import sys
import time
#创建自定义时钟类 继承窗口接口
class MyTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()
    #规定槽函数 更新时间
    def update_time(self):
        #获取本地时间 显示到窗口
        self.lcd.display(time.strftime('%X',time.localtime()))
    #实现定时器  信号 和槽函数
    def init_timer(self):
        #初始化定时器
        self.timer = QTimer()
        #设置触发信号，1000毫秒
        self.timer.setInterval(1000)
        #启动定时器
        self.timer.start()
        #信号触发
        self.timer.timeout.connect(self.update_time)
    #实现界面所有编写  实例方法 this
    def initUI(self):
        #设置组件大小 宽高251px * 150px
        self.resize(251,150)
        #设置窗口标题
        self.setWindowTitle('构建创意时钟')
        #设置窗口LOGO
        self.setWindowIcon(QIcon('C:/Users/19845/Desktop/a.jpg'))
        #初始化 调色板
        self.plt = QPalette()
        #设置背景颜色 深青色
        self.plt.setColor(QPalette.Background,Qt.darkCyan)
        #设置当前窗体自动填充渲染背景颜色
        self.setAutoFillBackground(True)
        #设置顶层布局
        self.setPalette(self.plt)
        #初始化 LCD数字组件
        self.lcd = QLCDNumber()
        #设置显示数字个数
        self.lcd.setDigitCount(10)
        #设置显示样式的模式，为平面模式
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        #设置显示模式，为10进制
        self.lcd.setMode(QLCDNumber.Dec)
        #获取本地时间，显示到窗口中
        self.lcd.display(time.strftime('%X',time.localtime()))
        #初始化盒子布局
        self.box = QVBoxLayout()
        #把要显示的LCD界面添加到布局中 统一管理
        self.box.addWidget(self.lcd)
        #设置组件到窗口中间位置显示
        self.box.setAlignment(Qt.AlignCenter)
        #将所有逻辑设置到顶层布局中
        self.setLayout(self.box)
        #显示所有ui界面
        self.show()
#程序入口
if  __name__ == '__main__':
    #创建应用对象
    app = QApplication(sys.argv)
    my_time = MyTime()
    #退出
    sys.exit(app.exec_())