/*
 * \file main.cpp
 * \author CS 70 Provided Code
 * \brief Creates and interacts with some Cows.
 */

#include <iostream>
#include "cow.hpp"

using namespace std;

int main() {
    Cow bessie{3, 12};
    const Cow mabel{1, 2};

    // This line wouldn't work!
    // Cow duke;

    bessie.moo(1);
    mabel.moo(2);
    bessie.setAge(4);

    // This line wouldn't work!
    // mabel.setAge(2);

    return 0;
}
