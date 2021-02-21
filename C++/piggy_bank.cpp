#include <iostream>

int main()
{
    int pesos, reals, soles;
    double dollars;
    std::cout << "Enter number of Colombian Pesos: ";
    std::cin >> pesos;
    std::cout << "Enter number of Brazilian Reais: ";
    std::cin >> reals;
    std::cout << "Enter number of Peruvian Soles: ";
    std::cin >> soles;

    /*
  1 peso = 0.049 USD
  1 real = 0.19 USD
  1 sol =0.27 USD
  */

    dollars = (0.049 * pesos) + (0.19 * reals) + (0.27 * soles);

    std::cout << "US Dollars = $" << dollars << "\n";
}