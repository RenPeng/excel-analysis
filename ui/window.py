# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/renpeng/code/project_analysis/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 890)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setToolTip("")
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(179, 215, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.line_7 = QtWidgets.QFrame(self.frame_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_9.addWidget(self.line_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.step1ConfigFileChooseBT = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1ConfigFileChooseBT.sizePolicy().hasHeightForWidth())
        self.step1ConfigFileChooseBT.setSizePolicy(sizePolicy)
        self.step1ConfigFileChooseBT.setObjectName("step1ConfigFileChooseBT")
        self.horizontalLayout_12.addWidget(self.step1ConfigFileChooseBT)
        self.step1ConfigFileChooseRV = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1ConfigFileChooseRV.sizePolicy().hasHeightForWidth())
        self.step1ConfigFileChooseRV.setSizePolicy(sizePolicy)
        self.step1ConfigFileChooseRV.setObjectName("step1ConfigFileChooseRV")
        self.horizontalLayout_12.addWidget(self.step1ConfigFileChooseRV)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.line_11 = QtWidgets.QFrame(self.frame_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_5.addWidget(self.line_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_11.addWidget(self.comboBox_3)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_3.setMouseTracking(False)
        self.toolButton_3.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.toolButton_3.setToolTip("")
        self.toolButton_3.setToolTipDuration(2)
        self.toolButton_3.setStatusTip("")
        self.toolButton_3.setWhatsThis("")
        self.toolButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon/setting-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_11.addWidget(self.toolButton_3)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.toolButton = QtWidgets.QToolButton(self.frame_3)
        self.toolButton.setMouseTracking(False)
        self.toolButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.toolButton.setToolTip("")
        self.toolButton.setToolTipDuration(2)
        self.toolButton.setStatusTip("")
        self.toolButton.setWhatsThis("")
        self.toolButton.setText("")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_4.addWidget(self.toolButton)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_2.setMouseTracking(False)
        self.toolButton_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.toolButton_2.setToolTip("")
        self.toolButton_2.setToolTipDuration(2)
        self.toolButton_2.setStatusTip("")
        self.toolButton_2.setWhatsThis("")
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_5.addWidget(self.toolButton_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: rgb(179, 215, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.label_3)
        self.line_8 = QtWidgets.QFrame(self.frame_4)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_10.addWidget(self.line_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.step1SourceFileChooseBT = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1SourceFileChooseBT.sizePolicy().hasHeightForWidth())
        self.step1SourceFileChooseBT.setSizePolicy(sizePolicy)
        self.step1SourceFileChooseBT.setObjectName("step1SourceFileChooseBT")
        self.horizontalLayout_14.addWidget(self.step1SourceFileChooseBT)
        self.step1SourceFileChooseRV = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1SourceFileChooseRV.sizePolicy().hasHeightForWidth())
        self.step1SourceFileChooseRV.setSizePolicy(sizePolicy)
        self.step1SourceFileChooseRV.setObjectName("step1SourceFileChooseRV")
        self.horizontalLayout_14.addWidget(self.step1SourceFileChooseRV)
        self.step1SourceDataSheetSelect = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1SourceDataSheetSelect.sizePolicy().hasHeightForWidth())
        self.step1SourceDataSheetSelect.setSizePolicy(sizePolicy)
        self.step1SourceDataSheetSelect.setObjectName("step1SourceDataSheetSelect")
        self.step1SourceDataSheetSelect.addItem("")
        self.horizontalLayout_14.addWidget(self.step1SourceDataSheetSelect)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.line_10 = QtWidgets.QFrame(self.frame_4)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_10.addWidget(self.line_10)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.step1ProcessBT = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1ProcessBT.sizePolicy().hasHeightForWidth())
        self.step1ProcessBT.setSizePolicy(sizePolicy)
        self.step1ProcessBT.setObjectName("step1ProcessBT")
        self.horizontalLayout_16.addWidget(self.step1ProcessBT)
        self.line_9 = QtWidgets.QFrame(self.frame_4)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_16.addWidget(self.line_9)
        self.step1ExportBT = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step1ExportBT.sizePolicy().hasHeightForWidth())
        self.step1ExportBT.setSizePolicy(sizePolicy)
        self.step1ExportBT.setObjectName("step1ExportBT")
        self.horizontalLayout_16.addWidget(self.step1ExportBT)
        self.line_6 = QtWidgets.QFrame(self.frame_4)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_16.addWidget(self.line_6)
        self.progressBar = QtWidgets.QProgressBar(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_16.addWidget(self.progressBar)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.line_2 = QtWidgets.QFrame(self.frame_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_10.addWidget(self.line_2)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        self.processTitle = QtWidgets.QLabel(self.frame_4)
        self.processTitle.setObjectName("processTitle")
        self.horizontalLayout_15.addWidget(self.processTitle)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.tab1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_7.addWidget(self.textBrowser)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(179, 215, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Alibaba PuHuiTi")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sourceFileChooseBT = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceFileChooseBT.sizePolicy().hasHeightForWidth())
        self.sourceFileChooseBT.setSizePolicy(sizePolicy)
        self.sourceFileChooseBT.setObjectName("sourceFileChooseBT")
        self.horizontalLayout_7.addWidget(self.sourceFileChooseBT)
        self.sourceFileChooseReView = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceFileChooseReView.sizePolicy().hasHeightForWidth())
        self.sourceFileChooseReView.setSizePolicy(sizePolicy)
        self.sourceFileChooseReView.setObjectName("sourceFileChooseReView")
        self.horizontalLayout_7.addWidget(self.sourceFileChooseReView)
        self.sourceWS = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceWS.sizePolicy().hasHeightForWidth())
        self.sourceWS.setSizePolicy(sizePolicy)
        self.sourceWS.setObjectName("sourceWS")
        self.sourceWS.addItem("")
        self.horizontalLayout_7.addWidget(self.sourceWS)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(179, 215, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame_2)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_2.addWidget(self.openGLWidget)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Alibaba PuHuiTi")
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.line_3 = QtWidgets.QFrame(self.frame_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.thirdFileChooseBT = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdFileChooseBT.sizePolicy().hasHeightForWidth())
        self.thirdFileChooseBT.setSizePolicy(sizePolicy)
        self.thirdFileChooseBT.setObjectName("thirdFileChooseBT")
        self.horizontalLayout_8.addWidget(self.thirdFileChooseBT)
        self.thirdFileChooseReView = QtWidgets.QLabel(self.frame_2)
        self.thirdFileChooseReView.setObjectName("thirdFileChooseReView")
        self.horizontalLayout_8.addWidget(self.thirdFileChooseReView)
        self.thirdWS = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdWS.sizePolicy().hasHeightForWidth())
        self.thirdWS.setSizePolicy(sizePolicy)
        self.thirdWS.setObjectName("thirdWS")
        self.thirdWS.addItem("")
        self.horizontalLayout_8.addWidget(self.thirdWS)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.thirdOrderIDColumn = QtWidgets.QComboBox(self.frame_2)
        self.thirdOrderIDColumn.setObjectName("thirdOrderIDColumn")
        self.thirdOrderIDColumn.addItem("")
        self.horizontalLayout_2.addWidget(self.thirdOrderIDColumn)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.thirdOrderAmountColumn = QtWidgets.QComboBox(self.frame_2)
        self.thirdOrderAmountColumn.setObjectName("thirdOrderAmountColumn")
        self.thirdOrderAmountColumn.addItem("")
        self.horizontalLayout_2.addWidget(self.thirdOrderAmountColumn)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.thirdName = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdName.sizePolicy().hasHeightForWidth())
        self.thirdName.setSizePolicy(sizePolicy)
        self.thirdName.setText("")
        self.thirdName.setObjectName("thirdName")
        self.horizontalLayout_2.addWidget(self.thirdName)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.thirdInfoAddBT = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdInfoAddBT.sizePolicy().hasHeightForWidth())
        self.thirdInfoAddBT.setSizePolicy(sizePolicy)
        self.thirdInfoAddBT.setObjectName("thirdInfoAddBT")
        self.horizontalLayout_9.addWidget(self.thirdInfoAddBT)
        self.thirdInfoEmptyBT = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdInfoEmptyBT.sizePolicy().hasHeightForWidth())
        self.thirdInfoEmptyBT.setSizePolicy(sizePolicy)
        self.thirdInfoEmptyBT.setObjectName("thirdInfoEmptyBT")
        self.horizontalLayout_9.addWidget(self.thirdInfoEmptyBT)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.thirdInfoListReview = QtWidgets.QTextEdit(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thirdInfoListReview.sizePolicy().hasHeightForWidth())
        self.thirdInfoListReview.setSizePolicy(sizePolicy)
        self.thirdInfoListReview.setObjectName("thirdInfoListReview")
        self.verticalLayout_3.addWidget(self.thirdInfoListReview)
        self.analysisErrorMsg = QtWidgets.QTextEdit(self.tab2)
        self.analysisErrorMsg.setObjectName("analysisErrorMsg")
        self.verticalLayout_3.addWidget(self.analysisErrorMsg)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.beginAnalysisBT = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beginAnalysisBT.sizePolicy().hasHeightForWidth())
        self.beginAnalysisBT.setSizePolicy(sizePolicy)
        self.beginAnalysisBT.setObjectName("beginAnalysisBT")
        self.horizontalLayout.addWidget(self.beginAnalysisBT)
        self.exportResultBT = QtWidgets.QPushButton(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportResultBT.sizePolicy().hasHeightForWidth())
        self.exportResultBT.setSizePolicy(sizePolicy)
        self.exportResultBT.setObjectName("exportResultBT")
        self.horizontalLayout.addWidget(self.exportResultBT)
        self.analysisProgressBar = QtWidgets.QProgressBar(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisProgressBar.sizePolicy().hasHeightForWidth())
        self.analysisProgressBar.setSizePolicy(sizePolicy)
        self.analysisProgressBar.setProperty("value", 24)
        self.analysisProgressBar.setObjectName("analysisProgressBar")
        self.horizontalLayout.addWidget(self.analysisProgressBar)
        self.analysisProcessTitle = QtWidgets.QLabel(self.tab2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisProcessTitle.sizePolicy().hasHeightForWidth())
        self.analysisProcessTitle.setSizePolicy(sizePolicy)
        self.analysisProcessTitle.setObjectName("analysisProcessTitle")
        self.horizontalLayout.addWidget(self.analysisProcessTitle)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setCheckable(True)
        self.actionnew.setObjectName("actionnew")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "对账分析工具"))
        self.label_2.setText(_translate("MainWindow", "✅配件信息配置"))
        self.step1ConfigFileChooseBT.setText(_translate("MainWindow", "选择文件"))
        self.step1ConfigFileChooseRV.setText(_translate("MainWindow", "【选择配置文件】"))
        self.label_18.setText(_translate("MainWindow", "渠道活动："))
        self.label_8.setText(_translate("MainWindow", "配件价格："))
        self.label_16.setText(_translate("MainWindow", "渠道折扣"))
        self.label_3.setText(_translate("MainWindow", "✅源Excel表格"))
        self.step1SourceFileChooseBT.setText(_translate("MainWindow", "选择文件"))
        self.step1SourceFileChooseRV.setText(_translate("MainWindow", "【选择源文件】"))
        self.step1SourceDataSheetSelect.setItemText(0, _translate("MainWindow", "选择月份数据"))
        self.step1ProcessBT.setText(_translate("MainWindow", "处理"))
        self.step1ExportBT.setText(_translate("MainWindow", "导出结果"))
        self.label_12.setText(_translate("MainWindow", "  进度信息："))
        self.processTitle.setText(_translate("MainWindow", "..."))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">新增需求：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.  捧味道，2款产品7折结算，其它按照8折结算。</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.  追加备注中包含渠道信息（未录入到配件价格表中的）。</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "公司数据Excel处理工具"))
        self.label.setText(_translate("MainWindow", "✅公司配置"))
        self.sourceFileChooseBT.setText(_translate("MainWindow", "选择文件"))
        self.sourceFileChooseReView.setText(_translate("MainWindow", "【选择源文件】"))
        self.sourceWS.setItemText(0, _translate("MainWindow", "选择WorkSheet"))
        self.label_7.setText(_translate("MainWindow", "✅渠道方数据配置"))
        self.thirdFileChooseBT.setText(_translate("MainWindow", "选择文件"))
        self.thirdFileChooseReView.setText(_translate("MainWindow", "【选择源文件】"))
        self.thirdWS.setItemText(0, _translate("MainWindow", "选择WorkSheet"))
        self.label_9.setText(_translate("MainWindow", "订单号标题："))
        self.thirdOrderIDColumn.setItemText(0, _translate("MainWindow", "请选择列信息"))
        self.label_11.setText(_translate("MainWindow", "订单总价标题："))
        self.thirdOrderAmountColumn.setItemText(0, _translate("MainWindow", "请选择列信息"))
        self.label_4.setText(_translate("MainWindow", "渠道名称："))
        self.thirdInfoAddBT.setText(_translate("MainWindow", "添加到分析队列"))
        self.thirdInfoEmptyBT.setText(_translate("MainWindow", "清空所有渠道信息"))
        self.beginAnalysisBT.setText(_translate("MainWindow", "开始分析"))
        self.exportResultBT.setText(_translate("MainWindow", "导出分析结果"))
        self.analysisProcessTitle.setText(_translate("MainWindow", "...."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "渠道数据分析"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionnew.setToolTip(_translate("MainWindow", "<html><head/><body><p>asdf</p></body></html>"))
