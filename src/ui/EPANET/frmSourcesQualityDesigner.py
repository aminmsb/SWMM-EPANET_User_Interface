# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EPANET\frmSourcesQualityDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmSourcesQuality(object):
    def setupUi(self, frmSourcesQuality):
        frmSourcesQuality.setObjectName("frmSourcesQuality")
        frmSourcesQuality.resize(356, 277)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmSourcesQuality.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmSourcesQuality)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.gridLayout = QtWidgets.QGridLayout(self.fraTop)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblQuality = QtWidgets.QLabel(self.fraTop)
        self.lblQuality.setObjectName("lblQuality")
        self.gridLayout.addWidget(self.lblQuality, 0, 0, 1, 1)
        self.txtQuality = QtWidgets.QLineEdit(self.fraTop)
        self.txtQuality.setObjectName("txtQuality")
        self.gridLayout.addWidget(self.txtQuality, 0, 1, 1, 1)
        self.lblPattern = QtWidgets.QLabel(self.fraTop)
        self.lblPattern.setObjectName("lblPattern")
        self.gridLayout.addWidget(self.lblPattern, 1, 0, 1, 1)
        self.txtPattern = QtWidgets.QLineEdit(self.fraTop)
        self.txtPattern.setObjectName("txtPattern")
        self.gridLayout.addWidget(self.txtPattern, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.fraTop)
        self.gbxType = QtWidgets.QGroupBox(self.centralWidget)
        self.gbxType.setObjectName("gbxType")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbxType)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbnConcentration = QtWidgets.QRadioButton(self.gbxType)
        self.rbnConcentration.setObjectName("rbnConcentration")
        self.gridLayout_2.addWidget(self.rbnConcentration, 0, 0, 1, 1)
        self.rbnSetPoint = QtWidgets.QRadioButton(self.gbxType)
        self.rbnSetPoint.setObjectName("rbnSetPoint")
        self.gridLayout_2.addWidget(self.rbnSetPoint, 0, 1, 1, 1)
        self.rbnMass = QtWidgets.QRadioButton(self.gbxType)
        self.rbnMass.setObjectName("rbnMass")
        self.gridLayout_2.addWidget(self.rbnMass, 1, 0, 1, 1)
        self.rbnFlow = QtWidgets.QRadioButton(self.gbxType)
        self.rbnFlow.setObjectName("rbnFlow")
        self.gridLayout_2.addWidget(self.rbnFlow, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.gbxType)
        self.fraOKCancel = QtWidgets.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraOKCancel.setObjectName("fraOKCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmSourcesQuality.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmSourcesQuality)
        QtCore.QMetaObject.connectSlotsByName(frmSourcesQuality)

    def retranslateUi(self, frmSourcesQuality):
        _translate = QtCore.QCoreApplication.translate
        frmSourcesQuality.setWindowTitle(_translate("frmSourcesQuality", "EPANET Source Editor"))
        self.lblQuality.setText(_translate("frmSourcesQuality", "Source Quality"))
        self.lblPattern.setText(_translate("frmSourcesQuality", "Time Pattern"))
        self.gbxType.setTitle(_translate("frmSourcesQuality", "Source Type"))
        self.rbnConcentration.setText(_translate("frmSourcesQuality", "Concentration"))
        self.rbnSetPoint.setText(_translate("frmSourcesQuality", "Setpoint Booster"))
        self.rbnMass.setText(_translate("frmSourcesQuality", "MassBooster"))
        self.rbnFlow.setText(_translate("frmSourcesQuality", "Flow Paced Booster"))
        self.cmdOK.setText(_translate("frmSourcesQuality", "OK"))
        self.cmdCancel.setText(_translate("frmSourcesQuality", "Cancel"))

