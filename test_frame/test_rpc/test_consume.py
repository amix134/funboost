# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/8/8 0008 14:57
import time

from function_scheduling_distributed_framework import get_consumer
from function_scheduling_distributed_framework.utils import LogManager

logger = LogManager('f2').get_logger_and_add_handlers()


def f2(a, b):
    logger.info(f'消费此消息 {a} + {b} 中。。。。。')
    time.sleep(3)  # 模拟做某事需要阻塞10秒种，必须用并发绕过此阻塞。
    logger.info(f'计算 {a} + {b} 得到的结果是  {a + b}')
    return a + b


# 把消费的函数名传给consuming_function，就这么简单。
consumer = get_consumer('queue_test33', consuming_function=f2, is_using_rpc_mode=True,broker_kind=2,concurrent_num=1000)  # 通过设置broker_kind，一键切换中间件为mq或redis等7种中间件或包。

if __name__ == '__main__':
    consumer.start_consuming_message()
