# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw_menus.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget.addTab(self.tab_12, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.label_71 = QtWidgets.QLabel(self.centralwidget)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_4.addWidget(self.label_71)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 28))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenuSub = QtWidgets.QMenu(self.menuMenu)
        self.menuMenuSub.setObjectName("menuMenuSub")
        self.menuMenuDelayed = QtWidgets.QMenu(self.menubar)
        self.menuMenuDelayed.setObjectName("menuMenuDelayed")
        self.menuMenuSubDelayed = QtWidgets.QMenu(self.menuMenuDelayed)
        self.menuMenuSubDelayed.setObjectName("menuMenuSubDelayed")
        self.menuMenuCheckale = QtWidgets.QMenu(self.menubar)
        self.menuMenuCheckale.setObjectName("menuMenuCheckale")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBarDelayed = QtWidgets.QToolBar(MainWindow)
        self.toolBarDelayed.setObjectName("toolBarDelayed")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDelayed)
        self.toolBarCheckable = QtWidgets.QToolBar(MainWindow)
        self.toolBarCheckable.setObjectName("toolBarCheckable")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarCheckable)
        MainWindow.insertToolBarBreak(self.toolBarCheckable)
        self.actionActionA = QtWidgets.QAction(MainWindow)
        self.actionActionA.setObjectName("actionActionA")
        self.actionActionSubA = QtWidgets.QAction(MainWindow)
        self.actionActionSubA.setObjectName("actionActionSubA")
        self.actionActionSubB = QtWidgets.QAction(MainWindow)
        self.actionActionSubB.setObjectName("actionActionSubB")
        self.actionActionDelayedA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedA.setObjectName("actionActionDelayedA")
        self.actionActionDelayedSubA = QtWidgets.QAction(MainWindow)
        self.actionActionDelayedSubA.setObjectName("actionActionDelayedSubA")
        self.actionActionCheckableA = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableA.setCheckable(True)
        self.actionActionCheckableA.setObjectName("actionActionCheckableA")
        self.actionActionCheckableSubAChecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAChecked.setCheckable(True)
        self.actionActionCheckableSubAChecked.setChecked(True)
        self.actionActionCheckableSubAChecked.setObjectName("actionActionCheckableSubAChecked")
        self.actionActionCheckableSubAUnchecked = QtWidgets.QAction(MainWindow)
        self.actionActionCheckableSubAUnchecked.setCheckable(True)
        self.actionActionCheckableSubAUnchecked.setObjectName("actionActionCheckableSubAUnchecked")
        self.menuMenuSub.addAction(self.actionActionSubA)
        self.menuMenuSub.addAction(self.actionActionSubB)
        self.menuMenu.addAction(self.actionActionA)
        self.menuMenu.addAction(self.menuMenuSub.menuAction())
        self.menuMenuSubDelayed.addAction(self.actionActionDelayedSubA)
        self.menuMenuDelayed.addAction(self.actionActionDelayedA)
        self.menuMenuDelayed.addAction(self.menuMenuSubDelayed.menuAction())
        self.menuMenuCheckale.addAction(self.actionActionCheckableA)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuMenuDelayed.menuAction())
        self.menubar.addAction(self.menuMenuCheckale.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionActionA)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionActionSubA)
        self.toolBar.addAction(self.actionActionSubB)
        self.toolBarDelayed.addAction(self.actionActionDelayedA)
        self.toolBarDelayed.addSeparator()
        self.toolBarDelayed.addAction(self.actionActionDelayedSubA)
        self.toolBarCheckable.addAction(self.actionActionCheckableA)
        self.toolBarCheckable.addSeparator()
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAChecked)
        self.toolBarCheckable.addAction(self.actionActionCheckableSubAUnchecked)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(11)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Issue #115 - Tabs scroller buttons"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Page"))
        self.groupBox.setTitle(_translate("MainWindow", "Issue #112 - Hyperlinks color"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a href=\"https://github.com/ColinDuquesnoy/QDarkStyleSheet/issues/112\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">Hyperlink Example</span></a></p><p align=\"center\"><span style=\" font-size:10pt; color:#7d7d7d;\">CSS for the documents (RichText) is not the same as the application. We cannot change the internal content CSS, e.g., hyperlinks. We suggest you use the middle tons (0-255, use 125), so this works for both white and dark theme (this color). The original color is the blue link on top.</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_71.setText(_translate("MainWindow", "Inside Central Widget"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuMenuSub.setTitle(_translate("MainWindow", "Menu Sub"))
        self.menuMenuDelayed.setTitle(_translate("MainWindow", "Menu Delayed"))
        self.menuMenuSubDelayed.setTitle(_translate("MainWindow", "Menu Sub Delayed"))
        self.menuMenuCheckale.setTitle(_translate("MainWindow", "Menu Checkable"))
        self.menuAbout.setTitle(_translate("MainWindow", "About QDarkStyle"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Tool bar actions"))
        self.toolBarDelayed.setWindowTitle(_translate("MainWindow", "Tool bar actions delayed"))
        self.toolBarCheckable.setWindowTitle(_translate("MainWindow", "Tool bar action checkable"))
        self.actionActionA.setText(_translate("MainWindow", "Action A"))
        self.actionActionSubA.setText(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubA.setToolTip(_translate("MainWindow", "Action A Sub"))
        self.actionActionSubB.setText(_translate("MainWindow", "Action B Sub"))
        self.actionActionDelayedA.setText(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedA.setToolTip(_translate("MainWindow", "Action Delayed A"))
        self.actionActionDelayedSubA.setText(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionDelayedSubA.setToolTip(_translate("MainWindow", "Action Delayed Sub A"))
        self.actionActionCheckableA.setText(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableA.setToolTip(_translate("MainWindow", "Action Checkable A"))
        self.actionActionCheckableSubAChecked.setText(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAChecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Checked"))
        self.actionActionCheckableSubAUnchecked.setText(_translate("MainWindow", "Action Checkable Sub A Unchecked"))
        self.actionActionCheckableSubAUnchecked.setToolTip(_translate("MainWindow", "Action Checkable Sub A Unchecked"))

