from PySide6.QtWidgets import (
    QApplication, QWidget,
    QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout,
    QLabel
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainterPath, QRegion

#Initialize App and Window
app = QApplication([])
window = QWidget()

# Initialize Toolbar Items
profile = QLabel()

pixmap = QPixmap("img.png")
pixmap = pixmap.scaled(20, 20,
    Qt.KeepAspectRatioByExpanding,
    Qt.SmoothTransformation)

profile.setPixmap(pixmap)


# Make Circle Mask
path = QPainterPath()
path.addEllipse(0, 0, 20, 20)

mask = QRegion(path.toFillPolygon().toPolygon())
profile.setMask(mask)

profile.setFixedSize(20, 20)

# Search Bar
search = QLineEdit()
search.setPlaceholderText("Search Anything...")
  
search_button = QPushButton("Search")

toolbar = QHBoxLayout()
toolbar.addWidget(profile)
toolbar.addStretch()
toolbar.addWidget(search)
toolbar.addWidget(search_button)

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

# Content

content = QLabel("Content Here")

content_layout = QHBoxLayout()
content_layout.addLayout(sidebar, stretch=1)
content_layout.addWidget(content, 4, alignment=Qt.AlignCenter)

display = QVBoxLayout()
display.addLayout(toolbar)
display.addLayout(content_layout)

window.setLayout(display)
window.resize(600, 700)
window.show()

app.exec()







