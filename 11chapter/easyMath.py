#!/usr/bin/env python
#coding:gbk

from operator import add, sub
from random import randint, choice

ops = {'+':add, '-':sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')                           #���ȡѡ��
    nums = [randint(1,10) for i in range(2)]    #��������10���ڵ������
    nums.sort(reverse=True)                     #���ɵ����������������
    ans = ops[op](*nums)                        #������
    pr = '%d %s %d = ' % ( nums[0], op, nums[1] )
    oops = 0                                    #��������������ʼ��
    while True:
        try:
            if int(raw_input(pr)) == ans:       #�жϴ��Ƿ���ȷ
                print 'correct'
                break
            if oops == MAXTRIES:                #�������Σ�������
                print 'answer\n%s%d' % (pr, ans)
            else:
                print 'incorrect...try again'   #�𰸲���ȷ����Ҫ���»ش�
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):   #�쳣����
            print 'invalid...try again'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[y]').lower()    #���д�ͳһתΪСд
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()
