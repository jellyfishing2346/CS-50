#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            int total = round((image[index][count].rgbtRed + image[index][count].rgbtGreen + image[index][count].rgbtBlue) / 3.0);
            image[index][count].rgbtRed = image[index][count].rgbtGreen = image[index][count].rgbtBlue = total;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed, sepiaBlue, sepiaGreen;
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            sepiaRed = round(.393 * image[index][count].rgbtRed + .769 * image[index][count].rgbtGreen + .189 * image[index][count].rgbtBlue);		
            sepiaGreen = round(.349 * image[index][count].rgbtRed + .686 * image[index][count].rgbtGreen + .168 * image[index][count].rgbtBlue);
            sepiaBlue = round(.272 * image[index][count].rgbtRed + .534 * image[index][count].rgbtGreen + .131 * image[index][count].rgbtBlue);
            image[index][count].rgbtRed = sepiaRed > 255 ? 255 : sepiaRed;
            image[index][count].rgbtGreen = sepiaGreen > 255 ? 255 : sepiaGreen;
            image[index][count].rgbtBlue = sepiaBlue > 255 ? 255 : sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    BYTE temp[3];
    RGBTRIPLE original_image[height][width];
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width / 2; count++)
        {
            temp[0] = image[index][count].rgbtBlue;
            temp[1] = image[index][count].rgbtGreen;
            temp[2] = image[index][count].rgbtRed;
          
            image[index][count].rgbtBlue = image[index][width - count - 1].rgbtBlue;
            image[index][count].rgbtGreen = image[index][width - count - 1].rgbtGreen;
            image[index][count].rgbtRed = image[index][width - count - 1].rgbtRed;
          
            image[index][width - count - 1].rgbtBlue = temp[0];
            image[index][width - count - 1].rgbtGreen = temp[1];
            image[index][width - count - 1].rgbtRed = temp[2];
          
        }
    }
  
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  
    RGBTRIPLE temporary[height][width];

    for (int h = 0; h < height; h++)
    {
        for (int w = 0; w < width; w++)
        {
            temporary[h][w] = image[h][w];
        }
    }

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            int count = 0;
            float red = 0;
            float green = 0;
            float blueaddup = 0;
            for (int r = -1; r < 2; r++)
            {
                for (int s = -1; s < 2; s++)
                {
                    if((y + r > height || y + r < 0) || (x + s > width || x + s < 0))
                    {

                    }
                    else
                    {
                        red += copy[y+r][x+s].rgbtRed;
                        green += copy[y+r][x+s].rgbtGreen;
                        blue += copy[y+r][x+s].rgbtBlue;
                        count++;
                    }
                }
            }
            image[y][x].rgbtRed = round(redaddup / count);
            image[y][x].rgbtGreen = round(greenaddup / count);
            image[y][x].rgbtBlue = round(blueaddup / count);

            image[y][x].rgbtRed = image[y][x].rgbtRed % 256;
            image[y][x].rgbtBlue = image[y][x].rgbtBlue % 256;
            image[y][x].rgbtGreen = image[y][x].rgbtGreen % 256;
        }
    }
    return;
}