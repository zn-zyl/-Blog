"""
=============================
@Time : 2020/5/24 18:24
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
定义一个user类
属性：name:属性值只能是字符串
     age:属性值只能是int
     desc:属性值只能是字符串
     skill:属性值只能是list类型
name属性不能被删除
skill属性如果没有添加 则返回NONE
"""


class User:
    def __setattr__(self, key, value):
        if key == 'name':
            if isinstance(key, str):
                super().__setattr__(key, value)
            else:
                raise TypeError("name必须是str类型")
        elif key == 'age':
            if isinstance(key, int):
                super().__setattr__(key, value)
            else:
                raise TypeError("age必须是int类型")
    def __delattr__(self, item):
        if item == "name":
            return AttributeError("name属性不能被删除")
        else:
            super().__delattr__(item)

    def __getattr__(self, item):
        if item == "skill":
            return None
        else:
            return super().__getattr__(item)
