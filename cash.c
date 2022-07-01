// Include libraries
#include <stdio.h>
#include <cs50.h>
#include <math.h>

// Function prototypes
int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

// Ask the user for the amount of change they owe
int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
    return cents;
}

// Calculate the change on quarters
int calculate_quarters(int cents)
{
    int quarters = 0;
    while (cents >= 25)
    {
        cents = cents - 25;
        quarters++;
    }
    return quarters; 
}

// Calculate the change on dimes
int calculate_dimes(int cents)
{
    int dimes = 0;
    while (cents >= 10)
    {
        cents = cents - 10;
        dimes++;
    }
    return dimes;
}

// Calculate the change on nickels
int calculate_nickels(int cents)
{
    int nickels = 0;
    while (cents >= 5)
    {
        cents = cents - 5; 
        nickels++;
    }
    return nickels;
}

// Calculate the change on pennies
int calculate_pennies(int cents)
{
    int pennies = 0;
    while (cents >= 1)
    {
        cents = cents - 1;
        pennies++;
    }
    return pennies; 
}

int main(void)
{
    // Telling the user the amount of change they owe
    int cents = get_cents();
    
    // How many quarters to give to the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;
    
    // How many dimes to give to the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;
    
    // How many nickels to give to the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;
    
    // How many pennies to give to the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;
    
    // The total sum of coins
    int coins = quarters + dimes + nickels + pennies;
    
    // Print the total sum of coins
    printf("%i\n", coins);
}