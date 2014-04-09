#!usr/bin/env python
#coding=utf-8

__author__ = 'xw'
# import time
# import sched
#
# s = sched.scheduler(time.time, time.sleep)
#
#
# #被周期性调度触发的函数
# def event_func():
#     print "Current Time:", time.time(), 'msg:'
#
#
# #enter四个参数分别为：间隔时间、优先级（用于同时间到达的两个事件同时执行时定序）、被调用触发的函数，给他的参数（注意：一定要以tuple给如，如果只有一个参数就(xx,)）
# def perform(inc):
#     s.enter(inc, 0, perform, (inc,))
#     event_func()
#
#
# def main(inc=100):
#     s.enter(0, 0, perform, (inc,))
#     s.run()
#
# if __name__ == "__main__":
#     main()

x = [v for v in range(0, 10)]

rows = [x for row in range(0, 10)]
print rows

print [x**2 for x in range(10)]