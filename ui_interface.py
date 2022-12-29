# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(955, 732)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #mainBodyContent, QLineEdit{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#header, #mainBody, #footer, #chartStackedWidget, #scrollArea,\n"
"#scrollAreaWidgetContents_2\n"
"#widget_4{\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	padding: 3px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10 px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchBtn, #continueLineChartBtn,\n"
"#returnToChartParameters,\n"
"#continueRatingBtn,\n"
"#returnToRatingParameters{\n"
"	background-color: #755D90;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QToolBox{\n"
"	text-align:left;\n"
"	background-color: #27263c;\n"
"}\n"
"QToolBox::tab{\n"
"	text-align:left;\n"
"	border-radius: 5px;\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#line_3{\n"
"	border: N"
                        "one;\n"
"	color: #27263c;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.headerLeftRrm = QFrame(self.header)
        self.headerLeftRrm.setObjectName(u"headerLeftRrm")
        self.headerLeftRrm.setFrameShape(QFrame.StyledPanel)
        self.headerLeftRrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerLeftRrm)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuBtn = QPushButton(self.headerLeftRrm)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignLeft)

        self.nameLbl = QLabel(self.headerLeftRrm)
        self.nameLbl.setObjectName(u"nameLbl")
        font1 = QFont()
        font1.setPointSize(14)
        self.nameLbl.setFont(font1)

        self.horizontalLayout_3.addWidget(self.nameLbl)


        self.horizontalLayout.addWidget(self.headerLeftRrm, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy1)
        self.mainBody.setMinimumSize(QSize(955, 593))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 564))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menuFrm = QFrame(self.widget)
        self.menuFrm.setObjectName(u"menuFrm")
        sizePolicy1.setHeightForWidth(self.menuFrm.sizePolicy().hasHeightForWidth())
        self.menuFrm.setSizePolicy(sizePolicy1)
        self.menuFrm.setFont(font)
        self.menuFrm.setFrameShape(QFrame.StyledPanel)
        self.menuFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menuFrm)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.menuFrm)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy2)
        self.toolBox.setMinimumSize(QSize(0, 560))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.toolBox.setFont(font2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 200, 488))
        self.verticalLayout_12 = QVBoxLayout(self.page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_4 = QWidget(self.page)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 20)
        self.search_table_line = QLineEdit(self.widget_4)
        self.search_table_line.setObjectName(u"search_table_line")
        font3 = QFont()
        font3.setPointSize(9)
        self.search_table_line.setFont(font3)

        self.gridLayout.addWidget(self.search_table_line, 0, 0, 1, 1)

        self.clearTableSearchBtn = QPushButton(self.widget_4)
        self.clearTableSearchBtn.setObjectName(u"clearTableSearchBtn")
        self.clearTableSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/checkbox_indeterminate.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clearTableSearchBtn.setIcon(icon1)

        self.gridLayout.addWidget(self.clearTableSearchBtn, 0, 3, 1, 1)

        self.searchTableNameBtn = QPushButton(self.widget_4)
        self.searchTableNameBtn.setObjectName(u"searchTableNameBtn")
        self.searchTableNameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/checkbox_checked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchTableNameBtn.setIcon(icon2)

        self.gridLayout.addWidget(self.searchTableNameBtn, 0, 2, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page, u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 200, 488))
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.linePlotBtn = QPushButton(self.page_2)
        self.linePlotBtn.setObjectName(u"linePlotBtn")
        self.linePlotBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/activity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.linePlotBtn.setIcon(icon3)
        self.linePlotBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.linePlotBtn)

        self.ratingPlotBtn = QPushButton(self.page_2)
        self.ratingPlotBtn.setObjectName(u"ratingPlotBtn")
        self.ratingPlotBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/bar-chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ratingPlotBtn.setIcon(icon4)
        self.ratingPlotBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_13.addWidget(self.ratingPlotBtn)

        self.toolBox.addItem(self.page_2, u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.menuFrm, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.homeWdgt = QWidget(self.homePage)
        self.homeWdgt.setObjectName(u"homeWdgt")
        self.verticalLayout_9 = QVBoxLayout(self.homeWdgt)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame = QFrame(self.homeWdgt)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.homeLbl = QLabel(self.widget_2)
        self.homeLbl.setObjectName(u"homeLbl")
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.homeLbl.setFont(font4)

        self.horizontalLayout_4.addWidget(self.homeLbl)

        self.refreshBtn = QPushButton(self.widget_2)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMaximumSize(QSize(50, 50))
        self.refreshBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/refresh-ccw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshBtn.setIcon(icon5)
        self.refreshBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.refreshBtn)

        self.saveTableBtn = QPushButton(self.widget_2)
        self.saveTableBtn.setObjectName(u"saveTableBtn")
        self.saveTableBtn.setMaximumSize(QSize(50, 40))
        self.saveTableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveTableBtn.setIcon(icon6)
        self.saveTableBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.saveTableBtn)


        self.horizontalLayout_6.addWidget(self.widget_2, 0, Qt.AlignLeft)

        self.homeSearchBtn = QPushButton(self.frame)
        self.homeSearchBtn.setObjectName(u"homeSearchBtn")
        self.homeSearchBtn.setFont(font2)
        self.homeSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeSearchBtn.setIcon(icon7)
        self.homeSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.homeSearchBtn, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.homeWdgt)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.homeWdgt)

        self.mainPages.addWidget(self.homePage)
        self.chartParametersPage = QWidget()
        self.chartParametersPage.setObjectName(u"chartParametersPage")
        self.verticalLayout_11 = QVBoxLayout(self.chartParametersPage)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.chart_header = QWidget(self.chartParametersPage)
        self.chart_header.setObjectName(u"chart_header")
        self.horizontalLayout_9 = QHBoxLayout(self.chart_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 11, 0, 11)
        self.chartLbl = QLabel(self.chart_header)
        self.chartLbl.setObjectName(u"chartLbl")
        self.chartLbl.setFont(font4)

        self.horizontalLayout_9.addWidget(self.chartLbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.chart_header)

        self.chartParametersFrm = QFrame(self.chartParametersPage)
        self.chartParametersFrm.setObjectName(u"chartParametersFrm")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.chartParametersFrm.sizePolicy().hasHeightForWidth())
        self.chartParametersFrm.setSizePolicy(sizePolicy3)
        self.chartParametersFrm.setFrameShape(QFrame.StyledPanel)
        self.chartParametersFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.chartParametersFrm)
        self.verticalLayout_25.setSpacing(20)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.parameterLbl = QLabel(self.chartParametersFrm)
        self.parameterLbl.setObjectName(u"parameterLbl")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.parameterLbl.setFont(font5)

        self.verticalLayout_25.addWidget(self.parameterLbl)

        self.mainParameterWdg = QWidget(self.chartParametersFrm)
        self.mainParameterWdg.setObjectName(u"mainParameterWdg")
        self.mainParameterWdg.setMinimumSize(QSize(0, 50))
        self.gridLayout_15 = QGridLayout(self.mainParameterWdg)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 10)
        self.mainParameter = QComboBox(self.mainParameterWdg)
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.addItem("")
        self.mainParameter.setObjectName(u"mainParameter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mainParameter.sizePolicy().hasHeightForWidth())
        self.mainParameter.setSizePolicy(sizePolicy4)
        self.mainParameter.setFont(font)
        self.mainParameter.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainParameter.setInsertPolicy(QComboBox.InsertAtBottom)

        self.gridLayout_15.addWidget(self.mainParameter, 0, 0, 1, 1)

        self.mainParameterSet = QPushButton(self.mainParameterWdg)
        self.mainParameterSet.setObjectName(u"mainParameterSet")
        self.mainParameterSet.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/check-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainParameterSet.setIcon(icon8)
        self.mainParameterSet.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.mainParameterSet, 0, 1, 1, 1, Qt.AlignRight)

        self.mainParameterReset = QPushButton(self.mainParameterWdg)
        self.mainParameterReset.setObjectName(u"mainParameterReset")
        self.mainParameterReset.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mainParameterReset.setIcon(icon9)
        self.mainParameterReset.setIconSize(QSize(24, 24))

        self.gridLayout_15.addWidget(self.mainParameterReset, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.mainParameterWdg)

        self.label_6 = QLabel(self.chartParametersFrm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_6)

        self.mainParameterValueWdg = QWidget(self.chartParametersFrm)
        self.mainParameterValueWdg.setObjectName(u"mainParameterValueWdg")
        self.mainParameterValueWdg.setMinimumSize(QSize(0, 50))
        self.mainParameterValueWdg.setFont(font)
        self.gridLayout_16 = QGridLayout(self.mainParameterValueWdg)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.mainParameterValue = QComboBox(self.mainParameterValueWdg)
        self.mainParameterValue.addItem("")
        self.mainParameterValue.setObjectName(u"mainParameterValue")
        self.mainParameterValue.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.mainParameterValue.sizePolicy().hasHeightForWidth())
        self.mainParameterValue.setSizePolicy(sizePolicy4)
        self.mainParameterValue.setFont(font)
        self.mainParameterValue.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_16.addWidget(self.mainParameterValue, 0, 0, 1, 1)

        self.mainParameterValueSet = QPushButton(self.mainParameterValueWdg)
        self.mainParameterValueSet.setObjectName(u"mainParameterValueSet")
        self.mainParameterValueSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainParameterValueSet.setIcon(icon8)
        self.mainParameterValueSet.setIconSize(QSize(24, 24))

        self.gridLayout_16.addWidget(self.mainParameterValueSet, 0, 1, 1, 1)

        self.mainParameterValueReset = QPushButton(self.mainParameterValueWdg)
        self.mainParameterValueReset.setObjectName(u"mainParameterValueReset")
        self.mainParameterValueReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainParameterValueReset.setIcon(icon9)
        self.mainParameterValueReset.setIconSize(QSize(24, 24))

        self.gridLayout_16.addWidget(self.mainParameterValueReset, 0, 2, 1, 1)


        self.verticalLayout_25.addWidget(self.mainParameterValueWdg)

        self.line_6 = QFrame(self.chartParametersFrm)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_6)

        self.line_7 = QFrame(self.chartParametersFrm)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFont(font)
        self.line_7.setLineWidth(3)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_25.addWidget(self.line_7)

        self.agregationLbl = QLabel(self.chartParametersFrm)
        self.agregationLbl.setObjectName(u"agregationLbl")
        self.agregationLbl.setFont(font5)

        self.verticalLayout_25.addWidget(self.agregationLbl)

        self.agregationTypeWdg = QFrame(self.chartParametersFrm)
        self.agregationTypeWdg.setObjectName(u"agregationTypeWdg")
        self.agregationTypeWdg.setMinimumSize(QSize(0, 50))
        self.agregationTypeWdg.setFrameShape(QFrame.StyledPanel)
        self.agregationTypeWdg.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.agregationTypeWdg)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 10)
        self.agregationType = QComboBox(self.agregationTypeWdg)
        self.agregationType.addItem("")
        self.agregationType.addItem("")
        self.agregationType.addItem("")
        self.agregationType.addItem("")
        self.agregationType.setObjectName(u"agregationType")
        self.agregationType.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.agregationType.sizePolicy().hasHeightForWidth())
        self.agregationType.setSizePolicy(sizePolicy5)
        self.agregationType.setMinimumSize(QSize(0, 0))
        self.agregationType.setFont(font)
        self.agregationType.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregationType.setEditable(False)

        self.gridLayout_17.addWidget(self.agregationType, 0, 0, 1, 1)

        self.agregationTypeSet = QPushButton(self.agregationTypeWdg)
        self.agregationTypeSet.setObjectName(u"agregationTypeSet")
        self.agregationTypeSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregationTypeSet.setIcon(icon8)
        self.agregationTypeSet.setIconSize(QSize(24, 24))

        self.gridLayout_17.addWidget(self.agregationTypeSet, 0, 1, 1, 1, Qt.AlignRight)

        self.agregationTypeReset = QPushButton(self.agregationTypeWdg)
        self.agregationTypeReset.setObjectName(u"agregationTypeReset")
        self.agregationTypeReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregationTypeReset.setIcon(icon9)
        self.agregationTypeReset.setIconSize(QSize(24, 24))

        self.gridLayout_17.addWidget(self.agregationTypeReset, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.agregationTypeWdg)

        self.label_7 = QLabel(self.chartParametersFrm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.verticalLayout_25.addWidget(self.label_7)

        self.agregationParameterWdg = QWidget(self.chartParametersFrm)
        self.agregationParameterWdg.setObjectName(u"agregationParameterWdg")
        self.agregationParameterWdg.setMinimumSize(QSize(0, 50))
        self.gridLayout_18 = QGridLayout(self.agregationParameterWdg)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 20)
        self.agregationParameterSet = QPushButton(self.agregationParameterWdg)
        self.agregationParameterSet.setObjectName(u"agregationParameterSet")
        self.agregationParameterSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregationParameterSet.setIcon(icon8)
        self.agregationParameterSet.setIconSize(QSize(24, 24))

        self.gridLayout_18.addWidget(self.agregationParameterSet, 0, 1, 1, 1, Qt.AlignRight)

        self.agregationParameterReset = QPushButton(self.agregationParameterWdg)
        self.agregationParameterReset.setObjectName(u"agregationParameterReset")
        self.agregationParameterReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.agregationParameterReset.setIcon(icon9)
        self.agregationParameterReset.setIconSize(QSize(24, 24))

        self.gridLayout_18.addWidget(self.agregationParameterReset, 0, 2, 1, 1, Qt.AlignRight)

        self.agregationParameter = QComboBox(self.agregationParameterWdg)
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.addItem("")
        self.agregationParameter.setObjectName(u"agregationParameter")
        self.agregationParameter.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.agregationParameter.sizePolicy().hasHeightForWidth())
        self.agregationParameter.setSizePolicy(sizePolicy4)
        self.agregationParameter.setFont(font)
        self.agregationParameter.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_18.addWidget(self.agregationParameter, 0, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.agregationParameterWdg)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_4)


        self.verticalLayout_11.addWidget(self.chartParametersFrm)

        self.chart_button_next = QWidget(self.chartParametersPage)
        self.chart_button_next.setObjectName(u"chart_button_next")
        sizePolicy.setHeightForWidth(self.chart_button_next.sizePolicy().hasHeightForWidth())
        self.chart_button_next.setSizePolicy(sizePolicy)
        self.chart_button_next.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_10 = QHBoxLayout(self.chart_button_next)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.continueLineChartBtn = QPushButton(self.chart_button_next)
        self.continueLineChartBtn.setObjectName(u"continueLineChartBtn")
        self.continueLineChartBtn.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.continueLineChartBtn.sizePolicy().hasHeightForWidth())
        self.continueLineChartBtn.setSizePolicy(sizePolicy6)
        self.continueLineChartBtn.setMinimumSize(QSize(150, 0))
        self.continueLineChartBtn.setMaximumSize(QSize(16777215, 16777215))
        self.continueLineChartBtn.setFont(font2)
        self.continueLineChartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.continueLineChartBtn.setLayoutDirection(Qt.RightToLeft)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.continueLineChartBtn.setIcon(icon10)
        self.continueLineChartBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.continueLineChartBtn)


        self.verticalLayout_11.addWidget(self.chart_button_next, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.chartParametersPage)
        self.chartPlotPage = QWidget()
        self.chartPlotPage.setObjectName(u"chartPlotPage")
        self.verticalLayout_15 = QVBoxLayout(self.chartPlotPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.chartWdg = QWidget(self.chartPlotPage)
        self.chartWdg.setObjectName(u"chartWdg")
        self.verticalLayout_24 = QVBoxLayout(self.chartWdg)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_2 = QFrame(self.chartWdg)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777211, 55))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.graphTypeQCB = QComboBox(self.widget_3)
        self.graphTypeQCB.addItem("")
        self.graphTypeQCB.addItem("")
        self.graphTypeQCB.addItem("")
        self.graphTypeQCB.setObjectName(u"graphTypeQCB")
        self.graphTypeQCB.setFont(font)
        self.graphTypeQCB.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.graphTypeQCB)

        self.refreshChartBtn = QPushButton(self.widget_3)
        self.refreshChartBtn.setObjectName(u"refreshChartBtn")
        self.refreshChartBtn.setMaximumSize(QSize(50, 50))
        self.refreshChartBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshChartBtn.setIcon(icon5)
        self.refreshChartBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.refreshChartBtn)


        self.horizontalLayout_7.addWidget(self.widget_3, 0, Qt.AlignLeft)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(45, 40))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.pushButton_4, 0, Qt.AlignRight)


        self.verticalLayout_24.addWidget(self.frame_2)

        self.lineChartWdg = QWidget(self.chartWdg)
        self.lineChartWdg.setObjectName(u"lineChartWdg")
        sizePolicy3.setHeightForWidth(self.lineChartWdg.sizePolicy().hasHeightForWidth())
        self.lineChartWdg.setSizePolicy(sizePolicy3)
        self.gridLayout_14 = QGridLayout(self.lineChartWdg)
        self.gridLayout_14.setObjectName(u"gridLayout_14")

        self.verticalLayout_24.addWidget(self.lineChartWdg)

        self.widget_6 = QWidget(self.chartWdg)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.returnToChartParameters = QPushButton(self.widget_6)
        self.returnToChartParameters.setObjectName(u"returnToChartParameters")
        self.returnToChartParameters.setFont(font)
        self.returnToChartParameters.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.returnToChartParameters.setIcon(icon11)
        self.returnToChartParameters.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.returnToChartParameters, 0, Qt.AlignLeft)


        self.verticalLayout_24.addWidget(self.widget_6, 0, Qt.AlignBottom)


        self.verticalLayout_15.addWidget(self.chartWdg)

        self.mainPages.addWidget(self.chartPlotPage)
        self.ratingParametersPage = QWidget()
        self.ratingParametersPage.setObjectName(u"ratingParametersPage")
        self.verticalLayout_16 = QVBoxLayout(self.ratingParametersPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.rating_header = QWidget(self.ratingParametersPage)
        self.rating_header.setObjectName(u"rating_header")
        self.horizontalLayout_15 = QHBoxLayout(self.rating_header)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 11, 0, 11)
        self.ratingLbl = QLabel(self.rating_header)
        self.ratingLbl.setObjectName(u"ratingLbl")
        self.ratingLbl.setFont(font4)

        self.horizontalLayout_15.addWidget(self.ratingLbl, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.rating_header)

        self.ratingParametersFrm = QFrame(self.ratingParametersPage)
        self.ratingParametersFrm.setObjectName(u"ratingParametersFrm")
        sizePolicy3.setHeightForWidth(self.ratingParametersFrm.sizePolicy().hasHeightForWidth())
        self.ratingParametersFrm.setSizePolicy(sizePolicy3)
        self.ratingParametersFrm.setFrameShape(QFrame.StyledPanel)
        self.ratingParametersFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.ratingParametersFrm)
        self.verticalLayout_27.setSpacing(20)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.parameterLbl_2 = QLabel(self.ratingParametersFrm)
        self.parameterLbl_2.setObjectName(u"parameterLbl_2")
        self.parameterLbl_2.setFont(font5)

        self.verticalLayout_27.addWidget(self.parameterLbl_2)

        self.ratingMainParameterWdg = QWidget(self.ratingParametersFrm)
        self.ratingMainParameterWdg.setObjectName(u"ratingMainParameterWdg")
        self.ratingMainParameterWdg.setMinimumSize(QSize(0, 50))
        self.gridLayout_20 = QGridLayout(self.ratingMainParameterWdg)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 15)
        self.ratingMainParameterSet = QPushButton(self.ratingMainParameterWdg)
        self.ratingMainParameterSet.setObjectName(u"ratingMainParameterSet")
        self.ratingMainParameterSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingMainParameterSet.setIcon(icon8)
        self.ratingMainParameterSet.setIconSize(QSize(24, 24))

        self.gridLayout_20.addWidget(self.ratingMainParameterSet, 0, 1, 1, 1, Qt.AlignRight)

        self.ratingMainParameterReset = QPushButton(self.ratingMainParameterWdg)
        self.ratingMainParameterReset.setObjectName(u"ratingMainParameterReset")
        self.ratingMainParameterReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingMainParameterReset.setIcon(icon9)
        self.ratingMainParameterReset.setIconSize(QSize(24, 24))

        self.gridLayout_20.addWidget(self.ratingMainParameterReset, 0, 2, 1, 1, Qt.AlignRight)

        self.ratingMainParameter = QComboBox(self.ratingMainParameterWdg)
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.addItem("")
        self.ratingMainParameter.setObjectName(u"ratingMainParameter")
        sizePolicy4.setHeightForWidth(self.ratingMainParameter.sizePolicy().hasHeightForWidth())
        self.ratingMainParameter.setSizePolicy(sizePolicy4)
        self.ratingMainParameter.setFont(font)
        self.ratingMainParameter.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingMainParameter.setInsertPolicy(QComboBox.InsertAtBottom)

        self.gridLayout_20.addWidget(self.ratingMainParameter, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.ratingMainParameterWdg)

        self.label_8 = QLabel(self.ratingParametersFrm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.verticalLayout_27.addWidget(self.label_8)

        self.ratingMainParameterValueWdg = QWidget(self.ratingParametersFrm)
        self.ratingMainParameterValueWdg.setObjectName(u"ratingMainParameterValueWdg")
        self.ratingMainParameterValueWdg.setMinimumSize(QSize(0, 50))
        self.ratingMainParameterValueWdg.setFont(font)
        self.gridLayout_21 = QGridLayout(self.ratingMainParameterValueWdg)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.ratingYearSet = QPushButton(self.ratingMainParameterValueWdg)
        self.ratingYearSet.setObjectName(u"ratingYearSet")
        self.ratingYearSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingYearSet.setIcon(icon8)
        self.ratingYearSet.setIconSize(QSize(24, 24))

        self.gridLayout_21.addWidget(self.ratingYearSet, 0, 2, 1, 1)

        self.ratingYearFrom = QComboBox(self.ratingMainParameterValueWdg)
        self.ratingYearFrom.addItem("")
        self.ratingYearFrom.setObjectName(u"ratingYearFrom")
        self.ratingYearFrom.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.ratingYearFrom.sizePolicy().hasHeightForWidth())
        self.ratingYearFrom.setSizePolicy(sizePolicy4)
        self.ratingYearFrom.setFont(font)
        self.ratingYearFrom.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_21.addWidget(self.ratingYearFrom, 0, 0, 1, 1)

        self.ratingYearReset = QPushButton(self.ratingMainParameterValueWdg)
        self.ratingYearReset.setObjectName(u"ratingYearReset")
        self.ratingYearReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingYearReset.setIcon(icon9)
        self.ratingYearReset.setIconSize(QSize(24, 24))

        self.gridLayout_21.addWidget(self.ratingYearReset, 0, 3, 1, 1)

        self.ratingYearTo = QComboBox(self.ratingMainParameterValueWdg)
        self.ratingYearTo.addItem("")
        self.ratingYearTo.setObjectName(u"ratingYearTo")
        self.ratingYearTo.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.ratingYearTo.sizePolicy().hasHeightForWidth())
        self.ratingYearTo.setSizePolicy(sizePolicy4)
        self.ratingYearTo.setFont(font)

        self.gridLayout_21.addWidget(self.ratingYearTo, 0, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.ratingMainParameterValueWdg)

        self.line_8 = QFrame(self.ratingParametersFrm)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_8)

        self.line_9 = QFrame(self.ratingParametersFrm)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFont(font)
        self.line_9.setLineWidth(3)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_9)

        self.ratingAgregationLbl = QLabel(self.ratingParametersFrm)
        self.ratingAgregationLbl.setObjectName(u"ratingAgregationLbl")
        self.ratingAgregationLbl.setFont(font5)

        self.verticalLayout_27.addWidget(self.ratingAgregationLbl)

        self.ratingAgregationTypeWdg = QFrame(self.ratingParametersFrm)
        self.ratingAgregationTypeWdg.setObjectName(u"ratingAgregationTypeWdg")
        self.ratingAgregationTypeWdg.setMinimumSize(QSize(0, 50))
        self.ratingAgregationTypeWdg.setFrameShape(QFrame.StyledPanel)
        self.ratingAgregationTypeWdg.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.ratingAgregationTypeWdg)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, 0, 0, 10)
        self.ratingAgregationType = QComboBox(self.ratingAgregationTypeWdg)
        self.ratingAgregationType.addItem("")
        self.ratingAgregationType.addItem("")
        self.ratingAgregationType.addItem("")
        self.ratingAgregationType.addItem("")
        self.ratingAgregationType.setObjectName(u"ratingAgregationType")
        self.ratingAgregationType.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.ratingAgregationType.sizePolicy().hasHeightForWidth())
        self.ratingAgregationType.setSizePolicy(sizePolicy5)
        self.ratingAgregationType.setMinimumSize(QSize(0, 0))
        self.ratingAgregationType.setFont(font)
        self.ratingAgregationType.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingAgregationType.setEditable(False)

        self.gridLayout_22.addWidget(self.ratingAgregationType, 0, 0, 1, 1)

        self.ratingAgregationTypeSet = QPushButton(self.ratingAgregationTypeWdg)
        self.ratingAgregationTypeSet.setObjectName(u"ratingAgregationTypeSet")
        self.ratingAgregationTypeSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingAgregationTypeSet.setIcon(icon8)
        self.ratingAgregationTypeSet.setIconSize(QSize(24, 24))

        self.gridLayout_22.addWidget(self.ratingAgregationTypeSet, 0, 1, 1, 1, Qt.AlignRight)

        self.ratingAgregationTypeReset = QPushButton(self.ratingAgregationTypeWdg)
        self.ratingAgregationTypeReset.setObjectName(u"ratingAgregationTypeReset")
        self.ratingAgregationTypeReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingAgregationTypeReset.setIcon(icon9)
        self.ratingAgregationTypeReset.setIconSize(QSize(24, 24))

        self.gridLayout_22.addWidget(self.ratingAgregationTypeReset, 0, 2, 1, 1, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.ratingAgregationTypeWdg)

        self.label_9 = QLabel(self.ratingParametersFrm)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.verticalLayout_27.addWidget(self.label_9)

        self.ratingAgregationParameterWdg = QWidget(self.ratingParametersFrm)
        self.ratingAgregationParameterWdg.setObjectName(u"ratingAgregationParameterWdg")
        self.ratingAgregationParameterWdg.setMinimumSize(QSize(0, 50))
        self.gridLayout_23 = QGridLayout(self.ratingAgregationParameterWdg)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 20)
        self.ratingAgregationParameterSet = QPushButton(self.ratingAgregationParameterWdg)
        self.ratingAgregationParameterSet.setObjectName(u"ratingAgregationParameterSet")
        self.ratingAgregationParameterSet.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingAgregationParameterSet.setIcon(icon8)
        self.ratingAgregationParameterSet.setIconSize(QSize(24, 24))

        self.gridLayout_23.addWidget(self.ratingAgregationParameterSet, 0, 1, 1, 1, Qt.AlignRight)

        self.ratingAgregationParameterReset = QPushButton(self.ratingAgregationParameterWdg)
        self.ratingAgregationParameterReset.setObjectName(u"ratingAgregationParameterReset")
        self.ratingAgregationParameterReset.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingAgregationParameterReset.setIcon(icon9)
        self.ratingAgregationParameterReset.setIconSize(QSize(24, 24))

        self.gridLayout_23.addWidget(self.ratingAgregationParameterReset, 0, 2, 1, 1, Qt.AlignRight)

        self.ratingAgregationParameter = QComboBox(self.ratingAgregationParameterWdg)
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.addItem("")
        self.ratingAgregationParameter.setObjectName(u"ratingAgregationParameter")
        self.ratingAgregationParameter.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.ratingAgregationParameter.sizePolicy().hasHeightForWidth())
        self.ratingAgregationParameter.setSizePolicy(sizePolicy4)
        self.ratingAgregationParameter.setFont(font)
        self.ratingAgregationParameter.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_23.addWidget(self.ratingAgregationParameter, 0, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.ratingAgregationParameterWdg)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_5)


        self.verticalLayout_16.addWidget(self.ratingParametersFrm)

        self.rating_button_next = QWidget(self.ratingParametersPage)
        self.rating_button_next.setObjectName(u"rating_button_next")
        sizePolicy.setHeightForWidth(self.rating_button_next.sizePolicy().hasHeightForWidth())
        self.rating_button_next.setSizePolicy(sizePolicy)
        self.rating_button_next.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_16 = QHBoxLayout(self.rating_button_next)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.continueRatingBtn = QPushButton(self.rating_button_next)
        self.continueRatingBtn.setObjectName(u"continueRatingBtn")
        self.continueRatingBtn.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.continueRatingBtn.sizePolicy().hasHeightForWidth())
        self.continueRatingBtn.setSizePolicy(sizePolicy6)
        self.continueRatingBtn.setMinimumSize(QSize(150, 0))
        self.continueRatingBtn.setMaximumSize(QSize(16777215, 16777215))
        self.continueRatingBtn.setFont(font2)
        self.continueRatingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.continueRatingBtn.setLayoutDirection(Qt.RightToLeft)
        self.continueRatingBtn.setIcon(icon10)
        self.continueRatingBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_16.addWidget(self.continueRatingBtn, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.rating_button_next, 0, Qt.AlignRight)

        self.mainPages.addWidget(self.ratingParametersPage)
        self.ratingPlotPage = QWidget()
        self.ratingPlotPage.setObjectName(u"ratingPlotPage")
        self.verticalLayout_17 = QVBoxLayout(self.ratingPlotPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.ratingWdg = QWidget(self.ratingPlotPage)
        self.ratingWdg.setObjectName(u"ratingWdg")
        self.verticalLayout_26 = QVBoxLayout(self.ratingWdg)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_3 = QFrame(self.ratingWdg)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777211, 55))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.frame_3)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ratingNumLE = QLineEdit(self.widget_7)
        self.ratingNumLE.setObjectName(u"ratingNumLE")
        self.ratingNumLE.setMinimumSize(QSize(200, 0))
        self.ratingNumLE.setFont(font)

        self.horizontalLayout_13.addWidget(self.ratingNumLE)

        self.refreshRatingBtn = QPushButton(self.widget_7)
        self.refreshRatingBtn.setObjectName(u"refreshRatingBtn")
        self.refreshRatingBtn.setMaximumSize(QSize(50, 50))
        self.refreshRatingBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.refreshRatingBtn.setIcon(icon5)
        self.refreshRatingBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.refreshRatingBtn)


        self.horizontalLayout_12.addWidget(self.widget_7, 0, Qt.AlignLeft)

        self.ratingSaveBtn = QPushButton(self.frame_3)
        self.ratingSaveBtn.setObjectName(u"ratingSaveBtn")
        self.ratingSaveBtn.setMaximumSize(QSize(45, 40))
        self.ratingSaveBtn.setFont(font)
        self.ratingSaveBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ratingSaveBtn.setIcon(icon6)
        self.ratingSaveBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_12.addWidget(self.ratingSaveBtn, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_3)

        self.ratingChartWdg = QWidget(self.ratingWdg)
        self.ratingChartWdg.setObjectName(u"ratingChartWdg")
        sizePolicy3.setHeightForWidth(self.ratingChartWdg.sizePolicy().hasHeightForWidth())
        self.ratingChartWdg.setSizePolicy(sizePolicy3)
        self.gridLayout_19 = QGridLayout(self.ratingChartWdg)
        self.gridLayout_19.setObjectName(u"gridLayout_19")

        self.verticalLayout_26.addWidget(self.ratingChartWdg)

        self.widget_8 = QWidget(self.ratingWdg)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.returnToRatingParameters = QPushButton(self.widget_8)
        self.returnToRatingParameters.setObjectName(u"returnToRatingParameters")
        self.returnToRatingParameters.setFont(font)
        self.returnToRatingParameters.setCursor(QCursor(Qt.PointingHandCursor))
        self.returnToRatingParameters.setIcon(icon11)
        self.returnToRatingParameters.setIconSize(QSize(24, 24))

        self.horizontalLayout_14.addWidget(self.returnToRatingParameters, 0, Qt.AlignLeft)


        self.verticalLayout_26.addWidget(self.widget_8, 0, Qt.AlignBottom)


        self.verticalLayout_17.addWidget(self.ratingWdg)

        self.mainPages.addWidget(self.ratingPlotPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        sizePolicy.setHeightForWidth(self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy)
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 11, 0, 0)
        self.searchWdjt = QWidget(self.rightMenu)
        self.searchWdjt.setObjectName(u"searchWdjt")
        self.searchWdjt.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.searchWdjt)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.searchWdjt)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.verticalLayout_7.addWidget(self.label, 0, Qt.AlignHCenter)

        self.scrollArea = QScrollArea(self.searchWdjt)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 400))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 20, 379))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.searchFrm = QFrame(self.scrollAreaWidgetContents_2)
        self.searchFrm.setObjectName(u"searchFrm")
        sizePolicy1.setHeightForWidth(self.searchFrm.sizePolicy().hasHeightForWidth())
        self.searchFrm.setSizePolicy(sizePolicy1)
        self.searchFrm.setFrameShape(QFrame.StyledPanel)
        self.searchFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.searchFrm)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)

        self.verticalLayout_14.addWidget(self.searchFrm)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea, 0, Qt.AlignTop)

        self.searchBtn = QPushButton(self.searchWdjt)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setFont(font2)
        self.searchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchBtn.setIcon(icon7)
        self.searchBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.searchBtn, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.searchWdjt)


        self.horizontalLayout_2.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footerLbl = QLabel(self.footer)
        self.footerLbl.setObjectName(u"footerLbl")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setBold(True)
        font6.setWeight(75)
        self.footerLbl.setFont(font6)

        self.horizontalLayout_5.addWidget(self.footerLbl, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.nameLbl.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441\u043e\u0432\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.search_table_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.clearTableSearchBtn.setText("")
        self.searchTableNameBtn.setText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.linePlotBtn.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438", None))
        self.ratingPlotBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433\u0438", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.homeLbl.setText("")
        self.refreshBtn.setText("")
        self.saveTableBtn.setText("")
        self.homeSearchBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.chartLbl.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u043f\u043e \u0433\u043e\u0434\u0430\u043c", None))
        self.parameterLbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.mainParameter.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440--", None))
        self.mainParameter.setItemText(1, QCoreApplication.translate("MainWindow", u"game", None))
        self.mainParameter.setItemText(2, QCoreApplication.translate("MainWindow", u"developer", None))
        self.mainParameter.setItemText(3, QCoreApplication.translate("MainWindow", u"publisher", None))
        self.mainParameter.setItemText(4, QCoreApplication.translate("MainWindow", u"category", None))
        self.mainParameter.setItemText(5, QCoreApplication.translate("MainWindow", u"tag", None))
        self.mainParameter.setItemText(6, QCoreApplication.translate("MainWindow", u"genre", None))

        self.mainParameter.setCurrentText(QCoreApplication.translate("MainWindow", u"--\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440--", None))
        self.mainParameterSet.setText("")
        self.mainParameterReset.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430", None))
        self.mainParameterValue.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430--", None))

        self.mainParameterValueSet.setText("")
        self.mainParameterValueReset.setText("")
        self.agregationLbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430", None))
        self.agregationType.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.agregationType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.agregationType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435", None))
        self.agregationType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))

        self.agregationType.setCurrentText(QCoreApplication.translate("MainWindow", u"--\u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.agregationTypeSet.setText("")
        self.agregationTypeReset.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a \u043a\u0430\u043a\u043e\u043c\u0443 \u0438\u0437 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.agregationParameterSet.setText("")
        self.agregationParameterReset.setText("")
        self.agregationParameter.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u043f\u0430\u0440\u0430\u043c\u0435\u0440 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.agregationParameter.setItemText(1, QCoreApplication.translate("MainWindow", u"positive_ratings", None))
        self.agregationParameter.setItemText(2, QCoreApplication.translate("MainWindow", u"negative_ratings", None))
        self.agregationParameter.setItemText(3, QCoreApplication.translate("MainWindow", u"positive_reviews", None))
        self.agregationParameter.setItemText(4, QCoreApplication.translate("MainWindow", u"negative_reviews", None))
        self.agregationParameter.setItemText(5, QCoreApplication.translate("MainWindow", u"average_playtime", None))
        self.agregationParameter.setItemText(6, QCoreApplication.translate("MainWindow", u"median_playtime", None))
        self.agregationParameter.setItemText(7, QCoreApplication.translate("MainWindow", u"owners_low", None))
        self.agregationParameter.setItemText(8, QCoreApplication.translate("MainWindow", u"owners_up", None))
        self.agregationParameter.setItemText(9, QCoreApplication.translate("MainWindow", u"price", None))

        self.continueLineChartBtn.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.graphTypeQCB.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u0432\u0438\u0434--", None))
        self.graphTypeQCB.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.graphTypeQCB.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0413\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))

        self.refreshChartBtn.setText("")
        self.pushButton_4.setText("")
        self.returnToChartParameters.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.ratingLbl.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433\u0438", None))
        self.parameterLbl_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440 \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430", None))
        self.ratingMainParameterSet.setText("")
        self.ratingMainParameterReset.setText("")
        self.ratingMainParameter.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440--", None))
        self.ratingMainParameter.setItemText(1, QCoreApplication.translate("MainWindow", u"game", None))
        self.ratingMainParameter.setItemText(2, QCoreApplication.translate("MainWindow", u"developer", None))
        self.ratingMainParameter.setItemText(3, QCoreApplication.translate("MainWindow", u"publisher", None))
        self.ratingMainParameter.setItemText(4, QCoreApplication.translate("MainWindow", u"category", None))
        self.ratingMainParameter.setItemText(5, QCoreApplication.translate("MainWindow", u"tag", None))
        self.ratingMainParameter.setItemText(6, QCoreApplication.translate("MainWindow", u"genre", None))

        self.ratingMainParameter.setCurrentText(QCoreApplication.translate("MainWindow", u"--\u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440--", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0433\u043e\u0434 (\u043d\u0435\u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u043f\u043e\u043b\u0435)", None))
        self.ratingYearSet.setText("")
        self.ratingYearFrom.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u0441 \u043a\u0430\u043a\u043e\u0433\u043e \u0433\u043e\u0434\u0430--", None))

        self.ratingYearReset.setText("")
        self.ratingYearTo.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u043f\u043e \u043a\u0430\u043a\u043e\u0439 \u0433\u043e\u0434--", None))

        self.ratingAgregationLbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430", None))
        self.ratingAgregationType.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.ratingAgregationType.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.ratingAgregationType.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435", None))
        self.ratingAgregationType.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))

        self.ratingAgregationType.setCurrentText(QCoreApplication.translate("MainWindow", u"--\u0441\u043f\u043e\u0441\u043e\u0431 \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.ratingAgregationTypeSet.setText("")
        self.ratingAgregationTypeReset.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e \u043a\u0430\u043a\u043e\u043c\u0443 \u0438\u0437 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0440\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.ratingAgregationParameterSet.setText("")
        self.ratingAgregationParameterReset.setText("")
        self.ratingAgregationParameter.setItemText(0, QCoreApplication.translate("MainWindow", u"--\u043f\u0430\u0440\u0430\u043c\u0435\u0440 \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430--", None))
        self.ratingAgregationParameter.setItemText(1, QCoreApplication.translate("MainWindow", u"positive_ratings", None))
        self.ratingAgregationParameter.setItemText(2, QCoreApplication.translate("MainWindow", u"negative_ratings", None))
        self.ratingAgregationParameter.setItemText(3, QCoreApplication.translate("MainWindow", u"positive_reviews", None))
        self.ratingAgregationParameter.setItemText(4, QCoreApplication.translate("MainWindow", u"negative_reviews", None))
        self.ratingAgregationParameter.setItemText(5, QCoreApplication.translate("MainWindow", u"average_playtime", None))
        self.ratingAgregationParameter.setItemText(6, QCoreApplication.translate("MainWindow", u"median_playtime", None))
        self.ratingAgregationParameter.setItemText(7, QCoreApplication.translate("MainWindow", u"owners_low", None))
        self.ratingAgregationParameter.setItemText(8, QCoreApplication.translate("MainWindow", u"owners_up", None))
        self.ratingAgregationParameter.setItemText(9, QCoreApplication.translate("MainWindow", u"price", None))

        self.continueRatingBtn.setText(QCoreApplication.translate("MainWindow", u" \u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.ratingNumLE.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.refreshRatingBtn.setText("")
        self.ratingSaveBtn.setText("")
        self.returnToRatingParameters.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044f \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.footerLbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u0434\u043b\u044f \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445 2022", None))
    # retranslateUi

