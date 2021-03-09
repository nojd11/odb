# -*- coding:utf-8 -*-
import json
import os


class DataBase(object):
    def __init__(self, DataFilePath):
        self.DataFilePath = DataFilePath

        if not os.path.exists(DataFilePath):
            print("Error: File Does Not Exist")
            return False
        with open(DataFilePath) as f:
            self.DictData = json.loads(f.read())

        # print(self.__dict__)

    def AddIndex(self, Name):
        if Name in self.DictData:
            print("Error: Index Exist")
            return False

        self.DictData[Name] = []
        return True

    def AddData(self, IndexName, Data):
        if IndexName not in self.DictData:
            print("Error: Index Not Exist")
            return False

        self.DictData[IndexName].append(Data)
        return True

    def DelIndex(self, Index):
        if Index not in self.DictData:
            print("Error: Index Not Exist")
            return False
        elif len(self.DictData[Index]) != 0:
            print("Error: Index Not Null")
            return False

        del self.DictData[Index]
        return True

    def DelData(self, Index, ID):
        if Index not in self.DictData:
            print("Error: Index Not Exist")
            return False

        try:
            del self.DictData[Index][ID]
        except IndexError:
            print("Error: The Data Corresponding To The ID Does Not Exist")
            return False

        return True

    def view(self, Index=None):
        if not Index:
            IndexList = []
            for i in self.DictData:
                IndexList.append(i)
            return IndexList
        return self.DictData[Index]

    def save(self):
        try:
            with open(self.DataFilePath, 'w+') as f:
                f.write(json.dumps(self.DictData))
        except IOError:
            print("Error: Save Error")
            return False
        return True
