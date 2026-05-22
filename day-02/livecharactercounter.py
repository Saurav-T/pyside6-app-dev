from PySide6.QtWidgets import (
    QApplication, QWidget, 
    QVBoxLayout, QLineEdit, 
    QPushButton, QListWidget,
    QLabel
    )

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()

input_box = QLineEdit()
counter_label = QLabel("0 Characters")

def update_count(text):
    counter_label.setText(f"{len(text)} characters")

input_box.textChanged.connect(update_count)

layout.addWidget(input_box)
layout.addWidget(counter_label)

window.setLayout(layout)
window.show()

app.exec()