#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Declare the following variables
    int count = 0;
    const int BLOCK_SIZE = 512;
    char *fileInfo = NULL;
    typedef unsigned char BYTE;
    FILE *image = NULL;
    BYTE buffer[BLOCK_SIZE];
  
    // If the argument character is not 2, execute the following statement
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1; 
    }
   
    FILE *file = fopen(argv[1], "r");
    
    // Determine if file pointer is NULL
    if (file == NULL)
    {
        printf("The file is not opened!\n");
        return 2;
    }
    
    while(fread(buffer,BLOCK_SIZE,1,file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xff && buffer[2] == 0xf0 && (buffer[3] & 0xf0) == 0xe0)
        {
            if (count == 0)
            {
                sprintf(fileInfo, "%03i.jpg", count);
                image = fopen(fileInfo, "w");
                count++;
            }
            else
            {
                fclose(image);
                sprintf(fileInfo, "%03i.jpg", count);
                image = fopen(fileInfo, "w");
                count++;
            }
        }
        else if (count != 0)
        {
            fwrite(buffer,BLOCK_SIZE,1,image);
        }
        
        else
        {
            continue;
        }
    }
    fclose(file);
    fclose(image);
    return 0; 
}