# This is a simple Makefile, it adds macros to example1.mak
#
# Use it by running:
#     cs70-make -f example2.mak 
# or
#     cs70-make -f example2.mak main
#
# (or specify any other target from the the file)

CXX      = clang++
CXXFLAGS = -g -Wall -Wextra -pedantic -std=c++17

all: main

main: main.o cow.o
	$(CXX) $(CXXFLAGS) -o main main.o cow.o

cow.o: cow.cpp cow.hpp
	$(CXX) $(CXXFLAGS) -c cow.cpp

main.o: main.cpp cow.hpp
	$(CXX) $(CXXFLAGS) -c main.cpp

clean:
	rm -f *.o main
