import sys
import vtk

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton
)

import vtkmodules.qt

vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget"  

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Control Viewer")
        self.resize(1000, 700)

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        
        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.15)

        self.render_window = self.vtk_widget.GetRenderWindow()

        self.render_window.AddRenderer(self.renderer)
        self.interactor = self.render_window.GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.create_scene()
        self.init_ui()


    def init_ui(self):
        container = QWidget()
        layout = QVBoxLayout()

        btn_layout = QHBoxLayout()

        btn_reset = QPushButton("Reset")
        btn_top = QPushButton("Top")
        btn_front = QPushButton("Front")
        btn_side = QPushButton("Side")
        btn_iso = QPushButton("Isometric")

        btn_reset.clicked.connect(self.reset_view)
        btn_top.clicked.connect(self.top_view)
        btn_front.clicked.connect(self.front_view)
        btn_side.clicked.connect(self.side_view)
        btn_iso.clicked.connect(self.iso_view)

        btn_layout.addWidget(btn_reset)
        btn_layout.addWidget(btn_top)
        btn_layout.addWidget(btn_front)
        btn_layout.addWidget(btn_side)
        btn_layout.addWidget(btn_iso)

        layout.addLayout(btn_layout)
        layout.addWidget(self.vtk_widget)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def reset_view(self):
        self.renderer.ResetCamera()
        self.render_window.Render()

    def top_view(self):
        camera = self.renderer.GetActiveCamera()
        camera.SetPosition(0, 0, 10)
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 1, 0)

        self.render_window.Render()

    def front_view(self):
        camera = self.renderer.GetActiveCamera()
        camera.SetPosition(0, -10, 0)
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 0, 1)

        self.render_window.Render()

    def side_view(self):
        camera = self.renderer.GetActiveCamera()
        camera.SetPosition(10, 0, 0)
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 0, 1)

        self.render_window.Render()

    def iso_view(self):
        camera = self.renderer.GetActiveCamera()
        camera.SetPosition(10, 10, 10)
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 0, 1)

        self.render_window.Render()
    
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
        self.renderer.ResetCamera()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    window.vtk_widget.Initialize()
    window.vtk_widget.Start()

    sys.exit(app.exec())


