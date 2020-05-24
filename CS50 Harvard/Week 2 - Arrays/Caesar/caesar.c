#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>


int main(int argc, string argv[])
{
    
    if (argc < 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    if (argc >2 )
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    string d = argv[1];
    
    for (int ct = 0; argv[1][ct] != '\0'; ct++ )
    {
        if (argv[1][ct] >= 65 && argv[1][ct] <= 122 )
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    
    // Convert key from string to int
    int key = atoi(argv[1]);

    // Testing argc
    if (key >=1 && key <=1000)
    {
        // Calling the text
        string plaintext = get_string("Plaintext: ");


        printf("ciphertext: ");

        // Encrypt the code
        for (int i=0; plaintext[i] !='\0'; i++)
        {

            // help debugg
            char w = (int) plaintext[i];
            char a = w + key;


            if (isalpha(plaintext[i]) == 0)
            {

                printf("%c", plaintext[i]);

            } else
            {

                if ( isupper(plaintext[i]) == 0)
                {


                    if (a > 122)
                    {
                        a = a - 122 + 96;
                        printf("%c", a);

                    } else if (a < 0)
                    {
                        a = key - a;
                        printf("c");
                        
                    } else
                    {
                        printf("%c", a);
                    }

                } else
                {
                    if (a > 90)
                    {
                        a = a - 90 + 64;
                        printf("%c", a);

                    }  else if (a < 0)
                    {
                        char b = w + key - 60;
                        b = b - 90 + 64 + 60;
                        printf("%c", b);
                    } else
                    {
                        printf("%c", a);
                    }
                }



            }
        }


    } else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    printf("\n");

}