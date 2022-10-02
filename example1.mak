# This is a simple Makefile, it exactly mirrors the data we saw in make.py
#
# Use it by running:
#     cs70-make -f example1.mak 
# or
#     cs70-make -f example1.mak main
#
# (or specify any other target from the the file)

main: main.o cow.o
	clang++ -g -std=c++17 -o main main.o cow.o

cow.o: cow.cpp cow.hpp
	clang++ -g -Wall -Wextra -pedantic -c -std=c++17 cow.cpp

main.o: main.cpp cow.hpp
	clang++ -g -Wall -Wextra -pedantic -c -std=c++17 main.cpp

clean:
	rm -f *.o main
