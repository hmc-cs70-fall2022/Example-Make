#!/usr/bin/python3

# Run with: python3 rebuild.py

from os.path import getmtime, exists
from os import system

# run a command on the system
def run(cmd):
    print("Running:",cmd)
    if (system(cmd) != 0):
        raise RuntimeError("Command failed")

# is file1 newer than file2
def isNewer(file1,file2):
    return getmtime(file1) > getmtime(file2)

# check if a file doesn't exist
def doesntExist(file):
    return not exists(file)
    
if doesntExist("cow.o") \
   or isNewer("cow.cpp", "cow.o") \
   or isNewer("cow.hpp", "cow.o"):
    run("clang++ -Wall -Wextra -pedantic -c -std=c++17 cow.cpp")

if doesntExist("main.o") \
   or isNewer("main.cpp", "main.o") \
   or isNewer("cow.hpp", "main.o"):
    run("clang++ -Wall -Wextra -pedantic -c -std=c++17 main.cpp")

if doesntExist("main") \
   or isNewer("main.o", "main") \
   or isNewer("cow.o", "main"):
    run("clang++ -std=c++17 -o main main.o cow.o")

print("All done.")