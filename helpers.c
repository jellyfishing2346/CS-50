#include "helpers.h"
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
            sepiaRed = .393 * image[index][count].rgbtRed + .769 * image[index][count].rgbtGreen + .189 * image[index][count].rgbtBlue;
         	sepiaGreen = .349 * image[index][count].rgbtRed + .686 * image[index][count].rgbtGreen + .168 * image[index][count].rgbtBlue;
			sepiaBlue = .272 * image[index][count].rgbtRed + .534 * image[index][count].rgbtGreen + .131 * image[index][count].rgbtBlue;
            image[index][count].rgbtRed = sepiaRed > 255 ? 255: sepiaRed;
            image[index][count].rgbtGreen = sepiaGreen > 255 ? 255: sepiaGreen;
            image[index][count].rgbtBlue = sepiaBlue > 255 ? 255: sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
     RGBTRIPLE original_image[height][width];
     // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            original_image[index][count] = image[index][count];
        }
    }
    return;
    
     // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            image[index][count] = image[index][count];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE original_image[height][width];
    
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            original_image[index][count] = image[index][count];
        }
    }
    
    int totalRed, totalGreen, totalBlue; 
    totalRed = totalGreen = totalBlue = 0;
    
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            // Count the rows
            for (int i = index - 1; i <= index + 1; i++)
            {
                // Count the columns
                for (int c = count - 1; c <= count + 1; c++)
                {
                    if (c < width && index < height && c >= 0 && index >= 0)
                    {
                    totalRed += original_image[i][c].rgbtRed;
                    totalGreen += original_image[i][c].rgbtGreen;
                    totalBlue += original_image[i][c].rgbtBlue;
                    }
                }
            }
            image[index][count].rgbtRed = round(totalRed / count);
            image[index][count].rgbtGreen = round(totalGreen / count);
            image[index][count].rgbtBlue = round(totalBlue / count);
            int total = 0;
        }
    }
    return;
}
