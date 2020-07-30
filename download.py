import pandas as pd

class Download:
    def __init__(self, data):
        self.data = data

    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input("\nEnter the filename you want?:  ")       
        newFileName = newFileName + ".csv"
        pd.DataFrame(self.data).to_csv(newFileName, index = False)
        print("Hurray!! It is done")
        
        if input("Do you want to exit now? (y/n) ") == 'y':
            print("Exiting...")
            exit()
        else:
            return