def main():
# Prompt the user to enter a time
    time = input("What time is it? ")
    convert(time)
def convert(time):
     answer = time
     hours, minutes = time.split(":")
# If time is between 7 and 8, print breakfast time
     if "7.0" <= time <= "8.0":
        print("breakfast time")
        return float(hours) + float(minutes) / 60
# If time is between 12 and 13 , print lunch time
     elif "12.0" <= time <= "13.0":
        print("lunch time")
        return float(hours) + float(minutes) / 60
# If time is between 18 and 19, print dinner time
     elif "18.0" <= time <= "19.0":
        print("dinner time")
        return float(hours) + float(minutes) / 60
# Otherwise print the default case
     else:
      print(" ")
	  return 0;

if __name__ == "__main__":
    main()