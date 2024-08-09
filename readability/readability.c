#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string sentence);
int count_words(string sentence);
int count_sentences(string sentence);

int main(void)
{
    string sentence = get_string("Text: ");

    int letter_count = count_letters(sentence);
    int word_count = count_words(sentence);
    int sentence_count = count_sentences(sentence);

    // L is the average number of letters per 100 words. In this case, we likely won't have 100 words to go off by.
    float L = ((float) letter_count / word_count) * 100.0;
    // S is the average number of sentences per 100 words. In this case, we likely won't have 100 words to go off by.
    float S = ((float) sentence_count / word_count) * 100.0;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
        return 0;
    }
    if (index >= 16)
    {
        printf("Grade 16+\n");
        return 0;
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string sentence)
{
    int letters = 0;
    for (int i = 0; i < strlen(sentence); i++)
    {
        if (isalpha(sentence[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

int count_words(string sentence)
{
    int words = 1;
    for (int i = 0; i < strlen(sentence); i++)
    {
        if (sentence[i] == ' ')
        {
            words += 1;
        }
    }
    return words;
}

int count_sentences(string sentence)
{
    int sentences = 0;
    for (int i = 0; i < strlen(sentence); i++)
    {
        if (sentence[i] == '.' || sentence[i] == '!' || sentence[i] == '?')
        {
            sentences += 1;
        }
    }
    return sentences;
}
