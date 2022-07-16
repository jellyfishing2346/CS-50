#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

 
int main(int argc, char *argv[])
{
   // Declare the following variables
   typedef uint8_t BYTE;
   BYTE buffer[512];
   FILE *imgptr = NULL;
   char file[8];
   int BLOCK_SIZE = 1;
   int count = 0;
  
   // If the argument character is not 2, execute the following statement
   if (argc != 2)
   {
        printf("Usage: ./recover IMAGE\n");
        return 1; 
   }
   
   else 
   {
        // Open the file named card.raw
        char *input = argv[1];
        FILE *inptr = fopen(argv[1], "r");
        
        // Execute if the input pointer is NULL
        if (inptr == NULL)
        {
             printf("Error: File not open %s\n", input);
             return 2; 
        }
        
       /* // Running the file unitl it reaches the end
       while (fread(buffer, 1, BLOCK_SIZE, inptr) == BLOCK_SIZE)
       {
           if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] == 0xf0 < 0xe0)
           {
                if (count != 0)
                {
                     fclose(imgptr);
                }
                
                // The file process
                sprintf(file, "%03i.jpg", count);
                imgptr = fopen(file, "w");
                count++; 
           }
           
           
           if (count != 0)
           {
                fwrite(&buffer, 512, BLOCK_SIZE, imgptr);
           }
       }
       fclose(inptr);
       fclose(imgptr);
   }
   */
   return 0; 
}
}