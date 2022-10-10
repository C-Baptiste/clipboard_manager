from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLineEdit, QInputDialog
import sys
import json

f = open("data.json")
data = json.load(f)


class Window(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for template in data["templates"]:
            button = Button(template["title"], template["content"])
            button.clicked.connect(button.copy)
            layout.addWidget(button)

        # unhidden button
        unhidden_button = QPushButton("unhidden")
        unhidden_button.clicked.connect(self.unhidden)
        layout.addWidget(unhidden_button)

        layout.addStretch()
        self.setLayout(layout)

    def unhidden(self):
        mail, ok = QInputDialog.getText(self, "unhidden", "mail")
        if ok and mail:
            command = f"blabla {mail} blabla"
            clipboard = app.clipboard()
            clipboard.clear()
            clipboard.setText(command)


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
