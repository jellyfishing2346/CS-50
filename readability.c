#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>

int main(void) 
{
    // Prompt the user to enter a string for text
    string text = get_string("Text: ");
    int index;
    int letters = 0;
    int words = 1;
    int sentences = 0; 
    
    // Going through the structure of the user's string
    for (index = 0; index < strlen(text); index++)
    {
        // The alphabet would return the number of letters
        if (isalpha(text[index]))
        {
            letters++;
        }
        
        // The space would return the number of words
        else if (text[index] == ' ')
        {
            words++;
        }
        
        // The .,?, and ! return the number of sentences after each expression
        else if (text[index] == '.' || text[index] == '?' || text[index] == '!')
        {
            sentences++;
        }
    } 
    // Determining the number of letters and sentences
    float L = (float) letters / (float) words * 100;
    float S = (float) sentences / (float) words * 100;
        
    // Round the amount from the calculations
    index = round(0.0588 * L - 0.296 * S - 15.8);
        
    // If the index is less than 1 the user is in Grade 1
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
        
    // Otherwise, the index is greater than 16 the user is in Grade 16+
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
        
    // Display a default statement
    else
    {
        printf("Grade %i\n", index);
    }
}