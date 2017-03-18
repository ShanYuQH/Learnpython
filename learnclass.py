# -*- coding:utf-8 -*-

class Screen(object):
    '实现一个可以用属性方式调用方法的方法'

    #定义宽度
    @property
    def width(self):
        return (self._width)
    @width.setter
    def width(self, value):
        self._width = value

    #定义高度
    @property
    def height(self):
        return (self._height)
    @height.setter
    def height(self, value):
        self._height = value

    #计算
    @property
    def resolution(self):
        return self._width * self._height


if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution   #使用断言函数来进行结果判断
