from openpyxl import load_workbook
from config.all_path import get_file_path


def insert_base(file_name, sheet_name, row_value, row_start, num):
    """
    向表格中插入数据
    @param file_name: 文件名
    @param sheet_name: sheet名
    @param row_value: 一行的数据，用列表装起来，里面的元素为函数名
    @param row_start: 开始插入的行号
    @param num: 要插入多少行
    """
    file_path = get_file_path(file_name)
    wb = load_workbook(file_path)
    ws = wb[sheet_name]
    for row in range(row_start, row_start + num + 1):
        for index, value in enumerate(row_value):
            ws.cell(row, index + 1, value())
    file_name_l = file_name.split('.')
    new_file_name = f'{file_name_l[0]}_new.{file_name_l[1]}'
    wb.save(get_file_path(new_file_name))


if __name__ == '__main__':
    def func():
        return 1
    l = [func, func, func, func, func, func, func, func]
    insert_base('批量导入客户.xlsx', '批量邀请客户建档模板', l, 4, 5)
