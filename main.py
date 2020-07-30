from data_description import DataDescription
from data_input import dataInput
from imputation import Imputation

class Preprocessor:
    tasks = [
        '1. About Data',
        '2. Handling NULL Values'
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
            print("\nEnter your Choice : (Press 0 to go back)")
            choice = int(input())
            if choice == 0:
                exit()
            elif choice==1:
                data_obj = DataDescription(self.data)
                data_obj.describe()
#                self.printData()
            elif choice==2:
                imputation_obj = Imputation(self.data)
                imputation_obj.whileLoop()

#if __name__ == "__main__ ":
obj = Preprocessor()
# print(obj.inputData())
#print(obj.printData())
obj.whileLoop()