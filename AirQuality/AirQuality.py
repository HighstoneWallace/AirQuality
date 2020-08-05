 
import sys
from TemperatureSensor import AirChecker
from PyQt5 import QtWidgets, QtCore, QtGui
from pyqtgraph import PlotWidget, plot


MAIN_WINDOW_SIZE = [800, 480]

FRAME_LEFT_GEOMETRY = [0, 0, 200, 480]
FRAME_MIDDLE_GEOMETRY = [250, 0, 350, 480]
FRAME_RIGHT_GEOMETRY = [600, 0, 200, 480]

class GuiWindow():

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QWidget()
        self.MainWindow.setObjectName("AirQuality")
        self.MainWindow.resize(MAIN_WINDOW_SIZE[0], MAIN_WINDOW_SIZE[1])

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        

        self.frame_left = self.create_frame(FRAME_LEFT_GEOMETRY)
        self.frame_middle = self.create_frame(FRAME_MIDDLE_GEOMETRY)
        self.frame_right = self.create_frame(FRAME_RIGHT_GEOMETRY)





    def create_frame(self, geometry):
        frame = QtWidgets.QFrame(self.centralwidget)
        frame.setGeometry(QtCore.QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        return frame

    def create_label(self, geometry):
        pass



if __name__=="__main__":

    AirQuality = AirChecker()
    MyGui = GuiWindow()
    MyGui.MainWindow.show() 
    MyGui.app.exec_()

    from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        self.label = QtWidgets.QLabel(self.frame_left)
        self.label.setGeometry(QtCore.QRect(10, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")



        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2") 
        

        
        
        
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(10, 70, 211, 91))
        self.lcdNumber_3.setObjectName("lcdNumber_3")

        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(10, 230, 211, 91))
        self.lcdNumber_4.setObjectName("lcdNumber_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Humidity"))
        self.label_2.setText(_translate("MainWindow", "Temperature"))