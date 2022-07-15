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
    RGBTRIPLE temporary_image[height][width];
    // Evaluate each row by the height
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            temporary_image[index][count] = image[index][count];
        }
    }
    
    // Evaluate each row by the height
    for (int h = 0; h < height; h++)
    {
        // Evaluate each column by the width
        for (int w = 0; w < width; w++)
        {
            int blue, green, red;
            float calculations;
            blue = green = red = calculations = 0; 
            

         
            // This pixel is for the upper left corner
            if (h > 0 && w > 0)
            {
                red += temporary_image[h - 1][w - 1].rgbtRed;
                green += temporary_image[h - 1][w - 1].rgbtGreen;
                blue += temporary_image[h - 1][w - 1].rgbtBlue;
                calculations++; 
            }
        
            // This pixel is for the top left
            if (h > 0 && w >= 0)
            {
                red += temporary_image[h - 1][w].rgbtRed;
                green += temporary_image[h - 1][w].rgbtGreen;
                blue += temporary_image[h - 1][w].rgbtBlue;
                calculations++; 
            }
         
            // This pixel is for the top right
            if (h >= 0 && w > 0)
            {
                red += temporary_image[h][w - 1].rgbtRed;
                green += temporary_image[h][w - 1].rgbtGreen;
                blue += temporary_image[h][w - 1].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the bottom edge
            if (h >= 0 && w + 1 < width)
            {
                red += temporary_image[h][w + 1].rgbtRed;
                green += temporary_image[h][w + 1].rgbtGreen;
                blue += temporary_image[h][w + 1].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the top edge
            if (h - 1 >= 0 && w + 1 < width)
            {
                red += temporary_image[h - 1][w + 1].rgbtRed;
                green += temporary_image[h - 1][w + 1].rgbtGreen;
                blue += temporary_image[h - 1][w + 1].rgbtBlue;
                calculations++;
            }

            // The pixels for the right edge
            if (h + 1 < height && w - 1 < width))
            {
                red += temporary_image[h + 1][w - 1].rgbtRed;
                green += temporary_image[h + 1][w - 1].rgbtGreen;
                blue += temporary_image[h + 1][w - 1].rgbtBlue;
                calculations++;
            }
         
            // The middle pixels
            if (h + 1 < height && w + 1 < width)
            {
                red += temporary_image[h + 1][w + 1].rgbtRed;
                green += temporary_image[h + 1][w + 1].rgbtGreen;
                blue += temporary_image[h + 1][w + 1].rgbtBlue;
                calculations++;
            }
            // This pixel is for the bottom right
            red += temporary_image[h][w].rgbtRed;
            green += temporary_image[h][w].rgbtGreen;
            blue += temporary_image[h][w].rgbtBlue;
            calculations++; 
                
            // The average amount for colors
            image[h][w].rgbtRed = round(red / calculations);
            image[h][w].rgbtGreen = round(green / calculations);
            image[h][w].rgbtBlue = round(blue / calculations);
        }
        return;
    }
}