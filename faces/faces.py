def main():
    message = input()
    result = convert(message)
    print(result)
def convert(message):
    happy = message.replace(":)", "🙂")
    sad = happy.replace(":(", "🙁")
    return sad
main()