import sys
import random
import vtk

import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget" 

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D Target Click Game")
        self.resize(1000, 700)

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.setCentralWidget(self.vtk_widget)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.15)

        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()

        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.picker = vtk.vtkPropPicker()

        self.target_actor = None

        self.create_target()
        self.renderer.ResetCamera()

        self.interactor.AddObserver(
            "LeftButtonPressEvent",
            self.on_click
        )

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(1000)

    def create_target(self):
        if self.target_actor:
            self.renderer.RemoveActor(self.target_actor)

        x = random.uniform(-5, 5)
        y = random.uniform(-5, 5)
        z = random.uniform(-5, 5)

        sphere = vtk.vtkSphereSource()
        sphere.SetRadius(0.5)
        sphere.SetCenter(x, y, z)
        sphere.SetThetaResolution(20)
        sphere.SetPhiResolution(20)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(sphere.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        actor.GetProperty().SetColor(1, 0, 0)

        self.target_actor = actor
        self.renderer.AddActor(actor)

        self.vtk_widget.GetRenderWindow().Render()

    def on_click(self, obj, event):
        self.vtk_widget.GetRenderWindow().Render()
        click_pos = self.interactor.GetEventPosition()

        self.picker.Pick(click_pos[0], click_pos[1], 0, self.renderer)

        picked_actor = self.picker.GetActor()

        if picked_actor == self.target_actor:
            print("HIT")
            self.create_target()
        else:
            print("MISS")

    def game_loop(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()

    sys.exit(app.exec())
