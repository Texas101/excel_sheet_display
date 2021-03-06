"""
Author: Tejas Narayanan
Date: 5/31/20
"""
from pathlib import Path
import pandas as pd

excel_file = "name.xlsx"
def check_should_continue(user_input):
    """
    Checks if loop should continue
    :param user_input: input provided by user to command line
    :return: False (don't continue) if user enters "stop" anywhere in their input
    """
    if 'STOP' in user_input.upper():
        return False
    return True

def check_user_entered_filename(user_input):
    if Path(user_input).exists():
        return True
    return False

def check_user_selected_sheetname(user_input):
    if Path(user_input).exists():
        return True
    return False


def print_data_on_sheet(filename, sheetname):
    print(f" {pd.read_excel(in1,in2)}")

def main_loop():
    should_continue = True
    while should_continue:
        try:
            in1 = input("Enter A File Name (stop to exit): ")
            should_continue = check_should_continue(in1)
            filename = ''
            if check_user_entered_filename(in1):
                in1 = 'name.xlsx'
                print(f"file exists! {in1}")

                print(f"Here are the sheets {(pd.ExcelFile(in1).sheet_names)}")
                # do something with filename
                in2 = input("Which sheet would you like to open? ")
                print(f" {pd.read_excel(in1, in2)}")

            else:
                print(f"Invalid file name! {in1}")

            if check_user_selected_sheetname(in1):
                pass
                # print_data_on_sheet(filename_entered, sheetname_entered)
                # print data on sheet
        except ValueError as e:
            print(f"Input not Valid! {e}")
        except TypeError as e:
            print(f"Input not valid - Type Error: {e}")
        except Exception as e:
            print(f"something else went wrong: {e}")

# main_loop()

if __name__ == '__main__':
    print("this is the main function")
    main_loop()

#
#
# should_continue = True
#
# while should_continue:
#     try:
#         in1 = input("Enter A File Name (stop to exit): ")
#         should_continue = check_should_continue(in1)
#         filename = ''
#         if check_user_entered_filename(in1):
#             in1 = 'name.xlsx'
#             print(f"file exists! {in1}")
#
#             print(f"Here are the sheets {(pd.ExcelFile(in1).sheet_names)}")
#             # do something with filename
#             in2 = input("Which sheet would you like to open? ")
#             print(f" {pd.read_excel(in1, in2)}")
#
#         else:
#             print(f"Invalid file name! {in1}")
#
#         if check_user_selected_sheetname(in1):
#             pass
#             # print_data_on_sheet(filename_entered, sheetname_entered)
#             # print data on sheet
#     except ValueError as e:
#         print(f"Input not Valid! {e}")
#     except TypeError as e:
#         print(f"Input not valid - Type Error: {e}")
#     except Exception as e:
#         print(f"something else went wrong: {e}")

    # if check_should_continue(in1):
    #     should_continue = False
    #     print("STOP entered. Program terminating...")

        # if 'STOP' in in1.upper():

    #print(f"input: {in1} upper_input: {in1.upper()}")

print("While loop closeed. Program terminating.")

# dhruv_dict = {'Mariott': 'Large GLobal hotel chain', 'Hilton': 'Great cookies at Doubletree', 'Choice Hotels': "cheap!"}
#
# for key, value in dhruv_dict.items():
#     print(f"key: {key} value: {value}")

# counting = [1,2,3,4,5,6,7,5,1,2,5,4,2,5,4,6,3,2,5]
# new_count = [(1,2) , (3,4), (5,6)]
# for key,value in new_count:
#     print(key)
