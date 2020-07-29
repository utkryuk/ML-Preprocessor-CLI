import sys
import pandas as pd
# argv.py
class dataInput:
    def Input(self):
        try:
            filename = sys.argv[1]
        except IndexError:
            raise SystemExit(f"Provide the dataset's name")


        try:
            train = pd.read_csv(filename)
        except pd.errors.EmptyDataError:
            raise SystemExit(f"The file is empty")

        # print(train)
        return train