#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // We add the .5 since if the average after dividing is a decimal, it will truncate properly.
            // Ex: It will go from 109.6 -> 200.1 -> 200, and not 109.6 -> 109
            average = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0 + 0.5;

            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue));
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            int sepiaGreen = round((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue));
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            int sepiaBlue = round((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue));
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int k = 0;
        for (int j = 1; j < width; j++)
        {
            RGBTRIPLE tmp = image[i][k];
            image[i][k] = image[i][width - j];
            image[i][width - j] = tmp;

            // If conditon is for even number.
            if (width % 2 == 0)
            {
                if (k + 1 == width - j)
                {
                    break;
                }
            // Else condition is if the width is an odd number.
            else
            {
                if (k == width - j)
                {
                    break;
                }
            }
            }
            k++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int total_green = 0;
            int total_red = 0;
            int total_blue = 0;
            int pixels = 0;
            for (int k = -1; k < 2; k++)
            {

                for (int l = -1; l < 2; l++)
                {
                    int row = i + k;
                    int col = j + l;

                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        pixels = pixels + 1;
                        int tmp_green = image_copy[row][col].rgbtGreen;
                        int tmp_blue = image_copy[row][col].rgbtBlue;
                        int tmp_red = image_copy[row][col].rgbtRed;

                        total_green += tmp_green;
                        total_blue += tmp_blue;
                        total_red += tmp_red;
                    }
                    // In a grid of 9 pixels, if the bottom right pixel is reached:
                    if (k == 1 && l == 1)
                    {
                        int green = round((double) total_green / pixels);
                        int blue = round((double) total_blue / pixels);
                        int red = round((double) total_red / pixels);
                        image[i][j].rgbtGreen = green;
                        image[i][j].rgbtBlue = blue;
                        image[i][j].rgbtRed = red;
                    }
                }
            }
        }
    }
    return;
}
