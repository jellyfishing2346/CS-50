// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// The following variables
unsigned int hash_amount;
unsigned int count = 0; 
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Specify the node
    hash_amount = hash(word);
    node *locate = table[hash_amount];
    
    // Evaluate node through linked list
    while (locate != 0)
    {
        if (strcmp(word, locate->word) == 0)
        {
            return true;
        }
        locate = locate->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Evaluate word calculations through this for looop
    unsigned long calculations = 0;
    for (int index = 0; index < strlen(word); index++)
    {
        calculations += tolower(word[index]);
    }
    return calculations % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *memory = fopen(dictionary, "r");
    
    // If the memory pointer is at NULL, then the file can't be opened
    if (memory == NULL)
    {
        printf("This file can't be opened %s\n", dictionary);
        return false;
    }
    
    // Create a variable called word and track with count
    char word[LENGTH + 1];
    
    
    // Scan the dictionary for each possible word
    while (fscanf(memory, "%s", word) != EOF)
    {
        // Create a node to allocate memory
        node *numbers = malloc(sizeof(node));
        
        // If the node is NULL, return false
        if (numbers == NULL)
        {
            return false; 
        }
        
        // Copy each word into the node
        strcpy(numbers->word, word);
        hash_amount = hash(word);
        numbers->next = table[hash_amount];
        table[hash_amount] = numbers;
        count++;
    }
    fclose(memory);
    return true;
    
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Return count if count is greater than 0
    if (count > 0)
    {
        return count; 
    }
    
    return 0; 
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Evaluate this loop for N
    for (int index = 0; index < N; index++)
    {
        // Set this node to memory location
        node *locate = table[index];
        
        // If the node is not Null, execute this statement
        while (locate != NULL)
        {
            // Design a temporary node 
            node *temporary = locate;
            
            // Move the locate node to the next node
            locate = locate->next; 
            
            // Release the temporary node
            free(temporary);
        }
        
        // If the locate node is Null, execute this statement
        if (locate == NULL && index = N - 1)
        {
            return true;
        }
    }
    return false;
}
