import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from data_description import DataDescription

class Categorical:
    
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
            column = input("\nWhich column would you like to one hot encode? (Provide the name with correct case)  ")
            if column in categorical_columns:
            # labelencoder_obj = LabelEncoder()
            # self.data[column] = labelencoder_obj.fit_transform(self.data[column])
            # onehotencoder = OneHotEncoder(categorical_features =[column])
            # print(self.data[column])
                self.data = pd.get_dummies(data=self.data, columns = [column])
                print("Encoding is done.......")
                
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
            print("\nWhat to do now?")
            for task in self.tasks:
                print(task)
            choice = int(input("\nEnter your Choice : (Press 0 to go back)  "))
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
                print("\nYou pressed the wrong key!! Try again..")
        
        return self.data
