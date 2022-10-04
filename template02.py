# pip install pyqt6

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)
import json

app = QApplication([])

window = QWidget()

window.setWindowTitle("Templates")

layout = QGridLayout()

f = open("data.json")
data = json.load(f)

i=0
j=0

def cp():
    cb = app.clipboard()
    cb.clear()
    cb.setText("pas content")

for task in data["tasks"]:
    if j == 5: i += 1; j = 0

    button = QPushButton(task["title"])
    layout.addWidget(button, i, j)

    button.clicked.connect(cp)

    j += 1
    
"""
class Button:

    def __init__(self, title, content):
        self.title = title
        self.content = content       

    def copyToClipboard(self):
        cb = QApplication.clipboard()
        cb.clear()
        cb.setText(self.content)

button.clicked.connect(copyToClipboard)
"""

window.setLayout(layout)

window.show()




sys.exit(app.exec())