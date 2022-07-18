#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>
#define BLOCK_SIZE 512
#define FILE_INFO 8

// The following variables
typedef uint8_t BYTE;

// The following functions
bool newImages(BYTE buffer[]);

// Main test driver
int main(int argc, char *argv[])
{
    // If the argument character is not 2, execute the following statement
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1; 
    }
    
    // Open the file
    FILE *file = fopen(argv[1], "r");
    
    // If the file pointer is NULL
    if (file == NULL)
    {
        printf("The file is non-existent!\n");
        return 1;
    }
    
    // The byte buffer
    BYTE buffer[BLOCK_SIZE];
    FILE *imgptr = NULL;
    int index = 0;
    
    bool image = false;
    while (fread(buffer, BLOCK_SIZE, 1, file))
    {
        if (newImages(buffer))
        {
            if (!image)
            {
                image = true;
            }
            else 
            {
                fclose(imgptr);
            }
            
            char fileData[FILE_INFO];
            sprintf(fileData, "%03i.jpg", index++);
            imgptr = fopen(fileData, "w");
            if (imgptr == NULL)
            {
                return 1; 
            }
            fwrite(buffer, BLOCK_SIZE, 1, imgptr);
        }
        
        else if (image)
        {
            // Write the file if it hasn't been written already
            fwrite(buffer, BLOCK_SIZE, 1, imgptr);
        }
    }
    fclose(imgptr);
    fclose(file);
    return 0; 
}

bool newImages(BYTE buffer[])
{
    return (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0);
}