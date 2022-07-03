// Include libraries
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// Function prototypes
bool only_digits(string s);
char rotate(char p, int k);

int main(int argc, string argv[]) 
{
    int key, index;
    int length = 0;
    string plaintext; 
    
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    else
    {
        return 0;
    }
   
    key = atoi(argv[1]);
    plaintext = get_string("plaintext: ");
    char cypher[length + 1];
    for (index = 0; index < length; index++)
    {
        cypher[index] = rotate(plaintext[index], key);
    }
    cypher[index] = '\0';
    
    
    printf("ciphertext: %s\n", cypher);
}

bool only_digits(string s)
{
    int index;
    int length = strlen(s);
    for (index = 0; index < length; index++)
    {
        if(!isdigit(index))
        {
            return false; 
        }
    }
    return true; 
}

char rotate(char p, int k)
{
    char c; 
    if (isupper(p))
    {
        c = (p - 'A' + k) % 26 + 'A';
    }
    
    else if (islower(p))
    {
        c = (p - 'a' + k) % 26 + 'a';
    }
    
    else
    {
        c = p; 
    }
    
    return c; 
}    