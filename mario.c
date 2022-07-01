// Include libraries
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height, row, column, space;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    
    // Display the number of rows
    for (row = 0; row < height; row++)
    {
        // Display the number of spaces
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        // Display the number of #s with the columns
        for (column = 0; column <= row; column++)
        {
            printf("#");
        }
        printf("\n");
    }
}