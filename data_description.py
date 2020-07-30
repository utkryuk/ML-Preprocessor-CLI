import pandas as pd
import numpy as np

class DataDescription:

    tasks = [
        '\n1. Print Table',
        '2. Describe a specific Column',
        '3. Show Numeric Properties of Each Column'
    ]

    def __init__(self, data):
        self.data = data

    def showDataset(self):
        print("\nHow many rows(>0) to print?")
        rows = int(input())
        print(self.data.head(rows))
        return


    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end="  ")
    
    def heading(self, _heading):
        underline_byte = b'\xcc\xb2'
        underline = str(underline_byte,'utf-8')
        for x in _heading:
            if x.isspace() == False:
                print(x+underline,end='')
            else:
                print(x,end='')
        print("")
            
    def describe(self):
        while(1):
            for task in self.tasks:
                print(task)

            print("\n\nWhat you want to see? (Press 0 to exit)")
#        self.heading("\nWelcome::")
            taskNo = int(input())
            if taskNo==0:
                break
            
            elif taskNo==1:
                self.showDataset()
            
            elif taskNo==2:
                self.showColumns()
                print("\n\nWhich Column?(Write full name(Don't ignore the case) of the column)")
                describeColumn = input()
                print(self.data[describeColumn].describe())
            
            elif taskNo==3:
                print(self.data.describe())

            else:
                print("You pressed the wrong key. Try again!!")