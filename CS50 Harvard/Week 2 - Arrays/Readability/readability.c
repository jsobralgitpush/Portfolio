#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Calling the text string
    string text = get_string("Text: ");

    // Counter

        // letters
        int num_letters =0;

        // words
        int num_words =0;

        // sentences
        int num_sentences =0;


    // Verifying each of the letters of the text
    for (int i=0; text[i] != '\0';i++)
    {
        if (text[i] == ' ')
        {
            num_words++;
        } else if (text[i] >= 'a' && text[i] <= 'z')
        {
            num_letters++;
        } else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            num_letters++;
        } else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            num_sentences++;
        }


    }

    // Add 1 to num_word
    num_words++;


    // Calculate the grade
    float var_l = 100*num_letters/num_words;
    float var_s = 100*num_sentences/num_words;
    float index = 0.0588*var_l -0.296*var_s  - 15.8;


    // printing the grade
    if (index > 16)
    {
        printf("Grade 16+\n");
    } else if (index < 1)
    {
        printf("Before Grade 1\n");
    } else
    {
        printf("Grade %i\n", (int) index);
    }


    // Debug
    // printf("letters: %i\n", num_letters);
    // printf("sentences: %i\n", num_sentences);
    // printf("words: %i\n", num_words);
    // printf("var_l: %f\n", var_l);
    // printf("var_s: %f\n", var_s);

}
