

import xlrd

import os
config_dir=os.path.dirname(os.path.dirname(__file__))+"/dataconfig/"

class OperaExcel:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path=config_dir+"/test.xlsx"
        else:
            self.file_path=file_path

        self.excel=self.get_excel()

    #打开excel
    def get_excel(self):
        tables=xlrd.open_workbook(self.file_path)
        return tables
    #获取表格sheet名称
    def get_sheet_names(self):
        name_list=self.excel.sheet_names()
        return name_list
    #通过name获取表格对象
    def get_sheet(self,name):
        sheet_data=self.excel.sheet_by_name(name)
        return sheet_data
    #获取行数
    def get_lines(self,name):
        lines=self.get_sheet(name).nrows
        return lines
    # 获取具体的值
    def get_cell(self,row,cell):
        data=self.get_sheet().cell(row,cell).value
        return data
    #获取某个sheet表单中所有数据，key:values的格式
    def get_sheet_data(self,name):
        L=[]
        sheet=self.get_sheet(name)
        lines=sheet.nrows
        cols=sheet.ncols
        for i in  range(2,lines):
            data={}
            for j in  range(cols):
                data[sheet.cell(1,j).value]=sheet.cell(i,j).value
            L.append(data)
        return L

if __name__ == '__main__':
    OperaExcel().get_sheet_data("第一个表格")