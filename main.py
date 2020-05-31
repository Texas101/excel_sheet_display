import pandas as pd

excel_file = 'name.xlsx'
#name = pd.read_excel(excel_file)
#name.head()
#name_sheet1 = pd.read_excel(excel_file)
#name_sheet1.head()
#name_sheet2 = pd.read_excel(excel_file, sheetname=1, index_col=0)
#name_sheet2.head()

xlsx = pd.ExcelFile(excel_file)
numbers_sheets = []
for sheet in xlsx.sheet_names:
    numbers_sheets.append(xlsx.parse(sheet))
numbers = pd.concat(numbers_sheets)
print(numbers)
