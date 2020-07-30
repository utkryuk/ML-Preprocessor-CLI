from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation
from download import Download

class Preprocessor:

    tasks = [
        '1. About Data',
        '2. Handling NULL Values',
        '3. Download the modified dataset'
    ]

    data = dataInput().Input()
    
    def __init__(self):
        print("Welcome!!!")


    # def divideTrain(self):
    #     print("\nSelect Target Variable(Y) from these columns:\n")
    #     for column in self.data.columns.values:
    #         print(column, end="  ")
    #     print("")
        
    
    def printData(self):
        print(self.data)

    def whileLoop(self):
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
                Imputation(self.data).whileLoop()
                
            elif choice==3:
                Download(self.data).download()

#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())
obj.whileLoop()