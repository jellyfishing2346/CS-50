// Include libraries
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function prototype
int checkTheKey(int argc, char* k);

int main(int argc, char** argv)
{
    char* n = argv[1];
    int m = argc;
    int key = checkTheKey(m, n);
    
    // if caesar key equals 0 print the following message
    if (key == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1; 
    }
    
    else
    {
        // Prompt the user to enter a string to plaintext
        char* plaintext = get_string("plaintext: ");
        int index, length;
        
        // Display the ciphertext 
        printf("ciphertext: ");
        for (index = 0, length = strlen(plaintext); index < length; index++)
        {
            // Display this text if plaintext is lower
            if (islower(plaintext[index]))
            {
                printf("%c", (plaintext[index] - 97 + key) % 26 + 97);
            }
            
            // Display this text if plaintext is higher
            else if (isupper(plaintext[index]))
            {
                printf("%c", (plaintext[index] - 65 + key) % 26 + 65);
            }
        
            // Otherwise, display the default statement
            else
            {
                printf("%c", plaintext[index]);
            }
        }
        
        // Print on a separate line
        printf("\n");
        return 0; 
    }
}

// Creating a key containing an int and a string
int checkTheKey(int argc, char* k)
{
    int digit = argc; 
    char* key = k;
    
    if (argc != 2)
    {
        return 0;
    }
    
    else
    {
        for (int i = 0; i < strlen(key); i++)
        {
          if (!isdigit(key[i]))
            {
              return 0; 
			}
        }
        // Design a digital key
        int digitalkey = atoi(key);
         
        printf("%d\n", digitalkey);
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