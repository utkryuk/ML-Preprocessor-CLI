import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import DataDescription

class Categorical:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    
    tasks = [
        '\n1. Show Categorical Columns',
        '2. Performing One Hot encoding',
        '3. Show the Dataset'
    ]
    def __init__(self, data):
        self.data = data

    def categoricalColumn(self):
        print('\n{0: <20}'.format("Categorical Column") + '{0: <5}'.format("Unique Values"))
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column) + '{0: <5}'.format(self.data[column].nunique()))


    def encoding(self):
        categorical_columns = self.data.select_dtypes(include="object")
        while(1):
            column = input("\nWhich column would you like to one hot encode? (Provide the name with correct case)(Press 0 to go back)  ")
            if column == "0":
                break
            if column in categorical_columns:
            # labelencoder_obj = LabelEncoder()
            # self.data[column] = labelencoder_obj.fit_transform(self.data[column])
            # onehotencoder = OneHotEncoder(categorical_features =[column])
            # print(self.data[column])
                self.data = pd.get_dummies(data=self.data, columns = [column])
                print("Encoding is done.......\U0001F601")
                
                choice = input("Are there more columns to be encoded?(y/n)  ")
                if choice == "y" or choice == "Y":
                    continue
                else:
                    self.categoricalColumn()
                    break
            else:
                print("Wrong Column Name.... Try Again...")


    def categoricalMain(self):
        while(1):
            print("\nTasks\U0001F447")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press 0 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....")
                    continue
                break

            if choice == 0:
                break
            
            elif choice == 1:
                self.categoricalColumn()

            elif choice == 2:
                self.categoricalColumn()
                self.encoding()

            elif choice == 3:
                DataDescription.showDataset(self)

            else:
                print("\nWrong Integer value!! Try again..")
        
        return self.data
