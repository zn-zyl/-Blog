"""
============================
Author:柠檬班-木森
Time:2020/6/1   13:51
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
import gevent
import multiprocessing



class MyProcess(multiprocessing.Process):
    def __init__(self, queue:multiprocessing.Queue):
        super().__init__()
        self.queue = queue



    def run(self):
        """进程的工作函数"""
        # 注意点：补丁要打在进程之中，否则影响进程的队列模块使用
        from gevent import monkey
        monkey.patch_all()

        # 进程中创建1000个协程
        cor_list = []
        for i in range(1000):
            cor = gevent.spawn(self.cor_work, i)
            cor_list.append(cor)
        for i in cor_list:
            i.join()
        # gevent.joinall(cor_list)

    def cor_work(self, i):


        """协程函数的工作任务"""
        while self.queue.qsize() > 0:
            try:
                url = self.queue.get(timeout=0.001)
            except:
                # print("队列中无数据")
                break
            else:
                print(f"进程：{self.pid}--第{i}个协程当前正在请求：{url}")
                # time.sleep(1)


# 计算时间的装饰器
def decorator(func):
    def wrapper(*args, **kwargs):
        # 函数执行之前获取系统时间
        start_time = time.time()
        func(*args, **kwargs)
        # 函数执行之后获取系统时间
        end_time = time.time()
        print('执行时间为：', end_time - start_time)
        return end_time - start_time

    return wrapper


@decorator
def main():
    # 创建队列，添加100000个任务
    urls_queue = multiprocessing.Queue()
    for i in range(100000):
        urls_queue.put("https://www.baidu.com/-{}".format(i))
    # 创建进程
    pro_list = []
    for i in range(4):
        print(f"创建进程：---{i}----")
        p = MyProcess(urls_queue)
        p.start()
        pro_list.append(p)

    for p in pro_list:
        p.join()


if __name__ == '__main__':
    main()
