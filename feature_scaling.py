import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    
    tasks = [
        "\n1. Perform Normalization(MinMax Scaler)",
        "2. Perform Standardization(Standard Scaler)",
        "3. Show the Dataset"
    ]
    
    tasks_normalization = [
        "\n1. Normalize a specific Column",
        "2. Normalize the whole Dataset",
        "3. Show the Dataset"
    ]

    tasks_standardization = [
        "\n1. Standardize a specific Column",
        "2. Standardize the whole Dataset",
        "3. Show the Dataset"
    ]

    def __init__(self, data):
        self.data = data
    
    def normalization(self):
        while(1):
            for task in self.tasks_normalization:
                print(task)
            choice = int(input("\nEnter your choice : (Press 0 to go back)  "))

            if choice == 0:
                break
            
            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the columns you want to normalize (With correct case): ")
                for column in columns.split(" "):
                    try:
                        minValue = self.data[column].min()
                        maxValue = self.data[column].max()
                        self.data[column] = (self.data[column] - minValue)/(maxValue - minValue)
                    except:
                        print("\nString Columns are present. So, NOT possible.\nYou can try the first option though.")
                    

            elif choice == 2:
                try:
                    self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                except:
                    print("\nString Columns are present. So, NOT possible.\nYou can try the first option though.")
                
            elif choice==3:
                DataDescription.showDataset(self)

            else:
                print("\nYou pressed the wrong key!! Try again..")

        return


    def standardization(self):
        while(1):
            for task in self.tasks_standardization:
                print(task)
            choice = int(input("\nEnter your choice : (Press 0 to go back)  "))

            if choice == 0:
                break

            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the columns you want to standardize (With correct case): ")
                for column in columns.split(" "):
                    try:
                        mean = self.data[column].mean()
                        standard_deviation = self.data[column].std()
                        self.data[column] = (self.data[column] - mean)/(standard_deviation)
                    except:
                        print("\nString Columns are present. So, NOT possible.\nYou can try the first option though.")
                    
            
            elif choice == 2:
                try:
                    self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
                except:
                    print("\nString Columns are present. So, NOT possible.\nYou can try the first option though.")
                break

            elif choice==3:
                DataDescription.showDataset(self)

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