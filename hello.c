// Include libraries
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Ask for the user for their name
    string name = get_string("What's your name \n");
    
    // Display the user's name
    printf("Hello, %s\n", name);
}