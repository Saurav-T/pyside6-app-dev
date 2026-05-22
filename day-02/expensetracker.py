import json
from json import JSONDecodeError

from PySide6.QtWidgets import (
    QApplication, QWidget, 
    QVBoxLayout, QLineEdit, 
    QPushButton, QListWidget,
    QComboBox, QLabel,
    QHBoxLayout
)

def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return []
    
def save_data(data):
    with open("expenses.json", "w") as f:
        return json.dump(data, f, indent=4)

class ExpenseItem(QWidget):
    def __init__(self, data, delete_callback):
        super().__init__()
        self.data = data 
        self.delete_callback = delete_callback

        self.label = QLabel(f"{data['title']} - {data['amount']} {data['category']}")
        self.btn = QPushButton("Delete")

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.btn)
        self.btn.clicked.connect(self.delete_self)

        

app = QApplication([])
window = QWidget()

main = QVBoxLayout()

title_input = QLineEdit()
amount_input = QLineEdit()
category_dropdown = QComboBox()

category_dropdown.addItems(["Food", "Travel", "Study", "Other"])

add_button = QPushButton("Add Expense")

