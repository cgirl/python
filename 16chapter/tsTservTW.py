#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connect from:' % clnt
    def dataRecived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data) )

factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connecting...'
reactor.listenTCP(PORT, factory)
reactor.run()
