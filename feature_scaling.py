import pandas as pd
from data_description import DataDescription
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # All the Tasks associated with this class.
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
    
    # Performs Normalization on specific column or on whole dataset.
    def normalization(self):
        while(1):
            print("\nTasks (Normalization)\U0001F447")
            for task in self.tasks_normalization:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break
    
            if choice == -1:
                break
            
            # Performs normalization on the columns provided.
            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to normalize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    # This is the basic approach to perform MinMax Scaler on a set of data.
                    try:
                        minValue = self.data[column].min()
                        maxValue = self.data[column].max()
                        self.data[column] = (self.data[column] - minValue)/(maxValue - minValue)
                    except:
                        print("\nNot possible....\U0001F636")
                print("Done....\U0001F601")

            # Performs normalization on whole dataset.
            elif choice == 2:
                try:
                    self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                    print("Done.......\U0001F601")

                except:
                    print("\nString Columns are present. So, " + self.bold_start + "NOT" + self.bold_end + " possible.\U0001F636\nYou can try the first option though.")
                
            elif choice==3:
                DataDescription.showDataset(self)

            else:
                print("\nYou pressed the wrong key!! Try again..\U0001F974")

        return

    # Function to perform standardization on specific column(s) or on whole dataset.
    def standardization(self):
        while(1):
            print("\nTasks (Standardization)\U0001F447")
            for task in self.tasks_standardization:
                print(task)

            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....")
                    continue
                break

            if choice == -1:
                break
            
            # This is the basic approach to perform Standard Scaler on a set of data.
            elif choice == 1:
                print(self.data.dtypes)
                columns = input("Enter all the column"+ self.bold_start + "(s)" + self.bold_end + "you want to normalize (Press -1 to go back)  ").lower()
                if columns == "-1":
                    break
                for column in columns.split(" "):
                    try:
                        mean = self.data[column].mean()
                        standard_deviation = self.data[column].std()
                        self.data[column] = (self.data[column] - mean)/(standard_deviation)
                    except:
                        print("\nNot possible....\U0001F636")
                print("Done....\U0001F601")
                    
            # Performing standard scaler on whole dataset.
            elif choice == 2:
                try:
                    self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
                    print("Done.......\U0001F601")
                except:
                    print("\nString Columns are present. So, " + self.bold_start + "NOT" + self.bold_end + " possible.\U0001F636\nYou can try the first option though.")
                break

            elif choice==3:
                DataDescription.showDataset(self)

            else:
                print("\nYou pressed the wrong key!! Try again..\U0001F974")

        return

    # main function of the FeatureScaling Class.
    def scaling(self):
        while(1):
            print("\nTasks (Feature Scaling)\U0001F447")
            for task in self.tasks:
                print(task)
            
            while(1):
                try:
                    choice = int(input(("\n\nWhat you want to do? (Press -1 to go back)  ")))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break
            if choice == -1:
                break
            
            elif choice == 1:
                self.normalization()

            elif choice == 2:
                self.standardization()

            elif choice==3:
                DataDescription.showDataset(self)
            
            else:
                print("\nWrong Integer value!! Try again..\U0001F974")
        # Returns all the changes on the DataFrame.
        return self.data