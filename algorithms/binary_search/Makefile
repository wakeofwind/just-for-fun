naive-test:
	gcc -shared -o libnaive.so naive.c
	gcc -I. -L. -lnaive -o test_naive test_naive.c
	LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH ./test_naive

test:
	gcc -o test_naive naive.c test_naive.c
	./test_naive

clean:
	rm -f libnaive.so test_naive
