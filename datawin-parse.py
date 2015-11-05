#!/usr/bin/python2
import os,sys
import binascii
import struct

# chunk names are 4 bytes long
# not quite sure how long the header is but I guess 8 bytes for now :>
dwheader=binascii.unhexlify("464F524DE6EF5A03")
datawin=open("data.win","r+")
header=datawin.read(8)

if header==dwheader:
    print "Doogie doogie Dodger"
else:
    print "Wrong magic bytes"
    quit()


def read_chunk():
    chunkname=datawin.read(4)
    print "Reading "+chunkname
    print datawin.tell()
    chunksize=datawin.read(4)
    # TODO: _THIS_ is stupid! ... let's correct this with a nice struct or somethin
    # later...
    foo=binascii.hexlify(chunksize)
    chunksize=foo[-2:]+foo[4:6]+foo[2:4]+foo[:2]
    chunksize=int(chunksize,16)
    chunk=datawin.read(chunksize)


print datawin.tell()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()
read_chunk()

