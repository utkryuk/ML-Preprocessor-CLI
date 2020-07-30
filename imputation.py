import pandas as pd
import numpy as np
from data_description import DataDescription


class Imputation:
    
    tasks = [
        "\n1. Show Null Values",
        "2. Remove Column",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Show the Dataset"
    ]

    def __init__(self, data):
        self.data = data

    def showColumns(self):
        for column in self.data.columns.values:
            print(column, end="  ")
        print("")
        return
    

    def printNullValues(self):
        print("\nNULL values of each column:")
        for column in self.data.columns.values:
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return

    def removeColumn(self):
        self.showColumns()
        column = input("\nWhich column you want to delete?  ")
        choice = input("Are you sure?(y/n) ")
        if choice=="y" or choice=="Y":
            self.data.drop([column], axis = 1, inplace = True)
            print("Done.......")
        else:
            print("Not Deleting then........")
        return

    # def removeRow(self):
    #     print("\nWhich row you want to delete?")
    #     row = input()
    #     print("Are you sure?(y/n)")
    #     if input()=="y":
    #         # self.data = self.data.iloc[row:]
    #         self.data.drop(self.data[row])
    #         # self.data.drop([row], inplace = True)
    #     return


    def fillNullWithMean(self):
        self.showColumns()
        column = input("\nEnter the column's name:  ")
        choice = input("Are you sure? (y/n)  ")
        if choice=="y" or choice=='Y':
            self.data[column] = self.data[column].fillna(self.data[column].mean())
            print("Done......")
        else:
            print("Not changing........")
        return


    def fillNullWithMedian(self):
        self.showColumns()
        column = input("\nEnter the column's name:  ")
        choice = input("Are you sure? (y/n)  ")
        if choice=="y" or choice=='Y':
            self.data[column] = self.data[column].fillna(self.data[column].median())
            print("Done......")
        else:
            print("Not changing........")
        return

    def fillNullWithMode(self):
        self.showColumns()
        column = input("\nEnter the column's name:  ")
        choice = input("Are you sure? (y/n)  ")
        if choice=="y" or choice=='Y':
            self.data[column] = self.data[column].fillna(self.data[column].mean()[0])
            print("Done......")
        else:
            print("Not changing........")
        return


    def imputer(self):
#        self.printNullValues()
        while(1):
            print("\nWhat to do now?")
            for task in self.tasks:
                print(task)
            choice = int(input("\nEnter your Choice : (Press 0 to go back)  "))

            if choice == 0:
                break

            elif choice==1:
                self.printNullValues()

            elif choice==2:
                self.removeColumn()

            # elif choice==3:
            #     self.removeRow()

            elif choice==3:
                self.fillNullWithMean()

            elif choice==4:
                self.fillNullWithMedian()
            
            elif choice==5:
                self.fillNullWithMode()

            elif choice==6:
                DataDescription.showDataset(self)

            else:
                print("\nYou pressed the wrong key!! Try again..")
        
        return self.data