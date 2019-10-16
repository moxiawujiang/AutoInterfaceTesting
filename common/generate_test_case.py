#coding:utf-8
from string import Template
from util.opera_excel import OperaExcel
from  util.opera_json import OperaJson
from util.opera_mysql import OperaMysql
from common.base import get_project_path



class GenerateTestCase:

    def __init__(self):
        self.excel=OperaExcel()

    #生成单个测试用例
    def create_single_case(self,sheet_name,information):
        demo=Template('''
    def test_${case_id}_${case_name}(self):
        """${case_description}"""
        url='${url}'
        data=$data
        res=self.s.${method}(url=url,data=data)
        expect ='${expect}'
        logger().info('url:'+'${url}')
        logger().info('data:'+"${data}")
        logger().info('data:'+"${expect}")
        result=res.text
        self.assertIn(expect,result)
        logger().info('result:'+result)
        ''')

        #获取参数
        try:
            if information['data'] == '':
                information['data'] = "None"
            else:
                _data = information['data'].split('.')
                _type=_data.lower()
                if _type=='json':
                    information['data']=OperaJson(sheet_name).get_json_data(information['data'])
                elif _type=='db':
                    sql=OperaJson(sheet_name).get_json_data(information['data'])
                    information['data']=OperaMysql().get_all_db_data(sql)

        except Exception:
            information['data']="获取"+sheet_name+"中"+information['data']+"参数失败"

        string=demo.safe_substitute(information)
        return string

    #生成测试用例集合
    def create_sheet_case(self,sheet_name):
        string=''
        #获取单个sheet中的所有接口数据
        sheet_list=self.excel.get_sheet_data(sheet_name)
        for  data in  sheet_list:
            #循环生成case并拼接为一个字符串
            case=self.create_single_case(sheet_name,data)
            string=string+case
        return string

    #生成单个测试用例集合文件
    def create_single_file(self,sheet_name):
        #获取用例文件名称和地址
        file_path=get_project_path()+'/test_cases/'
        file_name=file_path+"test_"+sheet_name+'.py'

        demo=Template('''\n
#coding:utf-8
__author__ = 'wujiang'

import requests
import unittest
from HTMLReport import logger
class Test_${sheet_name}(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()
    def tearDown(self):
        pass
    $cases
        ''')
        cases_string=self.create_sheet_case(sheet_name)
        string=demo.safe_substitute(sheet_name=sheet_name,cases=cases_string)
        with open(file_name,'w') as fp:
            fp.write(string)

    def create_case_files(self):
        #获取excel的所有表格名称，并循环生成测试用例集合py文件
        name_list=self.excel.get_sheet_names()
        for  name in name_list:
            self.create_single_file(name)



if __name__ == '__main__':
    GenerateTestCase().create_case_files()