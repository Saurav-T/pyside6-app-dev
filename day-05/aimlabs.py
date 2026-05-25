import sys
import vtk
import random
import time

import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget" 

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QWidget,
    QVBoxLayout
)
from PySide6.QtCore import QTimer

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aim Labs Game")
        self.resize(1000, 700)

        self.score = 0
        self.misses = 0
        self.reaction_times = []

        self.label = QLabel("Score: 0 | Misses: 0 | Avg RT: 0 ms")
        self.label.setStyleSheet("font-size: 16px; padding: 6px;")

        self.vtk_widget = QVTKRenderWindowInteractor(self)

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.vtk_widget)
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.15)

        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)

        self.interactor = self.render_window.GetInteractor()

        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.picker = vtk.vtkPropPicker()

        self.target_actor = None
        self.spawn_time = 0

        self.create_target()

        self.renderer.ResetCamera()   # ✔ ONLY ONCE

        self.interactor.AddObserver("LeftButtonPressEvent", self.on_click)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)

        # ✔ IMPORTANT FOR STABILITY
        self.vtk_widget.Initialize()
        self.render_window.Render()

    def create_target(self):
        if self.target_actor:
            self.renderer.RemoveActor(self.target_actor)

        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-5, 5)

        sphere = vtk.vtkSphereSource()
        sphere.SetRadius(0.4)
        sphere.SetCenter(x, y, z)
        sphere.SetThetaResolution(20)
        sphere.SetPhiResolution(20)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(1, 0.2, 0.2)

        self.target_actor = actor
        self.renderer.AddActor(actor)

        self.render_window.Render()

        self.spawn_time = time.perf_counter()

    def on_click(self, obj, event):
        self.render_window.Render()
        
        click_pos = self.interactor.GetEventPosition()

        self.picker.Pick(click_pos[0], click_pos[1], 0, self.renderer)

        picked = self.picker.GetActor()

        if picked == self.target_actor:
            rt = time.perf_counter() - self.spawn_time

            self.score += 1
            self.reaction_times.append(rt)

            print(f"HIT | RT: {rt: .3f}s")

            self.create_target()

        else:
            self.misses += 1
            print("MISS")

        self.update_ui()

    def update_ui(self):
        avg_rt = (
            sum(self.reaction_times) / len(self.reaction_times)
            if self.reaction_times else 0
        )

        self.label.setText(
            f"Score: {self.score} | Misses: {self.misses} | Avg RT: {avg_rt*1000:.0f} ms"
        )
    
    def update_game(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = GameWindow()
    window.show()

    sys.exit(app.exec())






