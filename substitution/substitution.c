#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc < 2 || argc > 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters\n");
        return 1;
    }

    for (int h = 0; h < strlen(argv[1]); h++)
    {
        if (!isalpha(argv[1][h]))
        {
            printf("It should all be letters\n");
            return 1;
        }
    }

    string key = argv[1];

    for (int j = 0; j < strlen(key); j++)
    {
        key[j] = tolower(key[j]);
    }

    int frequency[128] = {0};

    //Checks if the key has a duplicate letter
    for (int i = 0; i < strlen(key); i++)
    {
        if (frequency[(unsigned char) key[i]] == 1)
        {
            printf("Duplicate found\n");
            return 1;
        }
        else
        {
            frequency[(unsigned char) key[i]]++;
        }
    }

    char alphabet[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

    string plaintext = get_string("plaintext: ");
    //Initializes an array called ciphertext.
    char ciphertext[strlen(plaintext)];

    for (int k = 0; k < strlen(plaintext); k++)
    {
        if (isalpha(plaintext[k]))
        {
            int uppercase = 0;
            if (isupper(plaintext[k]))
            {
                uppercase = 1;
            }
            plaintext[k] = tolower(plaintext[k]);
            int position = 0;
            for (int n = 0; n < 26; n++)
            {
                if (plaintext[k] == alphabet[n])
                {
                    position = n;
                    break;
                }
            }
            ciphertext[k] = key[position];
            // Uppercases letters that were uppercased in plaintext.
            if (uppercase == 1)
            {
                ciphertext[k] = toupper(ciphertext[k]);
            }
        }
        // Else condition keeps anything but letters the same.
        else
        {
            ciphertext[k] = plaintext[k];
        }

        if (k == strlen(plaintext) - 1)
        {
            int null = k + 1;
            ciphertext[null] = '\0';
        }
    }
    printf("ciphertext: %s\n", ciphertext);
}
