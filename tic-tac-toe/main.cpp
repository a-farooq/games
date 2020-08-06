//
//  main.cpp
//  tic-tac-toe
//
//  Created by Aamil Farooq on 06/08/20.
//  Copyright © 2020 Aamil Farooq. All rights reserved.
//

#include <iostream>

using namespace std;
class Player
{
    char symbol;
public:
    Player(char a) : symbol(a)
    {
        srand(time_t(NULL));
    }
    char getSymbol()
    {
        return symbol;
    }
    
    void getLoc(short &x, short &y)
    {
        x = rand()%3;
        y = rand()%3;
    }
};

class Game
{
    char grid[3][3];
    int fill;
    bool over;
    
public:
    void drawBoard()
    {
        for(auto i = 0; i < 3; i++) {
            cout << "| ";
            for(auto j = 0; j < 3; j++)
                cout << grid[i][j] << " | ";
            cout << endl;
        }
        cout << "==========================" << endl;
    }
    void makeMove(Player *p)
    {
        short x, y;
        p->getLoc(x, y);
        
        while(!IsValidMove(x, y))
        {
            p->getLoc(x, y);
        }
        ++fill;
        grid[x][y] = p->getSymbol();
        
        if(IsSameThreeInLine(x, y))
        {
            over = true;
        }
    }
    
    bool IsSameThreeInLine(short x, short y)
    {
        if(checkRow(x) || checkCol(y) || checkDiag(x, y))
            return true;
        
        return false;
    }
    
    bool checkRow(short x)
    {
        if(grid[x][0] == grid[x][1] && grid[x][0] == grid[x][2])
            return true;
        return false;
    }
    
    bool checkCol(short y)
    {
        if(grid[0][y] == grid[1][y] && grid[0][y] == grid[2][y])
            return true;
        return false;
    }
    
    bool checkDiag(short x, short y)
    {
        bool flag = false;
        
        switch(abs(x-y)) {
            case 0:
                if(grid[0][0] == grid[1][1] && grid[0][0] == grid[2][2])
                    flag = true;
                break;
            case 1:
                break;
            case 2:
                if(grid[0][2] == grid[1][1] && grid[0][2] == grid[2][0])
                    flag = true;
                break;
        }
        return flag;
    }
    
    bool IsValidMove(short x, short y)
    {
        if(x < 0 || y < 0 || x > 2 || y > 2) return false;
        
        if(grid[x][y] == 'o' || grid[x][y] == 'x') return false;
        
        return true;
    }
    
    Game()
    {
        over = false;
        fill = 0;
        memset(grid, '-', 3*3);
    }
    
    bool IsBoardFull()
    {
        return fill == 3*3 ? true : false;
    }
    
    bool IsOver()
    {
        return over;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    Player *p1 = new Player('o');
    Player *p2 = new Player('x');
    
    Game game;
    
    Player *cur = p1;
    
    while(!game.IsBoardFull())
    {
        game.makeMove(cur);
        game.drawBoard();
        
        if(game.IsOver()) {
            cout << cur->getSymbol() << " wins" << endl;
            break;
        }
        else cur = (cur == p1 ? p2 : p1);
    }
    
    game.drawBoard();
    
    delete p1;
    delete p2;
    
    return 0;
}
