def get_chatbot_response(message):
    if message[:2] != "!!":
        return ''

    bangs, command, args = message.split(' ', 2)
    if command == "Hey":
        return "What's up!"
    elif command == "add":
        numbers = [int(i) for i in args.split() if i.isdigit()]
        return sum(numbers)
    elif command == "divide":
        numbers = [int(i) for i in args.split() if i.isdigit()]
        num1 = numbers[0]
        num2 = numbers[1]
        return num1 / num2
    elif command == "say":
        return args
    else:
        return "Oops! I didn't recognize your command :("

