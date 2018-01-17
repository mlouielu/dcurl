curl.o: curl.c
	gcc -fsigned-char -fPIC -g -c $<

constants.o: constants.c
	gcc -fPIC -g -c $<

trinary.o: trinary.c
	gcc -fsigned-char -fPIC -g -c $<

dcurl.o: dcurl.c
	gcc -fPIC -g -c $<

pow_c.o: pow_c.c
	gcc -fsigned-char -fPIC -g -c $<

test: test.c curl.o constants.o trinary.o dcurl.o pow_c.o
	gcc -fsigned-char -g -o $@ $^ -lpthread

#dcurl.o: dcurl.c
#	gcc -fPIC -c dcurl.c
#
libdcurl.so: dcurl.o curl.o constants.o trinary.o pow_c.o
	gcc -fsigned-char -shared -o libdcurl.so $^ -lpthread
