# Prompt the user to enter a file name
file = input("File name: ")
modify = file.lower()

# If the file name ends with .pdf, image/gif
if ".gif" in modify:
    print("image/gif")

# If the file name ends with .jpg, image/jpg
elif ".jpg" in modify:
    print("image/jpg")

# If the file name ends with .jpeg, image/jpeg
elif ".jpeg" in modify:
    print("image/jpeg")

# If the file name ends with .png, image/png
elif ".png" in modify:
    print("image/png")

# If the file name ends with .pdf, image/pdf
elif ".pdf" in modify:
    print("application/pdf")

# If the file name ends with .txt, image/txt
elif ".txt" in modify:
    print("text/plain")

# If the file name ends with .zip, image/zip
elif ".zip" in modify:
    print("application/zip")

# Otherwise print the default case
print("application/octet-stream")