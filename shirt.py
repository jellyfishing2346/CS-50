import sys
from os.path import splitext
from PIL import Image, ImageOps

# Main function
def main():
    check_command_line()
    # Open the image
    try:
        muppetInfo = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # Open the shirt
    shirtInfo = Image.open("shirt.png")
    # Retrieve the size of the shirt
    sizeAmount = shirt.size
    # Resize the muppet's image to fit the shirt
    muppetInfo = ImageOps.fit(muppetInfo, sizeAmount)
    # Paste the shirt on the muppet
    muppetInfo.paste(shirtInfo, shirtInfo)
    # Create the response image
    muppetInfo.save(sys.argv[2])

# Check the command line argument
def check_command_line():
    # Determine the number of elements that exist in the command line
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    fileOne = splitext(sys.argv[1])
    fileTwo = splitext(sys.argv[2])
    # Check if there is an Image file
    if check_extensions_info(fileOne[1].lower()) == False or check_extensions_info(fileTwo[1].lower()) == False:
        sys.exit("Not a Image File")
    # Check if the file extension for both files are the same
    if fileOne[1].lower() != fileTwo[1].lower():
        sys.exit("Input and output have different extensions")

# Check the file extension
def check_extensions_info(fileInfo):
    if fileInfo in [".jpg", "jpeg", ".png"]:
        return True
    return False

if __name__ == "__main__":
main()