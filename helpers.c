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
    for (int index = 0; index < height; index++)
    {
        // Evaluate each column by the width
        for (int count = 0; count < width; count++)
        {
            int blue, green, red;
            float calculations;
            blue = green = red = calculations = 0; 
            
            // This pixel is for the bottom right
            if (index >= 0 && count >= 0)
            {
                red += temporary_image[index][count].rgbtRed;
                green += temporary_image[index][count].rgbtGreen;
                blue += temporary_image[index][count].rgbtBlue;
                calculations++; 
            }
         
            // This pixel is for the bottom left
            if (index >= 0 && count - 1 >= 0)
            {
                red += temporary_image[index][count - 1].rgbtRed;
                green += temporary_image[index][count - 1].rgbtGreen;
                blue += temporary_image[index][count - 1].rgbtBlue;
                calculations++; 
            }
        
            // This pixel is for the top left
            if (index - 1 >= 0 && count >= 0)
            {
                red += temporary_image[index - 1][count].rgbtRed;
                green += temporary_image[index - 1][count].rgbtGreen;
                blue += temporary_image[index - 1][count].rgbtBlue;
                calculations++; 
            }
         
            // This pixel is for the top right
            if (index - 1 >= 0 && count - 1 >= 0)
            {
                red += temporary_image[index - 1][count - 1].rgbtRed;
                green += temporary_image[index - 1][count - 1].rgbtGreen;
                blue += temporary_image[index - 1][count - 1].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the bottom edge
            if ((index >= 0 && count + 1 >= 0) && (index >= 0 && count + 1 < width))
            {
                red += temporary_image[index][count + 1].rgbtRed;
                green += temporary_image[index][count + 1].rgbtGreen;
                blue += temporary_image[index][count + 1].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the top edge
            if ((index - 1 >= 0 &&  count + 1 >= 0) && (index - 1 >= 0 && count + 1 < width))
            {
                red += temporary_image[index - 1][count + 1].rgbtRed;
                green += temporary_image[index - 1][count + 1].rgbtGreen;
                blue += temporary_image[index - 1][count + 1].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the left edge
            if ((index + 1 >= 0 && count >= 0) && (index + 1 < height && count >= 0))
            {
                red += temporary_image[index + 1][count].rgbtRed;
                green += temporary_image[index + 1][count].rgbtGreen;
                blue += temporary_image[index + 1][count].rgbtBlue;
                calculations++;
            }
         
            // The pixels for the right edge
            if ((index + 1 >= 0 && count - 1 >= 0) && (index + 1 < height && count - 1 >= 0))
            {
                red += temporary_image[index + 1][count - 1].rgbtRed;
                green += temporary_image[index + 1][count - 1].rgbtGreen;
                blue += temporary_image[index + 1][count - 1].rgbtBlue;
                calculations++;
            }
         
            // The middle pixels
            if ((index + 1 >= 0 && count + 1 >= 0) && (index + 1 < height && count + 1 < width))
            {
                red += temporary_image[index + 1][count + 1].rgbtRed;
                green += temporary_image[index + 1][count + 1].rgbtGreen;
                blue += temporary_image[index + 1][count + 1].rgbtBlue;
                calculations++;
            }
         
            // The average amount for colors
            image[index][count].rgbtRed = round(red / calculations);
            image[index][count].rgbtGreen = round(green / calculations);
            image[index][count].rgbtBlue = round(blue / calculations);
        }
        return;
    }
}