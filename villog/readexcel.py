'''
    Excel reader module
'''

from dataclasses import dataclass
import pandas
import numpy

@dataclass(slots = False)
class Sheet:
    '''
        Excel sheet
    '''
    name: str
    data: list[list[any]] = []


class ReadExcel:
    '''
        Excel reader class
    '''
    def __init__(self,
                 file_path: str) -> None:
        '''
            Excel reader class

            :param file_path: :class:`str` Excel file's path
        '''
        self.file_path: str = file_path
        self.__sheet_names: list[str] = pandas.ExcelFile(self.file_path).sheet_names
        self.data: list[Sheet] = []
        for sheet_name in self.__sheet_names:
            sheet_data = pandas.read_excel(self.file_path,
                                           sheet_name = sheet_name,
                                           header = None).replace({numpy.nan: None}).values.tolist()
            sheet: Sheet = Sheet(name = sheet_name,
                                 data = sheet_data or [])
            self.data.append(sheet)


    def get_data_by_id(self,
                       sheet_id: str | int ) -> list[list[any]]:
        '''
            Get sheet data by name

            :param sheet_name: :class:`Union(str, int)` Sheet's ID
        '''
        if isinstance(sheet_id, int):
            if sheet_id in range(len(self.data)):
                return self.data[sheet_id]
        if isinstance(sheet_id, str):
            for sheet in self.data:
                if sheet.name == sheet_id:
                    return sheet.data
        return []
