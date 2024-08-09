#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int updated_pop = start_size;

    if (start_size < end_size)
    {
        do
        {
            updated_pop = updated_pop + (updated_pop / 3) - (updated_pop / 4);
            years++;
        }
        while (updated_pop < end_size);
    }

    // TODO: Print number of years

    printf("Years: %i\n", years);
}
