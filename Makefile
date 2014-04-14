default :
	make crack.so

crack.so : crack.c
	gcc -o crack.so -shared -fPIC crack.c -lcrypto

run :
	./iospyc.py
