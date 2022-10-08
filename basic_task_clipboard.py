from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
import json

f = open("data.json")
data = json.load(f)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for task in data["tasks"]:
            button = Button(task["title"], task["content"])
            button.clicked.connect(button.copy)
            layout.addWidget(button)

        self.setLayout(layout)


class Button(QPushButton):
    def __init__(self, title, content):
        super().__init__()
        self.setText(title)
        self.content = content

    def copy(self):
        clipboard = app.clipboard()
        clipboard.clear()
        clipboard.setText(self.content)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
