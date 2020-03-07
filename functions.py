def get_chatbot_response(message):
    if message[:2] != "!!":
        return ''

    bangs, command, args = message.split(' ', 2)
    if command == "Hey":
        return "What's up!"
    elif command == "add":
        num1, num2 = args.split()
        one = int(num1)
        two = int(num2)
        return one+two
    elif command == "divide":
        num1, num2 = args.split()
        one = int(num1)
        two = int(num2)
        return one / two
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("

test = get_chatbot_response("!! Hey Maya")
test2 = get_chatbot_response("!! add 5 6")
test3 = get_chatbot_response("!! divide 20 2")
# print(test)
# print(test2)
# print(test3)