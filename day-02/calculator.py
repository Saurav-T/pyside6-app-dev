from PySide6.QtWidgets import (
    QApplication, QWidget,
    QGridLayout, QPushButton,
    QLineEdit, QVBoxLayout
)

app = QApplication([])
window = QWidget()

main = QVBoxLayout()
grid = QGridLayout()

display = QLineEdit()
display.setReadOnly(True)

main.addWidget(display)

def add_text(text):
    display.setText(display.text() + text)

def calculate():
    try:
        result = eval(display.text())
        display.setText(str(result))
    except:
        display.setText("Error")

def clear():
    display.clear()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3),
]

for text, row, col in buttons:
    btn = QPushButton(text)
    grid.addWidget(btn, row, col)

    if text == "=":
        btn.clicked.connect(calculate)
    elif text == "C":
        btn.clicked.connect(clear)
    else:
        btn.clicked.connect(lambda _, t=text: add_text(t))

main.addLayout(grid)

window.setLayout(main)
window.show()

app.exec()