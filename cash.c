// Include libraries
#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollar;
    do
    {
        // Prompt the user to enter the amount of change they owe
        dollar = get_float("Change owed: ");
    }
    // This occurs is dollars is less than or equal to 0
    while (dollar <= 0);
    
    int cents = round(dollar*100);
    int coins = 0;
    
    // Subtract the number of cents if the user enters 25 cents or greater
    while (cents >= 25)
    {
        cents -= 25; 
        coins++;
    }
    
    // Subtract the number of cents if the user enters 10 cents or greater
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }
    
    // Subtract the number of cents if the user enters 5 cents or greater
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }
    
    // Subtract the number of cents if the user enters 1 cent or greater
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }
    
    // Tell the user how much coins they need to pay
    printf("You will need at least %i coins", coins);
}