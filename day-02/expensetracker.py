import json
from json import JSONDecodeError

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QComboBox,
    QLabel,
    QMessageBox
)


def load_data():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return []


def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


def refresh_list():
    expense_list.clear()

    total = 0

    for expense in expenses:
        expense_list.addItem(
            f"{expense['title']} | Rs.{expense['amount']} | {expense['category']}"
        )
        total += expense["amount"]

    total_label.setText(f"Total: Rs.{total}")


def add_expense():
    title = title_input.text().strip()
    amount = amount_input.text().strip()
    category = category_box.currentText()

    if not title:
        QMessageBox.warning(window, "Error", "Enter a title")
        return

    try:
        amount = float(amount)
    except ValueError:
        QMessageBox.warning(window, "Error", "Amount must be numeric")
        return

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category
    })

    save_data()
    refresh_list()

    title_input.clear()
    amount_input.clear()


def delete_expense():
    row = expense_list.currentRow()

    if row == -1:
        return

    expenses.pop(row)

    save_data()
    refresh_list()


app = QApplication([])

window = QWidget()
window.setWindowTitle("Expense Tracker")

main_layout = QVBoxLayout(window)

title_input = QLineEdit()
title_input.setPlaceholderText("Title")

amount_input = QLineEdit()
amount_input.setPlaceholderText("Amount")

category_box = QComboBox()
category_box.addItems([
    "Food",
    "Travel",
    "Study",
    "Other"
])

add_button = QPushButton("Add Expense")
delete_button = QPushButton("Delete Selected")

expense_list = QListWidget()

total_label = QLabel("Total: Rs.0")

main_layout.addWidget(title_input)
main_layout.addWidget(amount_input)
main_layout.addWidget(category_box)
main_layout.addWidget(add_button)
main_layout.addWidget(delete_button)
main_layout.addWidget(expense_list)
main_layout.addWidget(total_label)

expenses = load_data()

refresh_list()

add_button.clicked.connect(add_expense)
delete_button.clicked.connect(delete_expense)

window.show()
app.exec()