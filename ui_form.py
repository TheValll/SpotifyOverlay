# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QTextBrowser, QWidget)
import rc_ressource

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 600)
        Widget.setMinimumSize(QSize(400, 600))
        Widget.setMaximumSize(QSize(400, 600))
        Widget.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.musicName = QTextBrowser(Widget)
        self.musicName.setObjectName(u"musicName")
        self.musicName.setGeometry(QRect(40, 387, 301, 101))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        font.setBold(True)
        self.musicName.setFont(font)
        self.musicName.setStyleSheet(u"background-color: transparent;\n"
"border-color: rgb(0, 0, 0);\n"
"border: none;\n"
"color: rgb(250, 250, 250)")
        self.artistName = QTextBrowser(Widget)
        self.artistName.setObjectName(u"artistName")
        self.artistName.setGeometry(QRect(40, 360, 351, 31))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.artistName.setFont(font1)
        self.artistName.setStyleSheet(u"background-color: transparent;\n"
"border-color: rgb(0, 0, 0);\n"
"border: none;\n"
"color: rgb(250, 250, 250)")
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(50, 491, 305, 7))
        self.progressBar.setMinimumSize(QSize(305, 7))
        self.progressBar.setMaximumSize(QSize(250, 7))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)
        self.musicImage = QLabel(Widget)
        self.musicImage.setObjectName(u"musicImage")
        self.musicImage.setGeometry(QRect(50, 50, 300, 300))
        self.musicImage.setMinimumSize(QSize(300, 300))
        self.musicImage.setMaximumSize(QSize(300, 300))
        self.musicImage.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.musicImage.setScaledContents(True)
        self.bg = QLabel(Widget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(0, 0, 400, 600))
        self.bg.setMinimumSize(QSize(400, 600))
        self.bg.setMaximumSize(QSize(400, 600))
        font2 = QFont()
        font2.setFamilies([u"Roman"])
        self.bg.setFont(font2)
        self.bg.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.bg.setPixmap(QPixmap(u":/img/img/SPOTIFY_HUD.png"))
        self.bg.setScaledContents(True)
        self.bg.raise_()
        self.progressBar.raise_()
        self.musicName.raise_()
        self.artistName.raise_()
        self.musicImage.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.musicName.setMarkdown("")
        self.musicName.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.artistName.setMarkdown("")
        self.artistName.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt; font-weight:400;\"><br /></p></body></html>", None))
        self.progressBar.setFormat(QCoreApplication.translate("Widget", u"%p%", None))
        self.musicImage.setText("")
        self.bg.setText("")
    # retranslateUi

