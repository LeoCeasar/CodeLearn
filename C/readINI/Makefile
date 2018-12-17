CC = gcc

all: main
main: libcalc.a main.c libshow.so
    gcc -o main main.c -L. -lcalc  -lshow

lib: libcalc.a libshow.so
libcalc.a : calc.o
        ar crs libcalc.a calc.o
calc.o : calc.c
        $(CC) -c calc.c -o calc.o
libshow.so: show.o
        $(CC) -shared -o libshow.so show.o
show.o: show.c
        $(CC) -fPIC -Wall -c show.c -o show.o

clean:
    rm -rf *.o *.so *.a main
