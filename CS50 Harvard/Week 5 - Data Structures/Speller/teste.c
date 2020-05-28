#include <stdbool.h>
#include <ctype.h>
#include <stdio.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <stdlib.h>
#include <string.h>



#include "dictionary.h"


unsigned int hash(const char *word)
{
    // TODO
    // input: word, with alphabetical characters and possibly apostrophes
    // output: numeric index between 0 and N - 1

    int counter = 97;
    int fixid_counter = 97;
    
    while (true)
    {
        
        if (word[0] == (char) counter)
        {
            return (counter-fixid_counter); 
        } else 
        {
            counter++;
        }
        
    }

}

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];


int main (void)
{
    FILE *file = fopen("dictionaries/large", "r");
    
    
    char *p;
    p = malloc(sizeof(file));
    while (!feof(file))
        {
            fscanf(file,"%s",p);
            node *n = malloc(sizeof(node));
            strcpy(n -> word, p);
            n -> next =  NULL;
            
            strcpy(table[hash(p)] -> word, n -> word);

        }
        

//  while (!feof(file))
//         {
//                 fscanf(file,"%s",p);
//                 // if (strncmp((char) p[0] ,"a") == true)
//                 // {
//                 //     printf("Hello");
//                 // }
                
//                 if (p[0] == "a")
//                 {
//                     printf("nada");
//                 }
//         } 

}