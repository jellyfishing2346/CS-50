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
          
            image[index][count].rgbtBlue = image[index][width-count-1].rgbtBlue;
          	image[index][count].rgbtGreen = image[index][width-count-1].rgbtGreen;
          	image[index][count].rgbtRed = image[index][width-count-1].rgbtRed;
          
          	image[index][width-count-1].rgbtBlue = temp[0];
          	image[index][width-count-1].rgbtGreen = temp[1];
          	image[index][width-count-1].rgbtRed = temp[2];
          
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
  	int starti, startc, endi, endc; 
    
    // Evaluate each row by the height
    for (int j = 0; j < height; j++)
    {
        // Evaluate each column by the width
        for (int k = 0; k < width; k++)
        {
          	if (j - 1 < 0)
              {
                starti = 0; 
              } else {
                starti = j - 1;
              }
          	if (k - 1 < 0)
              {
			  	startc = 0;
              } else {
                startc = k; 
              }
          	if (j + 1 == height)
              {
                endi = height;
              } else {
                endi = j + 1; 
              }
             if (k + 1 == width)
               {
				 endc = width;
               } else {
                 endc = k + 1; 
               }
                // Count the rows
            	for (int i = starti; i < endi; i++)
            	{	
                	// Count the columns
                	for (int c = startc; c < endc; c++)
                	{
                    totalRed += original_image[i][c].rgbtRed;
                    totalGreen += original_image[i][c].rgbtGreen;
                    totalBlue += original_image[i][c].rgbtBlue;             
          			    
                	}
            	}
          			image[j][k].rgbtRed = round(totalRed / 3.0);
         			image[j][k].rgbtGreen = round(totalGreen / 3.0);
          			image[j][k].rgbtBlue = round(totalBlue / 3.0);
          			printf("%d ", image[j][k].rgbtRed);
          			printf("%d ", image[j][k].rgbtGreen);
          			printf("%d", image[j][k].rgbtBlue);
                    printf("\n");

            int total = 0;
        	}
    }
    return;
}