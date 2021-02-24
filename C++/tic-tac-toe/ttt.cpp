#include <iostream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <string>
//#include "ttt.hpp"

std::vector<char> p1;
std::vector<char> p2;
std::string move;
int player, winner;

void intro()
{
    std::cout << "Let's play Tic-Tac-Toe!\n";
    std::cout << "Player1: X\n";
    std::cout << "Player2: O\n";
}

void board_display(std::vector<char> p1, std::vector<char> p2)
{
    std::cout << "  a b c\n";
    std::cout << "1" << (p1[0] = 'X' ? p1[0] : p2[0]) << (p1[1] = 'X' ? p1[1] : p2[1]) << (p1[2] = 'X' ? p1[2] : p2[2]) << "\n";
    std::cout << "2" << (p1[3] = 'X' ? p1[3] : p2[3]) << (p1[4] = 'X' ? p1[4] : p2[4]) << (p1[5] = 'X' ? p1[5] : p2[5]) << "\n";
    std::cout << "3" << (p1[6] = 'X' ? p1[6] : p2[6]) << (p1[7] = 'X' ? p1[7] : p2[7]) << (p1[8] = 'X' ? p1[8] : p2[8]) << "\n";
}

int decide_start()
{
    srand(time(NULL));
    int p = std::rand() % 2 + 1;
    std::cout << "Player " << p << " starts!\n";
    return p;
}

void handle_input(std::string move)
{
    int locus=10;
    if (move == "a1")
    {
        locus = 0;
    }

    if (player == 1)
    {
        p1[locus] = 'X';
    }
    else
    {
        p2[locus] = 'O';
    }
}
void determine_winner() {
    winner = 1;
}
void switch_player() {
    if (player == 1 ) {
        player = 2;
    } else {player = 1;}
}
int main()

{
    for (int i = 0; i < 9; i++)
    {
        p1.push_back(' ');
        p2.push_back(' ');
    }
    intro();
    board_display(p1, p2);
    winner = 0;
    player = decide_start();

    while (winner == 0)
    {
        std::cout << "Player" << player << ", enter coordinate:";
        std::cin >> move;
        std::cout << "\n";
        handle_input(move);
        board_display(p1, p2);
        determine_winner();
        switch_player();


        
    }
    std::cout << "Congratulations, Player" << winner << "!\n";

}
