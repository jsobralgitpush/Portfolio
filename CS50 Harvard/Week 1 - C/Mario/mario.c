#include <cs50.h>
#include <stdio.h>

void space(int n);
void hashes(int n);

int main(void)
{
    // Get the Height from user
    int i;
    int n;
    do
    {
        n = get_int("Height:");
    }    
    while(n<=0 || n>8);


    // Print Hashes
    for (i=1;i< (n+1);i++)
    {
            // Left blocks
            space(n-i);
            hashes(i);

            // Right blocks
            space(2);
            hashes(i);

            // New line
            printf("\n");
    }
}

// Space function
void space(int n)
{
    for (int i=0; i<n;i++ )
    {
        printf(" ");
    }
}

// Hashes function
void hashes(int n)
{
    for (int i=0; i<n;i++ )
    {
        printf("#");
    }
}
