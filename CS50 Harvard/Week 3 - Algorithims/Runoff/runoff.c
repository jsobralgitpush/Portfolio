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

        // // debug: Jose Sobral 25/04
        // for (int i =0; i < candidate_count; i++)
        // {
        //     printf("O numero de votos de %s é %i", candidates[i].name, candidates[i].votes);
        // }


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
    // voter = número de pessoas que estarão votando
    // rank = número de candidatos
    // name = nome do candidato

   for (int i=0; i < candidate_count; i++)
   {
        if (strcmp(name, candidates[i].name) == 0)
        {
            // Updating the matrix preferences for the index of the candidate
            preferences[voter][rank] = i ;
            return true;
        }
   }

    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    int index_a = 0;


    for (int j = 0; j < voter_count; j++)
    {

        if (candidates[preferences[j][index_a]].eliminated == false)
        {
            candidates[preferences[j][index_a]].votes++;
            index_a = 0;
        } else
        {
            index_a++;
            j = j -1;
        }

    }


    // for (int i =0; i < voter_count; i++)
    // {
    //     printf("O número de votes de %s é %i\n", candidates[i].name, candidates[i].votes);
    // }

}

// Print the winner of the election, if there is one
bool print_winner(void)
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
    for (int i = 0; i < candidate_count; i++)
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
        return false;
    } else if (winner > (((float) voter_count / 2)) +1)
    {
        printf("%s\n", candidates[index_winner].name );
        return true;
    } else
    {
        return false;
    }


}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{

    // Counters
    int index_min = 0;


    // Check if the candidate with the min votes
    for (int i=0; i < candidate_count; i++)
    {
        for (int j=0; j < candidate_count; j++)
        {
            if (candidates[i].votes < candidates[j].votes)
            {
                if (candidates[i].eliminated == false)
                {
                    index_min = i;
                }
            }
        }
    }

    // Return the number of votes of the min candidate
    return candidates[index_min].votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{

    // Contadores
    int count_tie = 0;
    int count_candidate_tie = 0;


    // Nesta função colocaremos o número minimo de votos da função anterior e precisamos saber se isso gera um empate


    // Count the number of tie candidates
    for (int i =0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            if (min == candidates[i].votes)
            {
                count_tie++;
            }
        }
    }


    // Count the numer of not eliminated candidates
    for (int i =0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            count_candidate_tie++;
        }
    }


    // Check if the min vote is equal of the number of remaining candidates
    if (count_tie == count_candidate_tie)
    {
        return true;
    } else
    {
        return false;
    }



}

// Eliminate the candidate (or candidiates) in last place
void eliminate(int min)
{
    // Eliminate the candidate which has the min number of votes
    for (int i =0; i < candidate_count; i++)
    {
        if (min == candidates[i].votes)
        {
            candidates[i].eliminated = true;
        }
    }

}
