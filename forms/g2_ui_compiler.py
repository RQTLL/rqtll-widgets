# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QSizePolicy, QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget, QPlainTextEdit, QLineEdit)
import os

try:
    from ..utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from ..utils.nav import NavButton
except (ImportError, ValueError):
    import sys
    _parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if _parent not in sys.path:
        sys.path.insert(0, _parent)
    from utils.icon_loader import load_qicon, load_qpixmap, _resolve_icon
    from utils.nav import NavButton

placeholder = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'icons', 'placeholder.svg'))

class Nav(QWidget):
    def __init__(self, Parent, icon_dirs, theme):
        super().__init__(Parent)
        self.icon_dirs = icon_dirs
        self.theme = theme
        self.layout = QVBoxLayout()
        self.layout.setObjectName(u"Nav")
        
        self.code = NavButton(label="", target="code", parent=self)
        self.add(self.code, icon="code")

        self.launch = NavButton(label="", target="launch", parent=self)
        self.add(self.launch, icon="launch")

        self.graph = NavButton(label="", target="nodes", parent=self)
        self.add(self.graph, icon="nodes")

        self.teleop = NavButton(label="", target="teleop", parent=self)
        self.add(self.teleop, icon="teleop")

        self.ssh = NavButton(label="", target="ssh", parent=self)
        self.add(self.ssh, icon="ssh")

        self.spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.layout.addItem(self.spacer)

        self.viz = NavButton(label="", target="3d", parent=self)
        self.add(self.viz, icon="3d")

        self.sim = NavButton(label="", target="emulator", parent=self)
        self.add(self.sim, icon="emulator")

        self.widgets = NavButton(label="", target="widgets", parent=self)
        self.add(self.widgets, icon="widgets")

        self.packages = NavButton(label="", target="package", parent=self)
        self.add(self.packages, icon="package")

    def add(self, item, icon="close"):
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(self.sizePolicy.hasHeightForWidth())
        item.setSizePolicy(self.sizePolicy)
        i = QIcon()
        icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', icon, 'default.svg'), theme=self.theme)
        i.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        item.setIcon(i)
        self.layout.addWidget(item)

