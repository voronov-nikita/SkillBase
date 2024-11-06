# Построение графиков в PyQt5

```python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Отображение графика")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QGraphicsView()
        self.setCentralWidget(self.central_widget)

        self.scene = QGraphicsScene()
        self.central_widget.setScene(self.scene)

        self.plot()

    def plot(self):
        pen = Qt.black
        self.scene.addLine(50, 150, 350, 150, pen)
        self.scene.addLine(50, 150, 50, 50, pen)
        self.scene.addLine(50, 50, 350, 50, pen)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


```