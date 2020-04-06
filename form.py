# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 452)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(420, 452))
        Form.setMaximumSize(QSize(420, 452))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 90, 383, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.inputTokens = QButtonGroup(Form)
        self.inputTokens.setObjectName(u"inputTokens")
        self.inputTokens.addButton(self.btn_1)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.btn_1.setFont(font)

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_equal = QPushButton(self.gridLayoutWidget)
        self.btn_equal.setObjectName(u"btn_equal")
        sizePolicy1.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy1)
        self.btn_equal.setFont(font)

        self.gridLayout.addWidget(self.btn_equal, 4, 2, 1, 1)

        self.btn_7 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_7)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_7.setFont(font)

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_div = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_div)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy1.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy1)
        self.btn_div.setFont(font)

        self.gridLayout.addWidget(self.btn_div, 2, 3, 1, 1)

        self.btn_5 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_5)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_5.setFont(font)

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_8 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_8)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_8.setFont(font)

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_4)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_4.setFont(font)

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_6 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_6)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        self.btn_6.setFont(font)

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_3)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_3.setFont(font)

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_add = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_add)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy1.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy1)
        self.btn_add.setFont(font)

        self.gridLayout.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_mul = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_mul)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy1.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy1)
        self.btn_mul.setFont(font)

        self.gridLayout.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_9 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_9)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_9.setFont(font)

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_sub = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_sub)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy1.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy1)
        self.btn_sub.setFont(font)

        self.gridLayout.addWidget(self.btn_sub, 4, 3, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_2)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_2.setFont(font)

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_0 = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_0)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy1.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy1)
        self.btn_0.setFont(font)

        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)

        self.btn_clear = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_clear)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        self.btn_clear.setFont(font)

        self.gridLayout.addWidget(self.btn_clear, 0, 3, 1, 1)

        self.btn_dot = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_dot)
        self.btn_dot.setObjectName(u"btn_dot")
        sizePolicy1.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy1)
        self.btn_dot.setFont(font)

        self.gridLayout.addWidget(self.btn_dot, 4, 1, 1, 1)

        self.btn_bs = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_bs)
        self.btn_bs.setObjectName(u"btn_bs")
        sizePolicy1.setHeightForWidth(self.btn_bs.sizePolicy().hasHeightForWidth())
        self.btn_bs.setSizePolicy(sizePolicy1)
        self.btn_bs.setFont(font)

        self.gridLayout.addWidget(self.btn_bs, 0, 2, 1, 1)

        self.btn_rp = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_rp)
        self.btn_rp.setObjectName(u"btn_rp")
        sizePolicy1.setHeightForWidth(self.btn_rp.sizePolicy().hasHeightForWidth())
        self.btn_rp.setSizePolicy(sizePolicy1)
        self.btn_rp.setFont(font)

        self.gridLayout.addWidget(self.btn_rp, 0, 1, 1, 1)

        self.btn_lp = QPushButton(self.gridLayoutWidget)
        self.inputTokens.addButton(self.btn_lp)
        self.btn_lp.setObjectName(u"btn_lp")
        self.btn_lp.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_lp.sizePolicy().hasHeightForWidth())
        self.btn_lp.setSizePolicy(sizePolicy1)
        self.btn_lp.setFont(font)
        self.btn_lp.setFlat(False)

        self.gridLayout.addWidget(self.btn_lp, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 20, 381, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.lineEdit.setFont(font1)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Grammar Calculator", None))
        self.btn_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btn_equal.setText(QCoreApplication.translate("Form", u"=", None))
        self.btn_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.btn_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btn_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.btn_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btn_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btn_clear.setText(QCoreApplication.translate("Form", u"AC", None))
        self.btn_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.btn_bs.setText(QCoreApplication.translate("Form", u"BS", None))
        self.btn_rp.setText(QCoreApplication.translate("Form", u")", None))
        self.btn_lp.setText(QCoreApplication.translate("Form", u"(", None))
        self.lineEdit.setText("")
    # retranslateUi

