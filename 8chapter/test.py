#!/usr/bin/env python
#coding:utf-8

"find the longest line on the file"

#ȱ�㣺�ļ����һ�²��ͷţ�ֱ���������н������ͷ�
def Read1():
    f = open('./maxFact.py', 'r')
    longest = 0
    while True:
        linelen = len(f.readline().strip())
#        print 'linelen =', linelen
        if not linelen:
#            print 'while-if'
            break
        if linelen > longest:
#            print 'while-else'
            longest = linelen
    f.close()
    print 'Read1 =', longest

#Read1��ʹ�õ���readline,��ȡһ����Ϣ;Read2��ʹ�õ���readlines,��ȡ�����������µ����е���
#Read2���ڻ�ȡ������֮�󣬾��ͷ����ļ����
def Read2():
    f = open('./maxFact.py', 'r')
    longest = 0
    allLine = f.readlines()
    f.close()
    for line in allLine:
        linelen = len(line.strip())
        if linelen > longest:
            longest = linelen
    print 'Read2 =', longest

#Read3�ڻ�ȡ������֮ǰ��ÿ�н��в�֣��γ�һ�����б�
#Read2����ѭ����ʱ��Ž��в����
def Read3():
    f = open('./maxFact.py', 'r')
    longest = 0
    allLine = [x.strip() for x in f.readlines()]
    f.close()
    for line in allLine:
        linelen = len(line)
        if linelen > longest:
            longest = linelen
    print 'Read3 =', longest

#Read4����ʹ��readlines��ȡ�����У���Ϊ�ļ��������һ����������ֱ��ʹ���ļ����������ԣ���ȡ��¼ÿ�г��ȵ��б�Ȼ������б����
def Read4():
    f = open('./maxFact.py', 'r')
    allLinelen = [len(x.strip()) for x in f]
    f.close()
    print 'Read4 =', max(allLinelen)

#Read5ʹ�����������ʽ�����б����
def Read5():
    f = open('./maxFact.py', 'r')
    print 'Read5 =', max(len(x.strip()) for x in f)
    f.close()

#Read6ʹ���ļ��򿪵�Ĭ��ģʽ
def Read6():
    print 'Read6 =', max(len(x.strip()) for x in open('./maxFact.py'))


if __name__ == '__main__':
    Read1()
    Read2()
    Read3()
    Read4()
    Read5()
    Read6()
