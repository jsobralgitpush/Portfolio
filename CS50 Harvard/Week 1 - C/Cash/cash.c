#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Number of coins
    int coins = 0;
    float change;

    // Get the users change
    do
    {
        change = get_float("Change owed: ");
    }
    while (change <0) ;

    // Numbers of coins
    do 
    {
        if (change>=0.25)
        {
            coins = coins + 1;
            change = change -0.25;
        } else if (change>=0.10)
        {
            coins = coins + 1;
            change = change -0.10;
        } else if (change>=0.05)
        {
            coins = coins + 1;
            change = change -0.05;
        } else
        {
            coins = coins + 1;
            change = change - 0.01;
        } 

    }
    while (change>=0.009999999999999999999999999999999999);

    printf("%d \n", coins);
}
