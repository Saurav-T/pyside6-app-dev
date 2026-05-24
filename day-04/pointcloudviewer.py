import sys
import vtk
import random

import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget" 

from PySide6.QtWidgets import QApplication, QMainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Point Cloud Viewer")
        self.resize(1000, 700)

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.setCentralWidget(self.vtk_widget)

        self.renderer  = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.12)

        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.create_point_cloud()

    def create_point_cloud(self):
        points = vtk.vtkPoints()

        for _ in range(5000):
            x = random.uniform(-50, 50)
            y = random.uniform(-50, 50)
            z = random.uniform(-10, 30)
            points.InsertNextPoint(x, y, z)

        polydata = vtk.vtkPolyData()
        polydata.SetPoints(points)

        glyph_filter = vtk.vtkVertexGlyphFilter()
        glyph_filter.SetInputData(polydata)
        glyph_filter.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(glyph_filter.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        actor.GetProperty().SetPointSize(3)
        actor.GetProperty().SetColor(0.2, 0.8, 1.0)

        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

        self.vtk_widget.GetRenderWindow().Render()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())


