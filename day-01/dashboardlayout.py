from PySide6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel
)

from PySide6.QtCore import Qt

# Initialize App and Window
app = QApplication([])
window = QWidget()

# Sidebar Options
home = QPushButton("Home")
profile = QPushButton("Profile")
settings = QPushButton("Settings")

# Sidebar
sidebar = QVBoxLayout()
sidebar.addWidget(home)
sidebar.addWidget(profile)
sidebar.addWidget(settings)
sidebar.addStretch()

# Main Content
content_label = QLabel("Welcome")

main = QHBoxLayout()

main.addLayout(sidebar,1)
main.addWidget(content_label, 4, alignment=Qt.AlignCenter)

window.setLayout(main)

window.resize(700, 400)
window.show()

app.exec()
