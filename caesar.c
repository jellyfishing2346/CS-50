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
    int key, index, length; 
    string plaintext;
    
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
   
    // Design a key for ./caesar and determine length for ciphertext
    key = atoi(argv[1]);
    plaintext = get_string("Ciphertext: ");
    length = strlen(plaintext);
    char cypher[length + 1];
    
    // Rotate the ciphertext data
    for (index = 0; index < length; index++)
    {
        cypher[index] = rotate(plaintext[index], key);
    }
    
    // Null terminator
    cypher[index] = '\0';
    
    // Display ciphertext
    printf("ciphertext: %s", cypher);
}

// Evaluate input caesar key based on the number of digits
bool only_digits(string s)
{
    int length = strlen(s);
    for (int index = 0; index < length; index++)
    {
        if (!isdigit(s[index]))
        {
            return false; 
        }
    }
    return true; 
}

// Takes input for char and int as it falls between a to z and Z to A
char rotate(char p, int k)
{
    char c; 
    
    // If input is in range of A-Z
    if (isupper(p))
    {
        c = (p - 'A' + k) % 26 + 'A';
    }
    
    // If the input is in range of a-z
    else if (islower(p))
    {
        c = (p - 'a' + k) % 26 + 'a';
    }
    
    // Print the default statement
    else
    {
        c = p;
    }
    
    return c; 
}