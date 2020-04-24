__author__ = "Gerhart"
__license__ = "GPL3"
__version__ = "1.2.0"

from pykd import *
import sys


afd = module("afd")
ListHead = afd.AfdEndpointListHead
print("afd!AfdEndpointListHead address is ", hex(ListHead))
ptrNext = ptrQWord(ListHead)
print("----AfdEndpoint", hex(ListHead), hex(ptrWord(ListHead-0x120)))
count = 1
while (ptrNext != ListHead) & (ptrNext != 0xffffffffffffffff):
	print("----AfdEndpoint",hex(ptrNext), hex(ptrWord(ptrNext-0x120)), findSymbol(ptrQWord(ptrNext-0x108)), loadCStr(ptrQWord(ptrNext-0x120+0x28)+0x450), hex(ptrQWord(ptrQWord(ptrNext-0x120+0x28)+0x2e8)))
	ptrNext = ptrQWord(ptrNext)
	count = count+1
print("Cycle end. Count", count)