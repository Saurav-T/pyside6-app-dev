import random
import vtk
import sys

import vtkmodules.qt
vtkmodules.qt.QVTKRWIBase = "QOpenGLWidget" 

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QVBoxLayout
)

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Point Picker Tool")
        self.resize(1000, 700)

        self.vtk_widget = QVTKRenderWindowInteractor(self)
        self.setCentralWidget(self.vtk_widget)

        self.renderer = vtk.vtkRenderer()
        self.renderer.SetBackground(0.1, 0.1, 0.12)

        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)

        self.interactor = self.vtk_widget.GetRenderWindow().GetInteractor()
        style = vtk.vtkInteractorStyleTrackballCamera()
        self.interactor.SetInteractorStyle(style)

        self.create_points()

        self.picker = vtk.vtkPointPicker()

        self.interactor.AddObserver(
            "LeftButtonPressEvent",
            self.on_left_click
        )

    def create_points(self):
        self.points = vtk.vtkPoints()

        for _ in range(100):
            self.points.InsertNextPoint(
                random.uniform(-10, 10),
                random.uniform(-10, 10),
                random.uniform(-10, 10)
            )
        
        polydata = vtk.vtkPolyData()
        polydata.SetPoints(self.points)

        glyph_filter = vtk.vtkVertexGlyphFilter()
        glyph_filter.SetInputData(polydata)
        glyph_filter.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(glyph_filter.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        actor.GetProperty().SetPointSize(15)
        actor.GetProperty().SetColor(0.2, 0.8, 1.0)

        self.renderer.AddActor(actor)
        self.renderer.ResetCamera()

    def on_left_click(self, obj, event):
        click_x, click_y = self.interactor.GetEventPosition()
        self.picker.Pick(
            click_x,
            click_y,
            0,
            self.renderer
        )

        point_id = self.picker.GetPointId()
        if point_id != -1:
            point = self.points.GetPoint(point_id)

            print(
                f"Point {point_id}: "
                f"X={point[0]:.2f}, "
                f"Y={point[1]:.2f}, "
                f"Z={point[2]:.2f}"
            )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

window.vtk_widget.Initialize()
window.vtk_widget.Start()

sys.exit(app.exec())
