import random

from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class Sudoku(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('sudoku.ui', None)
        self.ui.show()

        self.ui.newgame_btn.clicked.connect(self.newGame)
        self.ui.playagain_btn.clicked.connect(self.playAgain)
        self.ui.check_btn.clicked.connect(self.checkGame)
        self.ui.dark_btn.clicked.connect(self.darkMode)

        self.game = [[None for i in range(9)] for j in range(9)]
        self.empty_cell = []
        self.wrong_cell = []
        self.flag_for_dark_mode = False

        for i in range(9):
            for j in range(9):
                line_edit = QLineEdit()
                line_edit.setAlignment(Qt.AlignCenter)
                line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                line_edit.setStyleSheet('font-size: 26px')
                self.game[i][j] = line_edit
                self.game[i][j].textChanged.connect(self.checkGame)
                self.ui.grid_layout.addWidget(line_edit, i, j)

    def darkMode(self):
        if self.ui.dark_btn.text() == 'Dark Mode':
            self.ui.setStyleSheet('color: white; background-color: rgb(150, 150, 150)')
            self.ui.dark_btn.setText('Light Mode')
            for item in self.empty_cell:
                row = item['row']
                col = item['col']
                self.game[row][col].setStyleSheet('font-size: 26px; color: blue; background-color: rgb(150, 150, 150)')
            self.flag_for_dark_mode = True
        else:
            self.ui.setStyleSheet('default')
            self.ui.dark_btn.setText('Dark Mode')
            for item in self.empty_cell:
                row = item['row']
                col = item['col']
                self.game[row][col].setStyleSheet('font-size: 26px; color: blue; background-color: white')
            self.flag_for_dark_mode = False
    
    def checkGame(self):
        flag_for_win = True

        if self.flag_for_dark_mode:
            for item in self.empty_cell:
                row = item['row']
                col = item['col']
                self.game[row][col].setStyleSheet('font-size: 26px; color: blue; background-color: rgb(150, 150, 150)')

        #     # for item in self.wrong_cell:
        #     #     item.setStyleSheet('font-size: 26px; color: blue; background-color: rgb(150, 150, 150)')
        else:
            for item in self.empty_cell:
                row = item['row']
                col = item['col']
                self.game[row][col].setStyleSheet('font-size: 26px; color: blue; background-color: white')

            # for item in self.wrong_cell:
            #     item.setStyleSheet('font-size: 26px; color: blue; background-color: white')
        self.wrong_cell.clear()

        for row in range(9):
            for i in range(9):
                for j in range(9):
                    for k in range(len(self.empty_cell)):
                        if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][j].text() != '' and row == self.empty_cell[k]['row'] and i == self.empty_cell[k]['col']:
                            self.game[row][i].setStyleSheet('font-size: 26px; color: blue; background-color: pink')
                            self.wrong_cell.append(self.game[row][i])
                            flag_for_win = False

        for col in range(9):
            for i in range(9):
                for j in range(9):
                    for k in range(len(self.empty_cell)):
                        if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '' and col == self.empty_cell[k]['col'] and i == self.empty_cell[k]['row']:
                            self.game[i][col].setStyleSheet('font-size: 26px; color: blue; background-color: pink')
                            self.wrong_cell.append(self.game[i][col])
                            flag_for_win = False
        
        cell_1 = []
        for i in range(0, 3):
            for j in range(0, 3):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_1.append(dict)
        
        cell_2 = []
        for i in range(0, 3):
            for j in range(3, 6):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_2.append(dict)
        
        cell_3 = []
        for i in range(0, 3):
            for j in range(6, 9):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_3.append(dict)
        
        cell_4 = []
        for i in range(3, 6):
            for j in range(0, 3):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_4.append(dict)
        
        cell_5 = []
        for i in range(3, 6):
            for j in range(3, 6):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_5.append(dict)
        
        cell_6 = []
        for i in range(3, 6):
            for j in range(6, 9):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_6.append(dict)
        
        cell_7 = []
        for i in range(6, 9):
            for j in range(0, 3):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_7.append(dict)

        cell_8 = []
        for i in range(6, 9):
            for j in range(3, 6):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_8.append(dict)
        
        cell_9 = []
        for i in range(6, 9):
            for j in range(6, 9):
                dict = {}
                dict['text'] = self.game[i][j].text()
                dict['row'] = i
                dict['col'] = j
                cell_9.append(dict)

        all_cell = [cell_1, cell_2, cell_3, cell_4, cell_5, cell_6, cell_7, cell_8, cell_9]

        for i in range(9):
            for j in range(9):
                for k in range(9):
                    row = all_cell[i][j]['row']
                    col = all_cell[i][j]['col']
                    for z in range(len(self.empty_cell)):
                        if all_cell[i][j]['text'] == all_cell[i][k]['text'] and j != k and all_cell[i][j]['text'] != '' and self.empty_cell[z]['row'] == row and self.empty_cell[z]['col'] == col:
                            self.game[row][col].setStyleSheet('font-size: 26px; color: blue; background-color: pink')
                            self.wrong_cell.append(self.game[row][col])
                            flag_for_win = False
        
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    flag_for_win = False
                    break
        
        if flag_for_win:
            message = QMessageBox(text= 'Nice, You Win, Press New Game')
            message.exec()
            
    def newGame(self):
        try:
            self.empty_cell.clear()

            for i in range(9):
                for j in range(9):
                    self.game[i][j].setText('')
                    self.game[i][j].setStyleSheet('font: 26px')
                    self.game[i][j].setReadOnly(False)

            rand_choice = random.randint(1, 6)
            myfile = open(f'data/s{rand_choice}.txt', 'r')
            data = myfile.read()
            data = data.split('\n')

            for i in range(9):
                numbers = data[i].split(' ')
                for j in range(9):
                    if numbers[j] == '0':
                        self.game[i][j].setText('')
                        self.game[i][j].setStyleSheet('font-size: 26px; color: blue')
                        dict = {'row' : i, 'col' : j}
                        self.empty_cell.append(dict)
                        
                    else:
                        self.game[i][j].setText(str(numbers[j]))
                        self.game[i][j].setReadOnly(True)
        except:
            message = QMessageBox(text= "Can't load the file, Try again")
            message.exec()

    def playAgain(self):
        for i in range(len(self.empty_cell)):
            row = self.empty_cell[i]['row']
            col = self.empty_cell[i]['col']
            self.game[row][col].setText('')
            self.game[row][col].setStyleSheet('font-size: 26px')   

app = QApplication([])
window = Sudoku()
app.exec()