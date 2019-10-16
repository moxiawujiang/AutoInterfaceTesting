#coding:utf-8
import json

class OperaJson:
    def __init__(self,name):
        try:
            self.file_path='../dataconfig/'+name+'.json'
            with open(self.file_path,'rb')  as f:
                self.data=json.load(f)
        except FileNotFoundError:
            raise


    def get_json_data(self,key):
        try:
            return self.data[key]
        except KeyError:
            raise


    def create_json_data(self,key,value):
        try:
            self.data[key]=value
            with open(self.file_path,'w') as f:
                json.dump(self.data,f)
        except KeyError:
            raise




if __name__ == '__main__':
    OperaJson("ShopApi").get_json_data('login')
    OperaJson('ShopApi').create_json_data('login2','zhang1')
