#include <iostream>
#include <vector>
#include <cstdlib>
#include <time.h>
#include <string>
#include "ttt.hpp"

int main()

{

    intro();

    while (determine_winner() == 0)
    {
        handle_input();
        board_display();
        switch_player();
    }
}
