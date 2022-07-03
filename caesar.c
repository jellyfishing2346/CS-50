// Include libraries
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function prototype
int checkTheKey(int argc, string k);

int main(int argc, string argv[])
{
    string n = argv[1];
    int m = argc;
    int key = checkTheKey(m, n);
    
    if (key == 0)
    {
        printf("This key is invalid!\n");
        return 1; 
    }
    
    else
    {
        string plaintext = get_string("plaintext: ");
        int index, length;
        printf("ciphertext: ");
        for (index = 0, length = strlen(plaintext); index < length; index++)
        {
            if (islower(plaintext[index]))
            {
                printf("%c", (plaintext[index] - 97 + key) % 26 + 97);
            }
            
            else if (isupper(plaintext[index]))
            {
                printf("%c", (plaintext[index] - 65 + key) % 26 + 65);
            }
        
            else
            {
                printf("%c", plaintext[index]);
            }
        }
        printf("\n");
        return 0; 
    }
}
    
int checkTheKey(int argc, string k)
{
    int digit = argc; 
    string key = k;
    
    if (argc != 2)
    {
        return 0;
    }
    
    else
    {
        int digitalkey = atoi(key);
        if (digitalkey > 0)
        {
            return digitalkey;
        }
        else
        {
            return 0; 
        }
    }
}