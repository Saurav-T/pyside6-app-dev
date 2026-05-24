import sys

import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget"  

from PySide6.QtWidgets import QApplication, QMainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import vtk

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VTK Viewer - macOS Fixed")
        self.resize(1200, 800)

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.setCentralWidget(self.vtk_widget)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.15)

        self.render_window = self.vtk_widget.GetRenderWindow()
        self.render_window.AddRenderer(self.renderer)

        self.interactor = self.render_window.GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.create_scene()

    def create_scene(self):
        cube = vtk.vtkCubeSource()
        cube.SetXLength(2)
        cube.SetYLength(2)
        cube.SetZLength(2)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(cube.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor(0.9, 0.4, 0.3)
        actor.GetProperty().SetOpacity(1.0)

        self.renderer.AddActor(actor)

        light = vtk.vtkLight()
        light.SetPosition(5, 5, 10)
        light.SetFocalPoint(0, 0, 0)
        self.renderer.AddLight(light)

        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().Zoom(1.2)

    def showEvent(self, event):
        super().showEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    window.vtk_widget.Initialize()
    window.vtk_widget.Start()

    sys.exit(app.exec())