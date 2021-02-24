#include <iostream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <string>
#include "ttt.hpp"

std::vector<char> p1;
std::vector<char> p2;
std::string move = "hello";
int main()

{
    for (int i = 0; i < 9; i++)
{
    p1.push_back(' ');
    p2.push_back(' ');
}
    intro();
    board_display(p1, p2);
    int winner = 0;
    int player = decide_start();
    
    while (winner = 0) {
        std::cout << "Player" << player << ", enter coordinate!";
        std::cin >> move;
        std::cout << "\n";
        


        winner++;
    }
}