# Prompt the user to enter a file name
file = input("File name: ")
modify = file.lower()

# If the file name ends with .pdf, image/gif
if ".gif" in modify:
    print("image/gif", end = "")

# If the file name ends with .jpg, image/jpg
elif ".jpg" in modify:
    print("image/jpg", end = "")

# If the file name ends with .jpeg, image/jpeg
elif ".jpeg" in modify:
    print("image/jpeg", end = "")

# If the file name ends with .png, image/png
elif ".png" in modify:
    print("image/png", end = "")

# If the file name ends with .pdf, image/pdf
elif ".pdf" in modify:
    print("application/pdf", end = "")

# If the file name ends with .txt, image/txt
elif ".txt" in modify:
    print("text/plain", end = "")

# If the file name ends with .zip, image/zip
elif ".zip" in modify:
    print("application/zip", end = "")

# Otherwise print the default case
else:
	print("application/octet-stream", end = "")	