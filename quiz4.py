import openpyxl
import openpyxl.utils



def find_smallest():
    excel_file = openpyxl.load_workbook("MAEmplyomentData.xlsx")
    sheet = excel_file.active
    all_rows = sheet.rows

    smallest_row = None
    for row in all_rows:
        if smallest_row is None:
            smallest_row = row
        smallest_row_variable = smallest_row[1].value
        if type (smallest_row_variable) is str:
            smallest_row = row
            continue
        row_variable = row[1].value
        if row_variable < smallest_row_variable:
            smallest_row = row

    name = smallest_row[0].value
    print(f"the row with the smallest variable is {name} ")

find_smallest()