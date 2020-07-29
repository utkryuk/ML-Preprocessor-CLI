from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation
class Preprocessor:
    tasks = [
        '1. About Data',
        '2. Removing the null Values',
    ]
    
    inputData = dataInput.Input

    def __init__(self):
        print("Welcome!!!")
    
    def printData(self):
        print(self.inputData())

    def whileLoop(self):
        while(1):
            print("\nWhat to do")
            for task in self.tasks:
                print(task)
            print("\nEnter your Choice : (Press 0 to go back)")
            choice = int(input())
            if choice == 0:
                exit()
            elif choice==1:
                data_obj = DataDescription(self.inputData())
                data_obj.describe()
#                self.printData()
            elif choice==2:
                Imputation(self.inputData())


#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())
obj.whileLoop()