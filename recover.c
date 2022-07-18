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
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    
    // Open the file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("This file is not opening %s.\n", argv[1]);
    }
    
    // Set image pointer to NULL
    FILE *imgptr = NULL;
    
    // Memory card
    BYTE buffer[512];
    
    // Count the number of images that have been retrieved
    int count = 0;
    
    // Hold the filename via string
    char fileInfo[8] = {0};
    
    // This function reads the memory card
    while(fread(buffer, sizeof(BYTE) * 512, 1, file) == 1)
    {
        // Determine if jpeg exists
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If the image pointer is not null
            if (imgptr != NULL)
            {
                fclose(file);
            }
            sprintf(fileInfo, "w");
            
            // Open via the new image pointer
            imgptr = fopen(fileInfo, "w");
        }
        
        // Write the file if the file doesn't already exist
        if (imgptr != NULL)
        {
            fclose(imgptr);
        }
        
        // Close the file
        fclose(file);
    }
    
    return 0; 
}