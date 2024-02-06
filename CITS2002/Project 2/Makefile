#	A Makefile to build our 'mysync' Project

CC = gcc
CFLAGS = -std=c11 -Wall -Werror
OBJS = mysync.o file_ops.o dir_ops.o sync_ops.o pattern_ops.o

all: mysync

mysync: $(OBJS)
	$(CC) $(CFLAGS) -o mysync $(OBJS)

mysync.o: mysync.c mysync.h
	$(CC) $(CFLAGS) -c mysync.c

file_ops.o: file_ops.c mysync.h
	$(CC) $(CFLAGS) -c file_ops.c

dir_ops.o: dir_ops.c mysync.h
	$(CC) $(CFLAGS) -c dir_ops.c

sync_ops.o: sync_ops.c mysync.h
	$(CC) $(CFLAGS) -c sync_ops.c

pattern_ops.o: pattern_ops.c mysync.h
	$(CC) $(CFLAGS) -c pattern_ops.c

clean:
	rm -f mysync $(OBJS)
