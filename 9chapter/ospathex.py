#!/usr/bin/env python
#coding=gbk
import os

for tmpdir in ('./'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no temp directory available'
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)    #�ı䵱ǰ����Ŀ¼�����뵽tmpdirָ����Ŀ¼��
    cwd = os.getcwd()   #��ȡ��ǰ����Ŀ¼
    print '*** current temporary directory'
    print cwd

print '*** creating example directory'
print cwd

print '*** current temporary directory...'
os.mkdir('example')     #����Ŀ¼
os.chdir('example')     #���뵽������Ŀ¼��
cwd = os.getcwd()       #��ȡ��ǰ����Ŀ¼
print '*** new working directory:'
print cwd
print '*** original directory listing:'
print os.listdir(cwd)   #�г�ָ��Ŀ¼���ļ�

print '*** creating test file...'
fobj = open('test.txt', 'w')#����һ��test.txt�ļ�
fobj.write('foo\n')         #д������foo
fobj.write('bar\n')         #д������bar
fobj.close()                #�ر��ļ�������
print '*** updated directory listing��'
print os.listdir(cwd)       #�г���ǰĿ¼�µ������ļ�




