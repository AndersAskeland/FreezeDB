# ----------------------------------------------------------------------------- #
# Title: Custom widgets                                                         #
#                                                                               #
# What: Custom widgets that are incorerated into app.                           #
#                                                                               #
# ----------------------------------------------------------------------------- #


# ------------------------------------------------------------- #
# 1 - Imports                                                   #
# ------------------------------------------------------------- #
''' External packages '''
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QSize, QPoint, QPointF, QRectF, QRect,QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup, Slot, Property, QXmlStreamReader
from PySide2.QtSvg import QSvgGenerator, QSvgRenderer, QSvgWidget
from PySide2.QtWidgets import QCheckBox, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy, QFrame
from PySide2.QtGui import QColor, QBrush, QPaintEvent, QPen, QPainter, QPixmap

''' Local functions '''
from modules.svg import svg_moon, svg_sun

''' Local classes '''

''' Local resources '''

# ------------------------------------------------------------- #
# 2 - Settings/constants                                        #
# ------------------------------------------------------------- #
moon_bytes = bytearray(svg_moon, encoding='utf-8')
sun_bytes = bytearray(svg_sun, encoding='utf-8')


# ------------------------------------------------------------- #
# 3 - Classes                                                   #
# ------------------------------------------------------------- #

# --------------------------- #
# 3.1 - Dark/light toggle     #
# --------------------------- # 
class AnimatedToggle(QCheckBox):

    _transparent_pen = QPen(Qt.transparent)
    _light_grey_pen = QPen(Qt.lightGray)

    def __init__(self,parent=None):
        super().__init__(parent)

        # Colors
        self.color_light = QBrush(QColor("#f5f5f5")) # White
        self.color_dark = QBrush(QColor("#333333")) # Dark

        # Size
        self.setContentsMargins(8, 0, 8, 0)
        self.setMinimumSize(QSize(80, 50))

        # Current handle position
        self._handle_position = 0

        # Animations
        self.animation = QPropertyAnimation(self, b"handle_position", self)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(200)  # time in ms

        # Signal
        self.stateChanged.connect(self.setup_animation)

    def sizeHint(self):
        return QSize(58, 45)

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    @Slot(int)
    def setup_animation(self, value):
        self.animation.stop()
        if value:
            self.animation.setEndValue(1)
        else:
            self.animation.setEndValue(0)
        self.animation.start()

    # Paint event
    def paintEvent(self, e: QPaintEvent):
        # Creates containing rectangle
        contRect = self.contentsRect()
        # print(f"The widget rectangle size: {contRect}") # Debug

        # Sets circle size
        handleRadius = round(0.24 * contRect.height())
        # æprint(f"The handle radius is: {handleRadius}") # Debug

        # Creates a painter event
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        # Creates a pen (transparant) inside painter event - Removes edges
        p.setPen(self._transparent_pen)

        # Creates rectangle
        barRect = QRectF(0, 0, contRect.width(), 0.58 * contRect.height()) # size (x,y,width,height)
        barRect.moveCenter(contRect.center())
        rounding = barRect.height() / 2

        # Define different positions and lengths
        trailLength = contRect.width() - (handleRadius * 2 * 1.2)
        xPos = contRect.x() + handleRadius * 1.2 + (trailLength * self._handle_position)
        yPos = barRect.y() + (barRect.height() / 4.6)  # Get y-position        
        sunPosX = contRect.x() + handleRadius / 2 # Position of sun
        moonPosX = contRect.x() + handleRadius / 2 + trailLength   # Position of moon

        # Icons
        moon = QtGui.QImage.fromData(moon_bytes)
        sun = QtGui.QImage.fromData(sun_bytes)
        icon_moon = QPixmap(moon)
        icon_sun = QPixmap(sun)

    
        # Draw based on states
        if self.isChecked(): # Dark
            p.setBrush(self.color_light) 
            p.drawRoundedRect(barRect, rounding, rounding) # Line
            p.drawPixmap(sunPosX, yPos, handleRadius * 1.5, handleRadius * 1.5, icon_sun) # Icon
            p.setBrush(self.color_dark)
            p.drawEllipse(QPointF(xPos, barRect.center().y()), handleRadius, handleRadius) # Circle

        else: # Light
            p.setBrush(self.color_dark)
            p.drawRoundedRect(barRect, rounding, rounding) # Line
            p.drawPixmap(moonPosX, yPos, handleRadius * 1.5, handleRadius * 1.5, icon_moon) # Icon
            p.setBrush(self.color_light)
            p.drawEllipse(QPointF(xPos, barRect.center().y()), handleRadius, handleRadius) # Circle

        # Close painter
        p.end()

    @Property(float)
    def handle_position(self):
        return self._handle_position

    @handle_position.setter
    def handle_position(self, pos):
        """change the property
        we need to trigger QWidget.update() method, either by:
            1- calling it here [ what we're doing ].
            2- connecting the QPropertyAnimation.valueChanged() signal to it.
        """
        self._handle_position = pos
        self.update()


# --------------------------- #
# 3.2 - Sidebar menu          #
# --------------------------- #
''' TODO '''

# --------------------------- #
# 3.3 - Sidebar setup menu    #
# --------------------------- #
''' Sidebar widget that shows freezeDB logo '''
class SidebarFirstSetup(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        # Widgets inside
        self.logo = QLabel()
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(100, 16777215))
        self.logo.setPixmap(QPixmap(u":/figures/graphics/logo.png"))
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addItem(self.verticalSpacer)

        self.setLayout(layout)

# --------------------------- #
# 3.4 - Select folder         #
# --------------------------- #
class SelectFolder(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.dlg = QFileDialog()
        self.dlg.setLabelText(QFileDialog.Accept, "Select directory")
        self.dlg.setFileMode(QFileDialog.Directory)
        self.dlg.Option.ShowDirsOnly
        self.dlg.Option.HideNameFilterDetails

        if dlg.exec_():
            selected_dir = dlg.selectedFiles()[0]
            print(selected_dir)



# ------------------------------------------------------------- #
# 4 - QT designer classes                                       #
# ------------------------------------------------------------- #
class QCard(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

class QSideBar(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)