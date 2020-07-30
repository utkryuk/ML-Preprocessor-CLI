from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation
from download import Download
from categorical import Categorical
from feature_scaling import FeatureScaling

class Preprocessor:

    tasks = [
        '1. About Data',
        '2. Handling NULL Values',
        '3. Encoding Categorical Data',
        '4. Feature Scaling of the Dataset',
        '5. Download the modified dataset'
    ]

    data = dataInput().Input()
    
    def __init__(self):
        print("\n\nWELCOME TO THE MACHINE LEARNING PREPROCESSOR CLI!!!\n\n")


    def removeTargetColumn(self):
        print("Columns:\n")
        for column in self.data.columns.values:
            print(column, end = "  ")
        
        while(1):
            column = input("\nWhich is the target variable:  ")
            choice = input("Are you sure?(y/n) ")
            if choice=="y" or choice=="Y":
                self.data.drop([column], axis = 1, inplace = True)
                print("Done.......")
                break
            else:
                print("Try again with the correct column name..")
        return
    
    def printData(self):
        print(self.data)

    def preprocessorMain(self):
        self.removeTargetColumn()
        while(1):
            print("\nWhat to do")
            for task in self.tasks:
                print(task)

            choice = int(input("\nEnter your Choice : (Press 0 to go exit)  "))

            if choice == 0:
                exit()

            elif choice==1:
                DataDescription(self.data).describe()

            elif choice==2:
                self.data = Imputation(self.data).imputer()
                
            elif choice==3:
                self.data = Categorical(self.data).categoricalMain()

            elif choice==4:
                self.data = FeatureScaling(self.data).scaling()

            elif choice==5:
                Download(self.data).download()


#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())
obj.preprocessorMain()