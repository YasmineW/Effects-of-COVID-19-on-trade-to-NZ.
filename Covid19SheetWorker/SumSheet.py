import openpyxl as xl
wb = xl.load_workbook("29July2020.xlsx")
source_sheet = wb['Effects-of-COVID-19-on-trade-1-']
target_sheet = wb['Sum']