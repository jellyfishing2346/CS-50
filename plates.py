def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    index = 0
    while index < len(s):
        if s[index].isalpha() == False
            if s[index] == '0':
                return False
            else:
                break
    index += 1
    for character in s:
        if character in ['.', ' ', '!', '?']:
            return False

main()
