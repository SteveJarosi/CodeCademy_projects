#include <iostream>

int main()
{

    int dog_age;

    std::cout << "Enter your dog's age: ";
    std::cin >> dog_age;

    int early_years = 21;                        // first 2 years
    int later_years = (dog_age - 2) * 4;         // after 2 years
    int human_years = early_years + later_years; // whatever

    std::cout << "My name is Tim! Ruff ruff, I am " << human_years << " years old in human years.\n";
}