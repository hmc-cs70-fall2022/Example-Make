# Introduction to Make

This GitHub repositor provides an introduction to the `make` tool.

## Review `rebuild.py`

Look over the code for rebuild.py and run it by typing:

```
python3 rebuild.py
```

experiment with editing one of the C++ source files and confirm it rebuilds
exactly what is necessary.

When you're ready to move on, run

```
rm *.o main
```

## Try running `make.py`

A problem with `rebuild.py` is that it's very hard-coded to our particular
program, and what depends on what, and what to run is baked into the code.

The program `make.py` is a generalization of the build process, which turns
the dependencies into data.  Look at the code and find the definition of
`buildRules`.  It's a dictionary that specifies both what the prerequisite
files are for a given file (i.e., what things it needs) and the command to
run for that file.

Then read over the `make` function.  It's a little long, but it should be
self explanatory.  Then, run:

```
python3 make.py
```

The program is rather chatty about what it is doing and why.  Read over
the output that it produced explaining its actions.  Then, as you did with
`rebuild.py`, you may want to try modifying a C++ source file and confirming
that it indeed rebuilds exactly what is needed.

The specification in `buildRules` also includes a rule for how to build a file
called `clean`, have a go at figuring out what will happen when you run.
Check your answer by running:

```
python3 make.py clean
```

Is it good or bad that the file called `clean` is never actually created by
this rule?  (FWIW, this is known as a “phony” target; the make algorithm
always thinks it needs to do what's necessary to build this target.)

## Getting to Know Makefiles — `example1.mak`

In the early 1970s, someone basically wrote `make.py` (but in C), and then
added a few enhancements.  It reads a file (known as a makefile) to get the
same data that was in `buildRules`.  Check out `example1.mak`, it is basically
the same data, just in a different (easier to type) format.

Notice that the format is:

```
‹target› : ‹prerequisites›
    ‹commands›
```

where the commands are indented by a single TAB character (not spaces).  This
file format is super simple to make it _easy_ for a program to read it.

You can check this works by running:

```
cs70-make -f example1.mak
```

or you can make a specific target, e.g.,

```
cs70-make -f example1.mak clean
```

Feel free to experiment with changing files and making sure it only rebuilds
what is necessary.

[Note that by default, if we don't specify a file to use with `-f` it reads
a file called `Makefile`; we haven't used that name because we'll look at
multiple makefiles.  You can aso try running `make` instead of `cs70-make`—it
works the same but is less chatty and has some more advanced features we don't
need to worry about.]

## More `make` features — `example2.mak`

Look over `example2.mak` and try out.  It adds macros to avoid copying and
pasting the same text in various places.

It also adds another phony target called `all`.  This commonly-provided target
is most useful when we have several executables we want to build as we can
list all our executables as prerequisites for `all`.

## Advanced `make` features — `example3.mak`

Look over `example3.mak` and try out.  It uses some more advanced features
to allow us to type less.

## A Handy Trick

Try typing:

```
clang++ -std=c++17 -MM *.cpp
```

Do you see how this output could be handy when creating a makefile?
