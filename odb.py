"""
MIT License

Copyright (c) 2021 nojd11

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
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
