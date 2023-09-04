def main():
    message = input()
    message = convert(message)
    print(message)

def convert(message):
    # if :) is in the string
    if message.find(":)") >= 0:
        message = message.replace(":)", "🙂")

    # if :) is in the string
    if message.find(":(") >= 0:
        message = message.replace(":(", "🙁")

    # return message
    return message

main()