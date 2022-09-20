#!/usr/bin/python3

# Run with: python3 make.py

import sys
from os.path import getmtime, exists
from os import system

# --- Useful helper functions ---

# indented print command
indent = 0
def iprint(text, delta=0):
    global indent
    if text is not None: print(("  "*indent) + text)
    indent = indent + delta

# error exit
def error(text):
    print("A problem with the Makefile (or its use) stopped execution:")
    print("\t" + text)
    sys.exit(1)

# run a command on the system
def run(cmd):
    iprint(f'  - Running: {cmd}')
    if (system(cmd) != 0):
        error("Command failed")

# check if a file doesn't exist
def doesntExist(file):
    return not exists(file)

# is file1 newer than file2
def isNewer(file1,file2):
    return doesntExist(file2) or (getmtime(file1) > getmtime(file2))

# --- Data describing what to build and how ---

# Unlike build.py, now we've got DATA describing our specific project, and
# generic code that understands that data.  For each file, we have two bits
# of information, the prereqs for the file (a list of files it depends on),
# and the command to run.
#
# The dictionary below maps FILENAME -> (LIST_OF_PREREQS, BUILD_COMMAND)

buildRules = { 
    "main":   (('main.o', 'cow.o'),
        "clang++ -std=c++17 -o main main.o cow.o"),
    "cow.o":  (('cow.cpp', 'cow.hpp'),
        "clang++ -Wall -Wextra -pedantic -c -std=c++17 cow.cpp"),
    "main.o": (('main.cpp', 'cow.hpp'),
        "clang++ -Wall -Wextra -pedantic -c -std=c++17 main.cpp"),
    "clean":  ((),
        "rm -f *.o main"),
}

# --- The build algorithm, a recursive function called make ---

def make(file):
    iprint(f'- Making {file}', +1)  # +1 => Indent subsequent output

    if file not in buildRules:
        # If a file doesn't have a rule, it's fine if it already exists
        if doesntExist(file):
            error(f"Couldn't make '{file}' (no rule, and doesn't it exist)!")
        iprint(f'  + Okay, no rule found, but file exists!', -1)
        return
    
    # Okay, the file does have a rule, get the prereqs and command to run
    (prereqs, cmd) = buildRules[file]
    iprint(f'- Found rule for {file}, prereqs: {" ".join(prereqs)}')

    # Before going further, make sure all prereqs are up to date
    # before checking this file (recursively run make on prereqs)
    for prereq in prereqs:
        make(prereq)

    # Now that prereqs are up to date, see if we need to build this file
    mustBuildReason = None
    if doesntExist(file):
        mustBuildReason = "it doesn't exist"
    else:
        for prereq in prereqs:
            if isNewer(prereq, file):
                mustBuildReason = "prereqs are newer"
    
    # If we do need to build the file (and have a command to run), do so.
    if mustBuildReason is not None:
        iprint(f'- Target {file} must be built because {mustBuildReason}.')
        if cmd is not None:
            iprint(f'- Building: {file}')
            run(cmd)
        iprint(f'+ Made {file}')
    else:
        iprint(f"+ Target {file} doesn't need to be rebuilt (no newer prereqs)")

    # Set indentation back to what it was before and return
    iprint(None, -1)


# --- Main Program ---

# Now we run the make function using either the files passed in on the
# command line, or if no files were passed in, use the first item in the
# buildRules dictionary

whatToMake = sys.argv[1:]
if not whatToMake:
    whatToMake = [next(iter(buildRules.keys()))]
for file in whatToMake:
    make(file)
