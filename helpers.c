#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Evaluate the height through each row
    for (int index = 0; index < height; index++)
    {
        // Evaluate the width through each column
        for (int count = 0; count < width; count++)
        {
            // Conversion to pixels to floats
            float Red = image[index][count].rgbtRed;
            float Green = image[index][count].rgbtGreen;
            float Blue = image[index][count].rgbtBlue;
            
            // Determine the average
            int avg_value = round((Red + Green + Blue) / 3);
            avg_value = image[index][count].rgbtRed
            = image[index][count].rgbtBlue = image[index][count].rgbtGreen;
            
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Evaluate the height through each row
    for (int index = 0; index < height; index++)
    {
        // Evaluate the width through each column
        for (int count = 0; count < width; count++)
        {
            // Conversion to pixels to floats
            float originalRed = image[index][count].rgbtRed;
            float originalBlue = image[index][count].rgbtBlue;
            float originalGreen = image[index][count].rgbtGreen;
            
            // Retrieve the update pixel value
            int sepiaRed = round((0.39) * originalRed + 0.769 * originalGreen
            + 0.189 * originalBlue);
            int sepiaBlue = round((0.39) * originalRed + 0.769 * originalGreen
            + 0.189 * originalBlue);
            int sepiaGreen = round((0.39) * originalRed + 0.769 * originalGreen
            + 0.189 * originalBlue);
            
            // Change the pixel value if sepiaRed, sepiaBlue, sepiaGreen is greater than 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255; 
            }
            
            // Update the final pixel values
            image[index][count].rgbtRed = sepiaRed;
            image[index][count].rgbtBlue = sepiaBlue;
            image[index][count].rgbtGreen = sepiaGreen;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
