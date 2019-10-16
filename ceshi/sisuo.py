#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sisuo.py
# @Author: hak
# @Date  : 2019-05-16
# @Desc  :
# coding=utf-8
import time
import threading

class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


def transfer(_from, to, amount):
    if _from.lock.acquire():  # 锁住自己的账户
        _from.withdraw(amount)
        time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
        print 'wait for lock...'
        if to.lock.acquire():  # 锁住对方的账户
            to.deposit(amount)
            to.lock.release()
        _from.lock.release()
    print 'finish...'


a = Account('a', 1000, threading.Lock())
b = Account('b', 1000, threading.Lock())
threading.Thread(target=transfer, args=(a, b, 100)).start()
threading.Thread(target=transfer, args=(b, a, 200)).start()