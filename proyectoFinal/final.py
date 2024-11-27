from matplotlib import pyplot as plt
import numpy as np
import pygame
import imageio
import sys
from scipy.io import loadmat
from scipy.signal import convolve2d
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os

# Clase para la simulación
class Simulation:
    def __init__(self):
        # Parámetros de simulación
        self.Re = 1500
        self.tsim = 1
        self.dt = 1e-5
        self.nt = int(np.round(self.tsim / self.dt))
        self.Lx = 1
        self.Ly = 1
        self.Nx = 1024
        self.Ny = 1024
        self.dx = self.Lx / self.Nx
        self.dy = self.Ly / self.Ny

        # Campos
        self.u = np.zeros((self.Nx + 1, self.Ny + 2))
        self.v = np.zeros((self.Nx + 2, self.Ny + 1))
        self.p = np.zeros((self.Nx, self.Ny))

        # Inicialización de matrices
        self.W_h = np.array([[1], [-2], [1]])
        self.W_v = np.array([[1, -2, 1]])
        self.dvx = np.array([[-1], [1]])
        self.dvy = np.array([[-1, 1]])

        # Cargar datos externos
        try:
            mat = loadmat('msgg.mat')
            self.msgg = mat['msgg']
        except FileNotFoundError:
            print("Error: Archivo 'msgg.mat' no encontrado.")
            self.msgg = np.zeros((self.Nx, self.Ny))

        try:
            self.Ga1 = np.array(plt.imread('Cuerpo_1024.png'))
        except FileNotFoundError:
            print("Error: Archivo 'Cuerpo_1024.png' no encontrado.")
            self.Ga1 = np.zeros((self.Nx, self.Ny, 3))

        # Inicializar cuerpo y flujo
        self.body_u = np.zeros_like(self.u)
        self.body_v = np.zeros_like(self.v)
        if self.Ga1.size > 0:
            self.body_u[1:self.Nx + 1, 1:self.Ny + 1] = self.Ga1[:, :, 0]
            self.body_v[1:self.Nx + 1, 1:self.Ny + 1] = self.Ga1[:, :, 0]

        self.int_jet = 4
        for k1 in range(0, self.Ny + 2):
            self.u[0, k1] = self.int_jet
            self.u[self.Nx, k1] = self.int_jet

        self.frames = []
        self.fps = 60
        self.filename = 'simulacion_pyqt5.mp4'

    def run_step(self, step):
        """Ejecuta un paso de la simulación."""
        if (self.dt * step) > 0:
            for k1 in range(0, self.Ny + 2):
                self.u[0, k1] = self.int_jet
                self.u[self.Nx, k1] = self.int_jet
        else:
            for k1 in range(0, self.Ny + 2):
                self.u[0, k1] = 0
                self.u[self.Nx, k1] = 0

        # Cálculos simplificados de ejemplo
        Lux = convolve2d(self.u[:, 1:self.Ny + 1], self.W_h, mode='valid') / (self.dx * self.dx)
        self.u[1:self.Nx, 1:self.Ny + 1] += self.dt * (-Lux / self.Re)

        # Crear una imagen representativa del campo de velocidad
        min_u = np.min(self.u)
        max_u = np.max(self.u)
        if max_u != min_u:
            u_visual = (self.u[1:-1, 1:-1] - min_u) / (max_u - min_u)
        else:
            u_visual = np.zeros_like(self.u[1:-1, 1:-1])
        u_visual = (u_visual * 255).astype(np.uint8)
        return u_visual

    def save_video(self):
        """Guarda el video generado."""
        if self.frames:
            imageio.mimsave(self.filename, self.frames, fps=self.fps)
            print(f"Video guardado en {self.filename}")
        else:
            print("No hay frames para guardar.")

# Clase de la ventana PyQt5
class SimulationWindow(QWidget):
    def __init__(self, simulation):
        super().__init__()
        self.simulation = simulation
        self.setWindowTitle('Simulación con PyQt5')
        self.setGeometry(100, 100, 800, 600)

        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Botón para iniciar simulación
        self.start_button = QPushButton('Iniciar Simulación', self)
        self.start_button.clicked.connect(self.start_simulation)
        self.layout.addWidget(self.start_button)

        # Botón para guardar video
        self.save_button = QPushButton('Guardar Video', self)
        self.save_button.clicked.connect(self.simulation.save_video)
        self.layout.addWidget(self.save_button)

        # Crear gráfica
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.layout.addWidget(self.canvas)

    def start_simulation(self):
        """Inicia la simulación y actualiza la gráfica."""
        for step in range(self.simulation.nt):
            u_visual = self.simulation.run_step(step)
            if step % 100 == 0:
                self.update_plot(u_visual)
                self.simulation.frames.append(u_visual)

    def update_plot(self, data):
        """Actualiza la gráfica con nuevos datos."""
        self.ax.clear()
        self.ax.imshow(data, cmap='viridis', origin='lower')
        self.canvas.draw()

# Main
if __name__ == '__main__':
    app = QApplication(sys.argv)
    simulation = Simulation()
    window = SimulationWindow(simulation)
    window.show()
    sys.exit(app.exec_())
