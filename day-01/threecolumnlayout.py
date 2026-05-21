from PySide6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel
)

from PySide6.QtCore import Qt

app = QApplication([])
window = QWidget()

# Initialize Menu Items
home = QPushButton("Home")
messages = QPushButton("Messages")
discover = QPushButton("Discover")
settings = QPushButton("Settings")

sidebar = QVBoxLayout()
sidebar.addWidget(home)
sidebar.addWidget(messages)
sidebar.addWidget(discover)
sidebar.addWidget(settings)
sidebar.addStretch()

content = QLabel("Content Here")

details = QLabel("Details Here")

display = QHBoxLayout()
display.addLayout(sidebar)
display.addWidget(content, stretch=3, alignment=Qt.AlignCenter)
display.addWidget(details, alignment=Qt.AlignCenter)

window.setLayout(display)
window.resize(500, 500)
window.show()

app.exec()

