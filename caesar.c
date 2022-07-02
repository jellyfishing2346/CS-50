#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[]) 
{
    int index;
    // Check if there is a command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
    }
    else printf("Success!\n");
    
    // Design a key
    string key = argv[1];
    
    // Checking if the input is a digit
    for (index = 0; index < strlen(argv[1]); index++)
    {
        if (!isdigit(argv[1][index]))
        {
        printf("Usage: ./caesar key\n");
        return 1;
        }
    }
    printf("Success\n%s\n", key);
    
    // Retrieve plaintext from the user
    string plaintext = get_string("plaintext: ");
    
    // Convert the key to an integer
    int integer_key = atoi(key);
    printf("ciphertext: ");
    
    // Retrieve the ciphertext
    for (int count = 0; count < strlen(plaintext); count++)
    {
        if (isupper(plaintext[index]))
        {
            printf("%c", (((plaintext[index] - 65) + integer_key) %26 ) + 65);
        }
        
        else if (islower(plaintext[index]))
        {
            printf("%c", (((plaintext[index] - 97) + k) %26 ) + 97);
        }
        
        else 
        {
            printf("%c", plaintext[index]);
        }
    }
    printf("\n");
}