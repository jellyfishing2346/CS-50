#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[]) 
{
    int index, count; 
    if (argc != 2)
    {
        // Error message for ./caesar key
        printf("Usage: ./caesar key\n");
        return 1; 
    }
    
    for (index = 0; index < strlen(argv[1]); index++)
    {
        // If the ./caesar key uses a digit 
        if (!isdigit(argv[1][index]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    
    // Design a key for ./caesar
    int key = atoi(argv[index]);
    
    // Display ciphertext after input from plaintext
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext: ");
    
    // Determine the condition for plaintext 
    for (count = 0; count < strlen(plaintext); count++)
    {
    
        // If plaintext is uppercase print this condition   
        if (isupper(plaintext[count]))
        {
            printf("%c", (plaintext[count] - 65 + key) % 26 + 65);
        }
    
        // Otherwise if plaintext is lowercase print this condition instead      
        else if (islower(plaintext[count]))
        {
            printf("%c", (plaintext[count] - 97 + key) % 26 + 97);
        }
    
        // If both cases fail print this default case instead     
        else
        {
            printf("%c", plaintext[count]);
        }
    }
    printf("\n");
}