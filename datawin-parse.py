#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os,sys
import binascii
import struct
import StringIO

# chunk names are 4 bytes long
# not quite sure how long the header is but I guess 8 bytes for now :>
# actually it's not really a header but the first chunk
# 4 bytes for the name (FORM) and 4 bytes for the length (filesize-8)
# so this is not needed anymore

#dwheader=binascii.unhexlify("464F524DE6EF5A03")
datawin=open("data.win","r+")
#datawin.seek(0,2)
#dwsize=datawin.tell()
#datawin.seek(0,0)
#header=datawin.read(8)
chunks={}

#if header==dwheader:
#    print "Doogie doogie Dodger"
#else:
#    print "Wrong magic bytes"
#    quit()

def read_chunk(data):
    # data has to be a StringIO/file... not!
    if type(data)!=type("foo"):
        print "Somehow the data is not a string"
        quit()
    else:
        dsize=len(binascii.hexlify(data))/2
        data=StringIO.StringIO(data)
#    data.seek(0,2)
#    dsize=datawin.tell()
#    if dsize!=realdsize:
#        print dsize
#        print realdsize
#        print "FUCK THIS SHIT I'M GOING HOME"
#        quit()
    data.seek(0,0)
    chunkname=data.read(4)
    if chunkname.isupper():
        print "Reading "+chunkname
    else:
        print "Reading "+binascii.hexlify(chunkname)
    chunksize=data.read(4)
    if len(chunksize)!=4:
        data.seek(0,0)
        return [data.read()]
    # TODO: _THIS_ is stupid! ... let's correct this with a nice struct or somethin
    # later...
    foo=binascii.hexlify(chunksize)
    chunksize=foo[-2:]+foo[4:6]+foo[2:4]+foo[:2]
    chunksize=int(chunksize,16)
    if chunksize+8==dsize:
        # print "One big chunk"
        chunk=data.read(chunksize)
        return [chunkname, chunk]
    elif chunksize+8 > dsize:
        # print "No chunk for you" # pure data
        data.seek(0,0)
        return [data.read()]
    else:
        # print "Multiple CHUNKS!!!!! xD ohh I'm sooo tired"
        chunk=data.read(chunksize)
        rest=data.read()
        # print chunksize
        # print "Actual chunk size "+str(len(chunk))
        # print dsize
        # print "REST:"
        # print len(rest)
        if len(rest)==0:
            print "Something went terrible, terrible WRONG :( WTF IS HAPPENING?????"
            return [chunkname, chunk]
        else:
            return [chunkname, chunk, rest]

def extract_chunks(data):
    if type(data)==type("Foo"):
        realdatasize=len(data)
        data=StringIO.StringIO(data)
    else:
        realdatasize=len(data.read())
    data.seek(0,2)
    datasize=data.tell()
    if datasize!=realdatasize:
        print "OK WHY ISN'T THIS WORKING??"
        quit()
    data.seek(0,0)
    while data.tell()!=datasize:
        chunk=read_chunk(data.read())
        if len(chunk)==1:
            return chunk[0]
        elif len(chunk)==2:
            print "One big chunk you chump"
            if type(chunk[1])==type("foo"):
                return {chunk[0]:extract_chunks(chunk[1])}
            else:
                print "OMG LIKE THAT'S TOTALLY LIKE A DICTIONARY THAT SOMEHOW GOT LIKE RETURNED! WHAT THE EFF"
                return {chunk[0]:chunk[1]}
        elif len(chunk)==3:
            if type(chunk[1])==type("foo"):
                newchunk={chunk[0]:extract_chunks(chunk[1])}
            else:
                newchunk={chunk[0]:chunk[1]}
            if type(chunk[2])==type("foo"):
                newdict=extract_chunks(chunk[2])
                if type(newdict)==type({}):
                    newchunk.update(newdict)
                else:
                    newchunk.update({"DEFECT":newdict})
            else:
                newchunk.update(chunk[2])
            return newchunk

final_dict=extract_chunks(datawin)
#print type(final_dict)
print len(final_dict["FORM"]["STRG"])
print type(final_dict["FORM"]["STRG"])
#for foo in final_dict["FORM"]:
#    print foo
#while datawin.tell()!=dsize:
    #extract chunk from data
    #übergib chunk to while like this


# chunk=read_chunk(datawin)
#
# chunks[chunk[0]]=StringIO.StringIO(chunk[1])
#
# chunk=read_chunk(chunks["FORM"])
#
#
# if check_chunk(StringIO.StringIO(chunk[1]))==0:
#     chunk=read_chunk(StringIO.StringIO(chunk[1]))

#while dwsize!=datawin.tell():
#    chunk=read_chunk()
#    chunks[chunk[0]]=chunk[1]


# check if chunk
# add chunk to dictionary
# check if chunk
# add to dictionary
