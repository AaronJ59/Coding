#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    int hashtags = 1;
    int spacechange = height;

    for (int i = 0; i < height; i++)
    {
        int spaces = spacechange - 1;
        // To print spaces
        for (int j = 0; j < spaces; j++)
        {
            printf(" ");
        }
        // print the hashtags on the left side
        for (int k = 0; k < hashtags; k++)
        {
            printf("#");
        }
        // print the two spaces between the hashtags
        for (int l = 0; l < 1; l++)
        {
            printf("  ");
        }
        // print the hashtags on the right side
        for (int m = 0; m < hashtags; m++)
        {
            printf("#");
        }

        printf("\n");
        hashtags++;
        spacechange--;
    }
}
