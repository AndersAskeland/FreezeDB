from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from PySide6.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtChart Pie Chart")
        self.setGeometry(100,100, 1280,600)

        self.show()

        self.create_piechart()



    def create_piechart(self):

        series = QPieSeries()
        series.append("Python", 80)
        series.append("C++", 70)
        series.append("Java", 50)
        series.append("C#", 40)
        series.append("PHP", 30)



        #adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)




        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart Example")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())