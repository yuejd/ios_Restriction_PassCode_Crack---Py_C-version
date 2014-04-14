#!/usr/bin/python
#Filename: ioscrack.py

#from passlib.utils.pbkdf2 import pbkdf2
import os
#import htos
import sys
from time import time
import base64
import ctypes

HOMEDIR = '/Users/yuejiadi/Library/Application Support/MobileSync/Backup/'
PSFILE = '398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b'
ITERATIONS = 1000

backup_dir = os.listdir(HOMEDIR)

for bkup_dir in backup_dir:
    passfile = open(HOMEDIR + bkup_dir + "/" + PSFILE, "r")
    line_list = passfile.readlines()
    secret64 = line_list[6][1:29]
    salt64 = line_list[10][1:9]
    print "secret: ", secret64
    print "salt: ", salt64
    #secret = htos.to_hex(base64.b64decode(secret64))
    secret = base64.b64decode(secret64)
    #print secret
    salt = base64.b64decode(salt64) 

    ##########################
    crack_func = ctypes.CDLL("./crack.so").crack_thread
#    crack_func.restype = ctypes.c_char_p
    start_t = time()
    pass_code = "0000"
    c_pass_code = ctypes.c_char_p(pass_code)
#    rtn = ctypes.c_char_p(crack_func(secret, salt, pass_code))
    crack_func(secret, salt, c_pass_code)
    print c_pass_code.value
#    print "type:", type(pass_code)
#    print rtn.value
#    print "type:", type(rtn)
    duration = time() - start_t
    print "%f seconds" % ( duration )

    ##########################
    #start_t = time()
    #for i in range(10000):
    #    key = "%04d" % ( i )
    #    #out = PBKDF2(key, salt, ITERATIONS).hexread(20)
    #    out = pbkdf2(key, salt, ITERATIONS)
    #    #print i," | ", out
    #    if out == secret:
    #        print "key: ", key
    #        duration = time() - start_t
    #        print "%f seconds" % ( duration )
    #        sys.exit(0)
    #print "no exact key"

#secret = '2beab52adb73bc50faa017fc84cbf4895d4311ad'
#salt = '23d0d317'
#key = '6532'
#rounds = 1000
#
#out = pbkdf2(key, htos.to_str(salt), rounds)
#
#print htos.to_hex(out)
#print secret
