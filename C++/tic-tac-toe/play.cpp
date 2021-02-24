#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif
#include <iostream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <string>
#include "ttt.hpp"

std::vector<char> p1;
std::vector<char> p2;
std::string move;
int player, winner;

void intro()
{
    std::cout << "Let's play Tic-Tac-Toe!\n";
    std::cout << "Player1: X\n";
    std::cout << "Player2: O\n";
    player = decide_start();
    for (int i = 0; i < 9; i++)
    {
        p1.push_back(' ');
        p2.push_back(' ');
    }
    board_display();
    winner = 0;
}

void board_display()
{   system("CLS");
    std::cout << "  1 2 3\n";
    std::cout << "a"
              << " " << (p1[0] == 'X' ? p1[0] : p2[0]) << " " << (p1[1] == 'X' ? p1[1] : p2[1]) << " " << (p1[2] == 'X' ? p1[2] : p2[2]) << "\n";
    std::cout << "b"
              << " " << (p1[3] == 'X' ? p1[3] : p2[3]) << " " << (p1[4] == 'X' ? p1[4] : p2[4]) << " " << (p1[5] == 'X' ? p1[5] : p2[5]) << "\n";
    std::cout << "c"
              << " " << (p1[6] == 'X' ? p1[6] : p2[6]) << " " << (p1[7] == 'X' ? p1[7] : p2[7]) << " " << (p1[8] == 'X' ? p1[8] : p2[8]) << "\n";
}

int decide_start()
{
    srand(time(NULL));
    int p = std::rand() % 2 + 1;
    std::cout << "Player " << p << " starts!\n";
    return p;
}

void handle_input()
{
    std::cout << "Player" << player << ", enter coordinate:";
    std::cin >> move;
    std::cout << "\n";
    int locus;
    if (move == "a1")
    {
        locus = 0;
    }
    else if (move == "a2")
    {
        locus = 1;
    }
    else if (move == "a3")
    {
        locus = 2;
    }
    else if (move == "b1")
    {
        locus = 3;
    }
    else if (move == "b2")
    {
        locus = 4;
    }
    else if (move == "b3")
    {
        locus = 5;
    }
    else if (move == "c1")
    {
        locus = 6;
    }
    else if (move == "c2")
    {
        locus = 7;
    }
    else if (move == "c3")
    {
        locus = 8;
    }
    else
    {
        std::cout << "Invalid input! (enter between a1-c3)\n";
        Sleep(2000);
        switch_player();
        return;
    }

    if (player == 1)
    {
        if (p1[locus] != ' ' || p2[locus] != ' ')
        {
            switch_player();
            std::cout << "Wrong place! Again!\n";
            Sleep(2000);
        }
        else
        {
            p1[locus] = 'X';
        }
    }
    else
    {
        if (p2[locus] != ' ' || p1[locus] != ' ')
        {
            switch_player();
            std::cout << "Wrong place! Again!\n";
            Sleep(2000);
        }
        else
        {
            p2[locus] = 'O';
        }
    }
}
int determine_winner()
{
    if ((p1[0] == 'X' && p1[1] == 'X' && p1[2] == 'X') || (p1[3] == 'X' && p1[4] == 'X' && p1[5] == 'X') ||
        (p1[6] == 'X' && p1[7] == 'X' && p1[8] == 'X') || (p1[0] == 'X' && p1[3] == 'X' && p1[6] == 'X') ||
        (p1[1] == 'X' && p1[4] == 'X' && p1[7] == 'X') || (p1[2] == 'X' && p1[5] == 'X' && p1[8] == 'X') ||
        (p1[0] == 'X' && p1[4] == 'X' && p1[8] == 'X') || (p1[2] == 'X' && p1[4] == 'X' && p1[6] == 'X') ||
        (p2[0] == 'O' && p2[1] == 'O' && p2[2] == 'O') || (p2[3] == 'O' && p2[4] == 'O' && p2[5] == 'O') ||
        (p2[6] == 'O' && p2[7] == 'O' && p2[8] == 'O') || (p2[0] == 'O' && p2[3] == 'O' && p2[6] == 'O') ||
        (p2[1] == 'O' && p2[4] == 'O' && p2[7] == 'O') || (p2[2] == 'O' && p2[5] == 'O' && p2[8] == 'O') ||
        (p2[0] == 'O' && p2[4] == 'O' && p2[8] == 'O') || (p2[2] == 'O' && p2[4] == 'O' && p2[6] == 'O'))
    {   
        switch_player();
        std::cout << "Congratulations, Player" << player << "!\n";
        winner = 3;
    }
    int sum = 0;
    for (int i = 0; i < p1.size(); i++)
    {
        if (p1[i] != ' ' || p2[i] != ' ')
        {
            sum++;
        }
    }

    if (sum == 9)
    {
        std::cout << "It's a tie!!!\n";
        winner = 3;
    }
    return winner;
}
void switch_player()
{
    if (player == 1)
    {
        player = 2;
    }
    else
    {
        player = 1;
    }
}