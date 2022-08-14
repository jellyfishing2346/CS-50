def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    lengthInfo = len(s)
    if lengthInfo >= 2 and lengthInfo <= 6:
        for letterInfo in s:
            if not s.isalnum(letterInfo):
                break

            if s[0:2].isalpha():
                middleIndex = s[1::-1]
                if middleIndex.isnumeric() and middleIndex.find(0):
                    break
                zero = s.find("0") - 1
                if s[-(zero)].isdigit():
                    for index in s:
                        if index.digit():
                            if index.startswith('0'):
                                return False
                            else
                                return True
                if s[-2].isdigit() and s[-1].isalpha():
                    break
                elif s[-2].isdigit():
                    return True
                elif s.isalpha():
                    return True
            else:
                return False

main()
