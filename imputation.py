import pandas as pd
from data_description import DataDescription


class Imputation:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # The Task associated with this class.
    tasks = [
        "\n1. Show number of Null Values",
        "2. Remove Columns",
        "3. Fill Null Values (with mean)",
        "4. Fill Null Values (with median)",
        "5. Fill Null Values (with mode)",
        "6. Show the Dataset"
    ]

    def __init__(self, data):
        self.data = data

    # function to show columns of the DataFrame
    def showColumns(self):
        print("\nColumns\U0001F447\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        return
    
    # function to print the number of NULL values present in each column
    def printNullValues(self):
        print("\nNULL values of each column:")
        for column in self.data.columns.values:
            # isnull checks on each value of a column that whether the value is null or not.
            print('{0: <20}'.format(column) + '{0: <5}'.format(sum(pd.isnull(self.data[column]))))
        print("")
        return

    # function to remove a column from the DataFrame
    def removeColumn(self):
        self.showColumns()
        while(1):
            columns = input("\nEnter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to delete (Press -1 to go back)  ").lower()

            if columns == "-1":
                break

            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    # inplace = True otherwise, the changes won't reflect on the DataFrame.
                    self.data.drop(columns.split(" "), axis = 1, inplace = True)
                except KeyError:
                    print("One or more Columns are not present. Try again.....\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Not Deleting........\U0001F974")
        return

    # function that fills null values with the mean of that column.
    def fillNullWithMean(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].mean())
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    # Imputation is only possible on some specific datatypes like int, float etc.
                    print("The Imputation is not possible here\U0001F974. Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return


    # function that fills null values with the median of that column.
    def fillNullWithMedian(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    self.data[column] = self.data[column].fillna(self.data[column].median())
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    print("The Imputation is not possible here\U0001F974.Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return

    # function that fills null values with the mean of that column.

    # function that fills null values with the mode of that column.
    def fillNullWithMode(self):
        self.showColumns()
        while(1):
            column = input("\nEnter the column name:(Press -1 to go back)  ").lower()
            if column == "-1":
                break
            choice = input("Are you sure? (y/n)  ")
            if choice=="y" or choice=='Y':
                try:
                    # Mode provides us with dataframe so, we will take 1st value(most probable value).
                    # Look into the documentation, if any doubts.
                    self.data[column] = self.data[column].fillna(self.data[column].mode()[0])
                except KeyError:
                    print("Column is not present. Try again.....\U0001F974")
                    continue
                except TypeError:
                    print("The Imputation is not possible here\U0001F974. Try on another column.")
                    continue
                print("Done......\U0001F601")
                break
            else:
                print("Not changing........\U0001F974")
        return

    # main function of the Imputation Class.
    def imputer(self):
        while(1):
            print("\nImputation Tasks\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            if choice == -1:
                break

            elif choice==1:
                self.printNullValues()

            elif choice==2:
                self.removeColumn()

            elif choice==3:
                self.fillNullWithMean()

            elif choice==4:
                self.fillNullWithMedian()
            
            elif choice==5:
                self.fillNullWithMode()

            elif choice==6:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again..\U0001F974")
        return self.data