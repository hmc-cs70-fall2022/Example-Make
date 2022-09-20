/*
 * \file cow.hpp
 * \author CS 70 Provided Code
 * \brief Interface definition for the Cow class.
 */

#ifndef COW_HPP_INCLUDED
#define COW_HPP_INCLUDED

#include <iostream>
#include <fstream>

/*
 * \class Cow
 * \brief Knows how many spots it has & how old it is. Can moo.
 */
class Cow {
 public:
    // We can only have a Cow if we know
    // how many spots it has and how old it is
    Cow(int numSpots, int age);
    Cow() = delete;

    // Moo the right number of times.
    void moo(int numMoos) const;

    // Accessor member functions
    int getNumSpots() const;
    int getAge() const;

    // Mutator member functions
    void setNumSpots(int numSpots);
    void setAge(int age);

 private:
    int numSpots_;
    int age_;
};

#endif  // ifndef COW_HPP_INCLUDED
