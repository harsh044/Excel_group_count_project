# Need install pandas package command are follow 
# pip install pandas
import pandas as pd

def digitalxc_automation():
    try:
        file = "./coding_test.xlsx" # Set your file according your file path
        column_name = "Assignment group" # Set your column name according to your excel file
        code_test = pd.read_excel(file) 
        group_count = code_test[column_name].value_counts() 
        group_dict = group_count.to_dict()

        new_Group_Count = pd.DataFrame(list(group_dict.items()), columns=['Group_Name', 'Number of occurrences'])

        with pd.ExcelWriter(file,mode="a", engine="openpyxl",if_sheet_exists="replace") as writer:
            #Write a new sheet in existing excel file
            new_Group_Count.to_excel(writer, sheet_name="GroupCount",index=False)

    except Exception as e:
        raise e

if __name__=="__main__":
    digitalxc_automation()