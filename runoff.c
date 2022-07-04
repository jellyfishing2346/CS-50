#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // Count the number of candidate votes
    for (int index = 0; index < candidate_count; index++)
    {
        // Compare the candidate's name and their votes
        if (strcmp(candidates[index].name, name) == 0)
        {
            // Determine the voter's name and their rank
            preferences[voter][rank] = index;
            return true; 
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // Count the number of votes from the votes
    for (int index = 0; index < voter_count; index++)
    {
        // Count the number of votes that were received by candidates
        for (int count = 0; count < candidate_count; count++)
        {
            int candidate_index = preferences[index][count];
            // If the following candidates aren't eliminated increment the voter count
            if (candidates[candidate_index].eliminated == false)
            {
                // Increment the preferred candidate and their count of votes
                candidates[candidate_index].votes ++;
                break; 
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // Calculate the maximum number of voters
    float max = (float)voter_count / 2 + 1;
    
    // Count the number of votes from the votes
    for (int index = 0; index < candidate_count; index++)
    {
        // If number of candidate votes greater than half of voter count
        if (candidates[index].votes > max)
        {
            // Display the winning candidate's name
            printf("%s\n", candidates[index].name);
            return true; 
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int min = MAX_VOTERS;
    
    // Count the number of candidate votes
    for (int index = 0; index < candidate_count; index++)
    {
        // Determine which candidate's votes equal the minimum number of votes
        if (!candidates[index].eliminated && candidates[index].votes < min)
        {
            // This candidate will receive the minimum number of votes
            min = candidates[index].votes;
        }
    }
    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // Count the number of candidate votes
    for (int index = 0; index < candidate_count; index++)
    {
       // If the 
       if (candidates[index].eliminated == false && candidates[index].votes != min)
       {
           return false; 
       }
    }
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // Count the number of candidate votes
    for (int index = 0; index < candidate_count; index++)
    {
        // If the candidate votes are the minimum amount
        if (candidates[index].eliminated  == min)
        {
            // Then the number of candidates eliminated is true
            candidates[index].eliminated = true;
        }
    }
    return;
}
