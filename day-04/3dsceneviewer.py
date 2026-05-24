import sys
import vtk

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout
)

import vtkmodules.qt

vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget"  

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VTK - 3D Scene Viewer")
        self.resize(1000, 700)

        self.vtk_widget = QVTKRenderWindowInteractor(self)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.15)

        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.actor = None

        self.init_ui()
        self.show_cube()

    def init_ui(self):
        container = QWidget()
        layout = QVBoxLayout()

        btn_layout = QHBoxLayout()

        cube_btn = QPushButton("Cube")
        sphere_btn = QPushButton("Sphere")
        cone_btn = QPushButton("Cone")
        reset_btn = QPushButton("Reset Camera")

        cube_btn.clicked.connect(self.show_cube)
        sphere_btn.clicked.connect(self.show_sphere)
        cone_btn.clicked.connect(self.show_cone)
        reset_btn.clicked.connect(self.reset_camera)

        btn_layout.addWidget(cube_btn)
        btn_layout.addWidget(sphere_btn)
        btn_layout.addWidget(cone_btn)
        btn_layout.addWidget(reset_btn)

        layout.addLayout(btn_layout)
        layout.addWidget(self.vtk_widget)

        container.setLayout(layout)
        self.setCentralWidget(container)

    def clear_scene(self):
        if self.actor:
            self.renderer.RemoveActor(self.actor)
            self.actor = None

    def add_actor(self, source):
        self.clear_scene()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)

        self.renderer.AddActor(self.actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

    def show_cube(self):
        cube = vtk.vtkCubeSource()
        cube.SetXLength(2)
        cube.SetYLength(2)
        cube.SetZLength(2)
        self.add_actor(cube)

    def show_sphere(self):
        sphere = vtk.vtkSphereSource()
        sphere.SetRadius(1)
        sphere.SetThetaResolution(32)
        sphere.SetPhiResolution(32)
        self.add_actor(sphere)

    def show_cone(self):
        cone = vtk.vtkConeSource()
        cone.SetHeight(2)
        cone.SetRadius(1)
        cone.SetResolution(32)
        self.add_actor(cone)

    def reset_camera(self):
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())