from PySide6.QtWidgets import (
    QApplication, QWidget, 
    QVBoxLayout, QLabel, 
    QPushButton)

from PySide6.QtCore import QTimer

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

label = QLabel("0")
start = QPushButton("Start")
stop = QPushButton("Stop")
reset = QPushButton("Reset")

layout.addWidget(label)
layout.addWidget(start)
layout.addWidget(stop)
layout.addWidget(reset)

window.setLayout(layout)

counter = 0
timer = QTimer()

def update():
    global counter
    counter += 1
    label.setText(str(counter))

timer.timeout.connect(update)
timer.setInterval(1000)

def start_timer():
    timer.start()

def stop_timer():
    timer.stop()

def reset_timer():
    global counter
    counter = 0
    label.setText("0")
    timer.stop()

start.clicked.connect(start_timer)
stop.clicked.connect(stop_timer)
reset.clicked.connect(reset_timer)

window.show()
app.exec()