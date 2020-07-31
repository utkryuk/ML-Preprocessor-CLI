from os import path
import sys
import pandas as pd
# argv.py
class DataInput:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    supported_file_extensions = [
        '.csv',
    ]

    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.argv[1])
            
            if file_extension == "":
                raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).")

            if file_extension not in self.supported_file_extensions:
                raise SystemExit(f"This file extension is not " + self.bold_start + "supported." + self.bold_end)

        except IndexError:
            raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).")
        
        try:
            train = pd.read_csv(filename)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is "+ self.bold_start + "EMPTY" + self.bold_end + "\U0001F635")

        except FileNotFoundError:
            raise SystemExit(f"File " + self.bold_start + "doesn't" + self.bold_end + " exist\U0001F635")

        # print(train)
        return train