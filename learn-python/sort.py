#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:   Leo Xu     <leopallas@gmail.com>
# Version:  1.0
# Create:   2014-05-19 14:56
# Copyright 2014 LEO
"""
在用python 写程序时，经常会跟 dict ,list ,tuple 打交道，这些集合是可以迭代的。
但经常也会对数据进行排序。list,tuple 本身是有序的， 而 dict 本身是无序的。 即使是有序的东西，也未必满足我们需要，可能还是要再次排序。
因此参考了python 文档和网上的一些例子。总结如下：
sort与sorted区别
1.序列的 sort 函数, 与 内置的 sorted 方法 有很类似的参数  sort(cmp=None, key=None, reverse=False)
2.sort 直接把当前序列变得有序，而sorted 是另外生成一个副本,是有返回值的
参数
1.cmp  接收的是一个函数, 但这个函数应该有两个参数，这种方式是被淘汰的对象,用key 比较好
2.key  接收的也是一个函数,这个函数只有一个参数.
3.reverse 就是升序或降序排列了
"""

#========对简单字典dict的排序操作===========
a = {"c": 9, "b": 6, "a": 7}
""" 按照 key 来排序 """
b = sorted(a.items(), key=lambda x: x[0])
print b

""" 按照 value 来排序 """
c = sorted(a.items(), key=lambda x: x[1])
print c

#========一个更复杂的字典===================
a = {(10, 'abc'): 1, (8, 'def'): 4, (12, 'ghi'): 3}
b = sorted(a.items(), key=lambda x: x[0][0])
print '按照key 元组的第一个值进行排序', b
c = sorted(a.items(), key=lambda x: x[1])
print '按照value 进行排序', c

#========对序列排序list的排序操作==========
mylist1 = ['a', 'c', 'b', 'd']
mylist1.sort(reverse=True)
print '直接调用序列的', mylist1
a = sorted(mylist1, reverse=False)
print '调用 sorted 方法返回:', a

#========同时排序,先对第二个关键字排序,再对第一个关键字排序
a = [('d', 2), ('a', 4), ('b', 3), ('c', 2)]
print sorted(a, key=lambda x: (x[1], x[0]))

#========创建一个类来测试=================
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


studentList = [
    Student('tom', 80, 18),
    Student('jack', 90, 17),
    Student('marry', 70, 20),
]


def orderbyage(student):
    return student.age


print '按年龄排序:', sorted(studentList, key=orderbyage)
print '按成绩排序:', sorted(studentList, key=lambda stu: stu.grade)