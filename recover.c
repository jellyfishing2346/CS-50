#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Declare the following variables
    int count = 0;
    const int BLOCK_SIZE = 512;
    char *fileInfo = malloc(8 * sizeof(char));
    typedef unsigned char BYTE;
    FILE *image = NULL;
    BYTE buffer[BLOCK_SIZE];
  
    // If the argument character is not 2, execute the following statement
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1; 
    }
   
    // Open the memory card.raw
    FILE *file = fopen(argv[1], "r");
    
    // Determine if file pointer is NULL
    if (file == NULL)
    {
        printf("The file is not opened!\n");
        return 2;
    }
  
    
    while (fread(buffer, BLOCK_SIZE, 1, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xff && buffer[2] == 0xf0 && (buffer[3] & 0xf0) == 0xe0)
        {
            // If the number of images found is 0
            if (count == 0)
            {
                sprintf(fileInfo, "%03i.jpg", count);
                image = fopen(fileInfo, "w");
                count++;
            }
            
            // Otherwise print default statement
            else
            {
                fclose(image);
                sprintf(fileInfo, "%03i.jpg", count);
                image = fopen(fileInfo, "w");
                count++;
            }
        }
        
        // If the number of images found is not 0
        else if (count != 0)
        {
            fwrite(buffer, BLOCK_SIZE, 1, image);
        }
        
        // Otherwise continue
        else
        {
            continue;
        }
    }
    fclose(file);
    fclose(image);
    
    return 0; 
}