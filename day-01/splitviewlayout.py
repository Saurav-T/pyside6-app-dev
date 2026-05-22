from PySide6.QtWidgets import (
    QApplication, QWidget, 
    QSplitter, QHBoxLayout, 
    QListWidget, QTextEdit)

from PySide6.QtCore import Qt

app = QApplication([])
window = QWidget()

splitter = QSplitter(Qt.Vertical)

menu = QListWidget()
menu.addItems(["Home", "Profile", "Settings"])

content = QTextEdit()

splitter.addWidget(menu)
splitter.addWidget(content)

layout = QHBoxLayout()
layout.addWidget(splitter)

window.setLayout(layout)    
window.resize(800, 500)
window.show()

app.exec()