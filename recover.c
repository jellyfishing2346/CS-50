#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Declare the following variables
    typedef uint8_t BYTE;
    
    // If the character argument is not 2, execute this statement
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover IMAGE\n");
        return 1;
    }
    
    // Open the file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "This file is not opening %s.\n", argv[1]);
        return 2; 
    }
    
    // Set image pointer to NULL
    FILE *imgptr = NULL;
    
    // Memory card
    BYTE buffer[512];
    
    // Count the number of images that have been retrieved
    int count = 0;
    
    // Hold the filename via string
    char fileInfo[8] = malloc(8 * sizeof(char));
    
    // This function reads the memory card
    while(fread(buffer, sizeof(BYTE) * 512, 1, file) == 1)
    {
        // Determine if jpeg exists
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF && (buffer[3] & 0xF0) == 0xE0)
        {
            // If the image pointer is not null
            if (imgptr != NULL)
            {
                fclose(imgptr);
            }
            sprintf(fileInfo, "%03d.jpg", count++);
            
            // Open via the new image pointer
            imgptr = fopen(fileInfo, "w");
        }
        
        // Write the file if the file doesn't already exist
        if (imgptr != NULL)
        {
            fwrite(buffer, sizeof(BYTE) * 512, 1, imgptr);
        }
        
        // Close the image pointer
        if (imgptr != NULL)
        {
            fclose(imgptr);
        }
        
        // Close the file
        fclose(file);
    }
    
    return 0; 
}