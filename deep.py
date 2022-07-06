# Prompt the user to answer the following question
response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# If the response is 42, Forty Two, or Forty-Two then print yes
if response == "42":
    print("Yes")
elif response.islower() == "forty two":
    print("Yes")
elif response.islower() == "forty-two":
    print("Yes")
# Otherwise the default case will print no
else:
    print("No")