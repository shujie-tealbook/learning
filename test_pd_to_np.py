import pandas as pd
import numpy as np

def add_str(str1, str2):
    return str1 + str2

if __name__ == "__main__":
    # load file into panda df
    gold_data = pd.read_csv("./company_name_golden.csv")

    # Use panda df directly to apply functions
    gold_data['combine'] = gold_data.apply(lambda row : add_str(gold_data["domains"], gold_data["name"]), axis=1)
    print(gold_data['combine'])