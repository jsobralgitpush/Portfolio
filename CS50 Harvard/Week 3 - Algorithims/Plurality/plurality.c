#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);



int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (vote(name) == false)
        {
            printf("Invalid vote.\n");
        }
    }


    // // Debug: Checking the number of votes
    // for (int i=0; i < candidate_count; i++)
    // {
    //     printf("O candidato %s teve %i votos\n", candidates[i].name, candidates[i].votes);
    // }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{


    // For i from the first to the last candidate
    for (int i = 0; i < candidate_count; i++)
    {
        
        // If candidate[i].name == name (if both names match)
        if (strcmp(candidates[i].name, name) == 0 )
        {
            // Add one vote to that candidate
            candidates[i].votes++;

            // Leave the function
            return true;
        }
        
    }

    // Gonna print "invalid vote"
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // index of the winner
    int winner = 0;
    int draw = 0;
    int index = 0;
    int index_winner = 0;


    // For i from the first to the last number of votes from each canditate
    for (int i = 0; i < candidate_count; i++)
    {
            if (candidates[i].votes > winner)
            {
                winner = candidates[i].votes;
                index_winner = i;
            }

    }

    // Checking or Draw
    for (int i = 0; i < candidate_count+1; i++)
    {
            if (candidates[i].votes == candidates[index_winner].votes)
            {
                draw++;
                if (strcmp(candidates[i].name, candidates[index_winner].name) != 0)
                {
                    index = i;
                }
            }

    }

    if (draw>1)
    {
        printf("%s\n%s\n", candidates[index].name, candidates[index_winner].name );
    } else
    {
        printf("%s\n", candidates[index_winner].name );
    }

}

