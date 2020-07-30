import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    
    tasks = [
        "\n1. Perform Normalization",
        "2. Perform Standardization"
        "3. Show the Dataset"
    ]
    
    tasks_normalization = [
        "\n1. Normalize a specific Column",
        "2. Normalize the whole Dataset"
    ]

    tasks_standardization = [
        "\n1. Standardize a specific Column",
        "2. Standardize the whole Dataset"
    ]

    def __init__(self, data):
        self.data = data
    
    def normalization(self):
        while(1):
            for task in self.tasks_standardization:
                print(task)
            choice = int(input("\nEnter your choice : (Press 0 to go back)  "))

            if choice == 0:
                break
            
            elif choice == 1:
                break

            elif choice == 2:
                break

            else:
                print("\nYou pressed the wrong key!! Try again..")

        return


    def standardization(self):
        while(1):
            for task in self.tasks_normalization:
                print(task)
            choice = int(input("\nEnter your choice : (Press 0 to go back)  "))

            if choice == 0:
                break

            elif choice == 1:
                break
            
            elif choice == 2:
                break

            else:
                print("\nYou pressed the wrong key!! Try again..")

        return


    def scaling(self):
        # self.categoricalColumn()
        while(1):
            print("\nWhat to do now?")
            for task in self.tasks:
                print(task)
            choice = int(input("\nEnter your Choice : (Press 0 to go back)  "))

            if choice == 0:
                break
            
            elif choice == 1:
                self.normalization()

            elif choice == 2:
                self.standardization()

            elif choice==3:
                DataDescription.showDataset(self)
            
            else:
                print("\nYou pressed the wrong key!! Try again..")
        
        return self.data


