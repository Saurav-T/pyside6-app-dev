from PySide6.QtWidgets import (
    QApplication, QWidget,
    QTabWidget, QVBoxLayout, 
    QLabel, QListWidget,
    QHBoxLayout
    )

from PySide6.QtCore import Qt

app = QApplication([])

window = QWidget()

layout = QHBoxLayout()

list_widget = QListWidget()
list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])

menu = QVBoxLayout()
menu.addWidget(list_widget)

tabs = QTabWidget()
home = QLabel("Home Page", alignment=Qt.AlignCenter)
profile = QLabel("Profile Page", alignment=Qt.AlignCenter)
settings = QLabel("Settings Page", alignment=Qt.AlignCenter)

tabs.addTab(home, "Home")
tabs.addTab(profile, "Profile")
tabs.addTab(settings, "Settings")

layout.addLayout(menu)
layout.addWidget(tabs, stretch=3)

window.setLayout(layout)
window.resize(700, 500)
window.show()

app.exec()



 