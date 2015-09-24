#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ftplib
import socket
import os

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-4.0-to-4.0.10.diff.gz'

def main():
    #����
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR:cannot reach "%s"' % HOST
        return
    print '*** Connect to host %s' % HOST

    #��¼
    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymously"'

    #��ת��Ŀ��Ŀ¼
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    #����Ŀ���ļ�
    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write )
    except ftplib.error_perm:
        print 'ERROR: cannot read file %s' % FILE
        os.unlink(FILE)
    else:
        cwd = os.getcwd()
        print '*** Downloaded "%s" to "%s"' % (FILE, cwd)
    f.quit()
    return

#����������
if __name__ == '__main__':
    main()
