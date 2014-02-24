#!/usr/bin/env python
# encoding: utf-8
class RecvPacket:

    def __init__(self,buff):
        self.buff=buff
        self.currentIndex=0

    def unpackInt(self,size):
        return int

    def unpackStr(self):
        return str
c = RecvPacket('xxx')
print c.buff
