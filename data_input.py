from os import path
import sys
import pandas as pd
# argv.py
class DataInput:
    
    bold_start = "\033[1m"
    bold_end = "\033[0;0m"

    # all extensions supported by this project.
    supported_file_extensions = [
        '.csv',
    ]

    # function to convert all the column names of any specific dataset into lowercase.
    def change_to_lower_case(self, data):
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
        return data

    # function that takes any dataset from the input file and convert it into DataFrame.
    # The print statements are well defined and tells about the state of the errors.
    def inputFunction(self):
        try:
            filename, file_extension = path.splitext(sys.argv[1])
            if file_extension == "":
                raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).\U0001F643")

            if file_extension not in self.supported_file_extensions:
                raise SystemExit(f"This file extension is not " + self.bold_start + "supported.\U0001F643" + self.bold_end)
        
        except IndexError:
            raise SystemExit(f"Provide the " + self.bold_start + "DATASET" + self.bold_end +" name (with extension).\U0001F643")
        
        try:
            data = pd.read_csv(filename+file_extension)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is "+ self.bold_start + "EMPTY" + self.bold_end + "\U0001F635")

        except FileNotFoundError:
            raise SystemExit(f"File " + self.bold_start + "doesn't" + self.bold_end + " exist\U0001F635")

        data = self.change_to_lower_case(data)

        return data
