#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Card error\n");
        return 2;
    }

    uint8_t buffer[512];

    int jpg_count = 0;

    char filename[8];
    FILE *img = NULL;

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {

            if (img != NULL)
            {
                fclose(img);
                jpg_count++;
            }

            sprintf(filename, "%03i.jpg", jpg_count);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                return 3;
            }
        }

        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);
}
