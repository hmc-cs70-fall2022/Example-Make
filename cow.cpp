/*
 * \file cow.cpp
 * \author CS 70 Provided Code
 * \brief Implements the Cow class
 */

#include <cstddef>
#include <iostream>
#include "cow.hpp"

using namespace std;

Cow::Cow(int numSpots, int age)
    : numSpots_{numSpots},
      age_{age}
{
    cout << "Made a cow with " << numSpots_ << " spots!" << endl;
}

void Cow::moo(int numMoos) const {
    for (int i = 0; i < numMoos; ++i) {
        cout << "Moo! ";
    }
    cout << endl;
}

int Cow::getNumSpots() const {
    return numSpots_;
}

int Cow::getAge() const {
    return age_;
}

void Cow::setNumSpots(int numSpots) {
    numSpots_ = numSpots;
}

void Cow::setAge(int age) {
    age_ = age;
}