class Ui_Widget(object):
    def setupUi(self, Widget, icon_dirs=None, theme='default.qss'): 
        self.icon_dirs = icon_dirs
        self.theme = theme
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1060, 644)
        Widget.setMinimumSize(QSize(575, 350))
        icon = QIcon()
        icon_path = _resolve_icon(icon_dirs, os.path.join('logo.svg'))
        icon.addFile(icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.nav = Nav(Widget, icon_dirs, theme)
        self.nav.setObjectName(u"nav")
        self.horizontalLayout.addLayout(self.nav.layout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        """
        self.BTNDir = QPushButton(Widget)
        self.BTNDir.setObjectName(u"BTNDir")
        icon1 = QIcon()
        icon1_path = _resolve_icon(icon_dirs, os.path.join('folder', 'default.svg'), theme=theme)
        icon1.addFile(icon1_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNDir.setIcon(icon1)
        self.BTNDir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        """
        self.BTNROSCLean = QPushButton(self.frame)
        self.BTNROSCLean.setObjectName(u"BTNROSCLean")
        clean_icon = QIcon()
        clean_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'clean', 'click.svg'), theme=self.theme)
        clean_icon.addFile(clean_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSCLean.setIcon(clean_icon)
        self.BTNROSCLean.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.verticalLayout.addWidget(self.BTNROSCLean)

        self.BTNROSColcon = QPushButton(self.frame)
        self.BTNROSColcon.setObjectName(u"BTNROSColcon")
        compile_icon = QIcon()
        compile_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'compile', 'default.svg'), theme=self.theme)
        compile_icon.addFile(compile_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSColcon.setIcon(compile_icon)
        self.BTNROSColcon.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.verticalLayout.addWidget(self.BTNROSColcon)

        self.BTNROSBag = QPushButton(self.frame)
        self.BTNROSBag.setObjectName(u"BTNROSBag")
        record_icon = QIcon()
        record_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'record', 'default.svg'), theme=self.theme)
        record_icon.addFile(record_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNROSBag.setIcon(record_icon)
        self.BTNROSBag.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.verticalLayout.addWidget(self.BTNROSBag)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")

        self.verticalLayout.addWidget(self.label_1)

        self.LAYOUTNodes = QGridLayout()
        self.LAYOUTNodes.setObjectName(u"LAYOUTNodes")
        self.LABELNode1 = QLabel(self.frame)
        self.LABELNode1.setObjectName(u"LABELNode1")

        self.LAYOUTNodes.addWidget(self.LABELNode1, 0, 0, 1, 1)

        self.BTNNode1 = QPushButton(self.frame)
        self.BTNNode1.setObjectName(u"BTNNode1")
        run_icon = QIcon()
        run_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'run', 'default.svg'), theme=self.theme)
        run_icon.addFile(run_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNNode1.setIcon(run_icon)
        self.BTNNode1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        self.BTNNode1.setFixedSize(32, 32)

        self.LAYOUTNodes.addWidget(self.BTNNode1, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.LAYOUTNodes)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.LAYOUTLanchers = QGridLayout()
        self.LAYOUTLanchers.setObjectName(u"LAYOUTLanchers")
        self.LABELLaunch1 = QLabel(self.frame)
        self.LABELLaunch1.setObjectName(u"LABELLaunch1")

        self.LAYOUTLanchers.addWidget(self.LABELLaunch1, 0, 0, 1, 1)

        self.BTNLaunch1 = QPushButton(self.frame)
        self.BTNLaunch1.setObjectName(u"BTNLaunch1")
        self.BTNLaunch1.setIcon(run_icon)
        self.BTNLaunch1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        self.BTNLaunch1.setFixedSize(32, 32)

        self.LAYOUTLanchers.addWidget(self.BTNLaunch1, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.LAYOUTLanchers)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.line_4 = QFrame(self.frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.LAYOUTTopic1 = QHBoxLayout()
        self.LAYOUTTopic1.setObjectName(u"LAYOUTTopic1")
        self.LABELTopic1 = QLabel(self.frame)
        self.LABELTopic1.setObjectName(u"LABELTopic1")

        self.LAYOUTTopic1.addWidget(self.LABELTopic1)

        self.BTNECHOTopic1 = QPushButton(self.frame)
        self.BTNECHOTopic1.setObjectName(u"BTNECHOTopic1")
        down_icon = QIcon()
        down_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'arrows', 'down.svg'), theme=self.theme)
        down_icon.addFile(down_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNECHOTopic1.setIcon(down_icon)
        self.BTNECHOTopic1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        self.BTNECHOTopic1.setFixedSize(32, 32)

        self.LAYOUTTopic1.addWidget(self.BTNECHOTopic1)

        self.BTNPUBTopic1 = QPushButton(self.frame)
        self.BTNPUBTopic1.setObjectName(u"BTNPUBTopic1")
        up_icon = QIcon()
        up_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'arrows', 'up.svg'), theme=self.theme)
        up_icon.addFile(up_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNPUBTopic1.setIcon(up_icon)
        self.BTNPUBTopic1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 
        self.BTNPUBTopic1.setFixedSize(32, 32)

        self.LAYOUTTopic1.addWidget(self.BTNPUBTopic1)


        self.verticalLayout_2.addLayout(self.LAYOUTTopic1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.line_5 = QFrame(self.frame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_5)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.EDITType = QLineEdit(self.tab)
        self.EDITType.setObjectName(u"EDITType")

        self.horizontalLayout_2.addWidget(self.EDITType)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.EDITPub = QPlainTextEdit(self.tab)
        self.EDITPub.setObjectName(u"EDITPub")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.EDITPub.sizePolicy().hasHeightForWidth())
        self.EDITPub.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.EDITPub)

        self.BTNSend = QPushButton(self.tab)
        self.BTNSend.setObjectName(u"BTNSend")
        sync_icon = QIcon()
        sync_icon_path = _resolve_icon(self.icon_dirs, os.path.join('icons', 'synchronize', 'default.svg'), theme=self.theme)
        sync_icon.addFile(sync_icon_path, QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BTNSend.setIcon(sync_icon)
        self.BTNSend.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        self.verticalLayout_4.addWidget(self.BTNSend)
        

        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_4.addWidget(self.textEdit)
        self.LABELInfo = QLabel(self.tab)
        self.LABELInfo.setObjectName(u"LABELInfo")
        self.LABELInfo.setProperty('role', 'info_label')
        self.LABELInfo.setProperty('variant', 'default')
        self.LABELInfo.setProperty('state', 'normal')

        self.verticalLayout_4.addWidget(self.LABELInfo)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_3.addWidget(self.frame)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"RQT2 IDE", None))
        self.BTNROSCLean.setText(QCoreApplication.translate("Widget", u"Limpiar", None))
        self.BTNROSColcon.setText(QCoreApplication.translate("Widget", u"Compilar", None))
        self.BTNROSBag.setText(QCoreApplication.translate("Widget", u"Grabar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Tipo de mensaje", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"Nodos", None))
        self.LABELNode1.setText(QCoreApplication.translate("Widget", u"my_publisher", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Lanzadores", None))
        self.LABELLaunch1.setText(QCoreApplication.translate("Widget", u"my_launch.yml", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Topicos", None))
        self.LABELTopic1.setText(QCoreApplication.translate("Widget", u"/topic1", None))
        self.LABELInfo.setText(QCoreApplication.translate("Widget", u"Bandwidth: 0 B/s \t\tPublicadores: 0\nFrecuencia: 0 hz\t\tSuscriptores: 0\nTipo: none", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Tab 1", None))
        self.BTNSend.setText(QCoreApplication.translate("Widget", u"Enviar", None))
    # retranslateUi