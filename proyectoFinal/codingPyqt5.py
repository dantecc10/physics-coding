import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
 
class SimpleWindow(QWidget):
    def __init__(self, px, py, lx, ly):
        super().__init__()
 
        # Tamaño de la ventana
        self.px = px
        self.py = py
        # Ubicación de la ventana
        self.lx = lx
        self.ly = ly
        # Configuración de la ventana principal
        self.setWindowTitle('Ejemplo Sencillo de PyQt5')
        self.setGeometry(lx, ly, px, py)
 
        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
 
        # Creación de un botón
        self.button = QPushButton('Presióname', self)
        self.button.setGeometry(50, 20, 180, 40)
        # Conexión del botón a una función
        self.button.clicked.connect(self.show_message)
 
        # Creación de un segundo botón para actualizar la gráfica
        self.update_button = QPushButton('Actualizar Gráfica', self)
        self.update_button.setGeometry(50, 70, 180, 40)
        # Conexión del botón de actualización a una función
        self.update_button.clicked.connect(self.update_graph)
 
        # Agregar los botones al layout
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.update_button)
 
        # Crear y agregar la gráfica al layout
        self.create_plot()
 
    def create_plot(self):
        # Crear una figura de matplotlib
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
 
        # Crear una gráfica de ejemplo
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([0, 1, 2, 3], [0, 1, 4, 9])
        self.canvas.draw()
 
    def update_plot(self, x_data, y_data):
        # Limpiar la gráfica actual
        self.ax.clear()
        # Dibujar la nueva gráfica
        self.ax.plot(x_data, y_data)
        # Redibujar el canvas
        self.canvas.draw()
 
    def show_message(self):
        # Mostrar un cuadro de mensaje
        QMessageBox.information(self, 'Mensaje', '¡Hola, mundo!')
 
    def update_graph(self):
        # Datos nuevos para la gráfica
        x_data = [0, 1, 2, 3, 4]
        y_data = [0, 1, 8, 27, 64]
        self.update_plot(x_data, y_data)
 
app = QApplication(sys.argv)
window = SimpleWindow(580, 580, 100, 100)
window.show()
 
 
# Aquí se llama al método update_plot con los nuevos datos
window.update_plot([1, 1, 1, 1, 1], [10, 20, 15, 25, 30])
 
 
sys.exit(app.exec_())