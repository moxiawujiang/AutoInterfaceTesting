

#coding:utf-8
__author__ = 'wujiang'

import requests
import unittest
from HTMLReport import logger
class Test_ShopApi(unittest.TestCase):
    def setUp(self):
        self.s=requests.session()
    def tearDown(self):
        pass
    
    def test_001_login(self):
        """登录认证接口"""
        url='http://127.0.0.1:8000/login/?format=json'
        data=获取ShopApi中login参数失败
        res=self.s.post(url=url,data=data)
        expect ='token'
        logger().info('url:'+'http://127.0.0.1:8000/login/?format=json')
        logger().info('data:'+"获取ShopApi中login参数失败")
        result=res.text
        self.assertIn(expect,result)
        logger().info('result:'+result)
        
    def test_002_get_goods(self):
        """获取商品"""
        url='http://127.0.0.1:8000/goods/?format=json'
        data=None
        res=self.s.get(url=url,data=data)
        expect ='detail'
        logger().info('url:'+'http://127.0.0.1:8000/goods/?format=json')
        logger().info('data:'+"None")
        result=res.text
        self.assertIn(expect,result)
        logger().info('result:'+result)
        
        