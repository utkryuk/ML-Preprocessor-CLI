import pandas as pd
from data_description import DataDescription
class FeatureScaling:
    
    tasks = [
        "\n1. Normalization",
        "2. Show the Dataset"
    ]
    def __init__(self, data):
        self.data = data

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
                break

            elif choice == 2:
                DataDescription.showDataset(self)

            else:
                print("\nYou pressed the wrong key!! Try again..")
        
        return self.data
