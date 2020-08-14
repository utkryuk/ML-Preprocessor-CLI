from data_description import DataDescription
from data_input import DataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling

class Preprocessor:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"
    
    # The Task associated with this class. This is also the main class of the project.
    tasks = [
        '1. Data Description',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = 0
    
    def __init__(self):
        self.data = DataInput().inputFunction()
        print("\n\n" + self.bold_start + "WELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\N{grinning face}" + self.bold_end + "\n\n")

    # function to remove the target column of the DataFrame.
    def removeTargetColumn(self):
        print("Columns\U0001F447\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        
        while(1):
            column = input("\nWhich is the target variable:(Press -1 to exit)  ").lower()
            if column == "-1":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                try:
                    self.data.drop([column], axis = 1, inplace = True)
                except KeyError:
                    print("No column present with this name. Try again......\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Try again with the correct column name...\U0001F974")
        return
    
    def printData(self):
        print(self.data)

    # main function of the Preprocessor class.
    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nTasks (Preprocessing)\U0001F447\n")
            for task in self.tasks:
                print(task)

            while(1):
                try:
                    choice = int(input("\nWhat do you want to do? (Press -1 to exit):  "))
                except ValueError:
                    print("Integer Value required. Try again.....\U0001F974")
                    continue
                break

            if choice == -1:
                exit()

            # moves the control into the DataDescription class.
            elif choice==1:
                DataDescription(self.data).describe()


            # moves the control into the Imputation class.
            elif choice==2:
                self.data = Imputation(self.data).imputer()
                

            # moves the control into the Categorical class.
            elif choice==3:
                self.data = Categorical(self.data).categoricalMain()


            # moves the control into the FeatureScaling class.
            elif choice==4:
                self.data = FeatureScaling(self.data).scaling()


            # moves the control into the Download class.
            elif choice==5:
                Download(self.data).download()
            
            else:
                print("\nWrong Integer value!! Try again..\U0001F974")

# obj is the object of our Preprocessor class(main class).
obj = Preprocessor()
# the object 'obj' calls the main function of our Preprocessor class.
obj.preprocessorMain()