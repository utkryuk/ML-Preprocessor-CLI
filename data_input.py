import sys
import pandas as pd
# argv.py
class DataInput:
    def inputFunction(self):
        try:
            filename = sys.argv[1]
        except IndexError:
            raise SystemExit(f"Provide the dataset's name (with extension)")
        
        try:
            train = pd.read_csv(filename)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is empty")

        except FileNotFoundError:
            raise SystemExit(f"File doesn't exist.")

        # print(train)
        return train