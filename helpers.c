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

// This function is in charge of calculation 
float getBlur(int height, int width, RGBTRIPLE image[height][width])
{
  	RBGTRIPLE average[height][width];
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
  
    RGBTRIPLE temporary[height][width];
    int index, count;

    for (index = 0; index < height; index++)
    {
        for (count = 0; count < width; count++)
        {
            temporary[index][count] = image[index][count];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int c = 0; c < width; c++)
        {
            int calculations = 0;
            float red = 0;
            float green = 0;
            float blue = 0;
            for (int rows = -1; rows < 2; rows++)
            {
                for (int columns = -1; columns < 2; columns++)
                {
                    if((i + columns >= height || i + columns < 0) || (c + rows >= width || c + rows < 0))
                    {

                    }
                    else
                    {
                        red += temporary[i+rows][c+columns].rgbtRed;
                        green += temporary[c+rows][columns+i].rgbtGreen;
                        blue += temporary[i+rows][c+columns].rgbtBlue;
                        calculations++;
                    }
                }
            }
            image[i][c].rgbtRed = round(red/ calculations);
            image[i][c].rgbtGreen = round(green / calculations);
            image[i][c].rgbtBlue = round(blue / calculations);

            image[i][c].rgbtRed = image[i][c].rgbtRed % 256;
            image[i][c].rgbtBlue = image[i][c].rgbtBlue % 256;
            image[i][c].rgbtGreen = image[i][c].rgbtGreen % 256;
        }
    }
    return;
}