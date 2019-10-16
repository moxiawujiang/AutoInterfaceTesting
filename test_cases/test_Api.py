

#coding:utf-8
__author__ = 'wujiang'

import requests
import unittest
from HTMLReport import logger
class Test_Api(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()
    def tearDown(self):
        pass
    
    def test_001_get_categroy(self):
        """获取菜单"""
        url='http://127.0.0.1:8000/categorys/?format=json'
        data=None
        res=self.s.get(url=url,data=data)
        expect ='detail'
        logger().info('url:'+'http://127.0.0.1:8000/categorys/?format=json')
        logger().info('data:'+"None")
        result=res.text
        self.assertIn(expect,result)
        logger().info('result:'+result)
        
        