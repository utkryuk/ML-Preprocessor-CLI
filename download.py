import pandas as pd

class Download:

    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    def __init__(self, data):
        self.data = data

    def download(self):
        toBeDownload = {}
        for column in self.data.columns.values:
            toBeDownload[column] = self.data[column]

        newFileName = input("\nEnter the " + self.bold_start +"FILENAME" + self.bold_end +" you want?:  ")       
        newFileName = newFileName + ".csv"
        pd.DataFrame(self.data).to_csv(newFileName, index = False)
        print("Hurray!! It is done....\U0001F601")
        
        if input("Do you want to exit now? (y/n) ") == 'y':
            print("Exiting...\U0001F44B")
            exit()
        else:
            return