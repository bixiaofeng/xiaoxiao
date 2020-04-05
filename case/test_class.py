#encoding:utf-8
#@Time:2020/1/16 9:58
#@Author:sunny

class TestClass:  
    def test_one(self):  
        x = "this"  
        assert 'h' in x  
  
    def test_two(self):  
        x = "hello"  
        assert hasattr(x, 'check')