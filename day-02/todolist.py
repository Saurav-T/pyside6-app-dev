import json
from json import JSONDecodeError

from PySide6.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton,
    QLabel, QCheckBox
)

def load_todos():
    try:
        with open("todos.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        return []

def save_todos(data):
    with open("todos.json", "w") as file:
        json.dump(data, file, indent=4)

class ToDoItem(QWidget):

    def __init__(self, todo, delete_callback):
        super().__init__()

        self.todo = todo
        self.delete_callback = delete_callback

        self.checkbox = QCheckBox()
        self.label = QLabel(todo["task"])
        self.delete = QPushButton("Delete")

        self.delete.clicked.connect(self.handle_delete)

        layout = QHBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.delete)

        self.setLayout(layout)

    def handle_delete(self):
        self.delete_callback(self.todo["id"])

app = QApplication([])
window = QWidget()

main_layout = QVBoxLayout()

task_input = QLineEdit()
add_button = QPushButton("Add Task")

main_layout.addWidget(task_input)
main_layout.addWidget(add_button)

container_widget = QWidget()
container_layout = QVBoxLayout(container_widget)

main_layout.addWidget(container_widget)

def clear_list():
    while container_layout.count():
        item = container_layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()

def display():
    clear_list()

    todos = load_todos()

    for todo in todos:
        item = ToDoItem(todo, delete_task)
        container_layout.addWidget(item)

def add_task():
    task = task_input.text().strip()
    if not task:
        return

    todos = load_todos()

    todos.append({
        "id": len(todos) + 1,
        "task": task,
        "completed": False
    })

    save_todos(todos)
    task_input.clear()
    display()

def delete_task(task_id):
    todos = load_todos()

    todos = [t for t in todos if t["id"] != task_id]

    save_todos(todos)
    display()

add_button.clicked.connect(add_task)

window.setLayout(main_layout)
display()

window.show()
app.exec()