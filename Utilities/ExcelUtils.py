import openpyxl


class ExcelUtils:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_cell_data(self, sheet_name, row, column):
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook[sheet_name]
        return sheet.cell(row=row, column=column).value