from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Color_Picker(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()
        self.ui.sliderblue.valueChanged.connect(self.Blue)
        self.ui.sliderred.valueChanged.connect(self.Red)
        self.ui.slidergreen.valueChanged.connect(self.Green)
        self.ui.green_color_number.setText("0")
        self.ui.red_color_number.setText("0")
        self.ui.blue_color_number.setText("0")
    def Blue(self):
        value=str(self.ui.sliderblue.value())
        self.ui.blue_color_number.setText(value) 
        self.ui.rgb_color.setStyleSheet(f'background-color:rgb({self.ui.sliderred.value()},{self.ui.slidergreen.value()},{value})')  
        self.Background_color()
    def Red(self):
        value=str(self.ui.sliderred.value())
        self.ui.red_color_number.setText(value) 
        self.ui.rgb_color.setStyleSheet(f'background-color:rgb({value},{self.ui.slidergreen.value()},{self.ui.sliderblue.value()})') 
        self.Background_color()
    def Green(self):
        value = str(self.ui.slidergreen.value())
        self.ui.green_color_number.setText(value)
        self.ui.rgb_color.setStyleSheet(f'background-color:rgb({self.ui.sliderred.value()},{value},{self.ui.sliderblue.value()})') 
        self.Background_color()
    def Background_color(self):
        if self.ui.rgb_btn.isChecked():
            self.ui.setStyleSheet(f'background-color:rgb({self.ui.red_color_number.text()},{self.ui.green_color_number.text()},{self.ui.blue_color_number.text()})')
        else:
            self.ui.setStyleSheet("background-color: rgb(255, 255, 255)")

app = QApplication()
window = Color_Picker()
app.exec_()