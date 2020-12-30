from PySide6.QtWidgets import QGraphicsScene, QApplication, QGraphicsView, QGraphicsEllipseItem
from PySide6.QtGui import QColor
import sys, random
from PySide2.QtCharts import QtCharts



app = QApplication(sys.argv)
scene = QGraphicsScene()

data = [100, 20, 40]
total = 0
set_angle = 0
count1 = 0
colours = [QColor(255,255,255), QColor(100,100,100), QColor(0, 0, 0)]
total = sum(data)

# for count in range(len(families)):
#     number = []
#     for count in range(3):
#         number.append(random.randrange(0, 255))
#     colours.append(QColor(number[0],number[1],number[2]))

for section in data:
    # Max span is 5760, so we have to calculate corresponding span angle
    angle = round(float(section*5760)/total)
    ellipse = QGraphicsEllipseItem(0,0,400,400)
    ellipse.setPos(0,0)
    ellipse.setStartAngle(set_angle)
    ellipse.setSpanAngle(angle)
    ellipse.setBrush(colours[count1])
    set_angle += angle
    count1 += 1
    scene.addItem(ellipse)


series = QtCharts.QPieSeries()
series.append('Jane', 1)
series.append('Joe', 2)

chart = QtCharts.QChart()
chart.addSeries(series)
chart.setTitle('Simple piechart example')


view = setCentralWidget(QChartView(chart))
view.show()
app.exec_()

