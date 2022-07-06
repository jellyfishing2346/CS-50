# Prompt the user to enter a file name
file = input("File name: ")

# If the file name ends with .pdf, image/gif
if ".gif" in file:
    print("image/gif")

# If the file name ends with .jpg, image/jpg
elif ".jpg" in file:
    print("image/jpg")

# If the file name ends with .jpeg, image/jpeg
elif ".jpeg" in file:
    print("image/jpeg")

# If the file name ends with .png, image/png
elif ".png" in file:
    print("image/png")

# If the file name ends with .pdf, image/pdf
elif ".pdf" in file:
    print("image/pdf")

# If the file name ends with .txt, image/txt
elif ".txt" in file:
    print("image/txt")

# If the file name ends with .zip, image/zip
elif ".zip" in file:
    print("image/zip")

# Otherwise print the default case
print("application/octet-stream")