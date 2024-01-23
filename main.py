def celsius_to_fahrenheit(celsius):  # this function converts Celsius values to Fahrenheit.
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):  # this function converts Fahrenheit values to Celsius.
    return (fahrenheit - 32) * 5 / 9


def main():  # The main function serves to prompt the user for an input.
    while True:  # this statement will loop the function.
        choice = input('Fahrenheit (1) or Celsius (2)?')  # user's input is recorded as "choice".
        if choice == '1':  # the value of choice is used to determine what method to pursue.
            fahrenheit = float(input('enter a temperature in Fahrenheit'))  # A value is assigned to "fahrenheit".
            celsius = fahrenheit_to_celsius(fahrenheit)  # variable is assigned a value from the converting function.
            print(celsius)  # value assigned to variable is printed to console.
        elif choice == '2':  # the value of choice is used to determine what method to pursue.
            celsius = float(input('enter a temperature in Celsius'))  # A value is assigned to "celsius".
            fahrenheit = celsius_to_fahrenheit(celsius)  # variable is assigned a value from the converting function.
            print(fahrenheit)  # value assigned to variable is printed to console.
        else:  # if user input is not 1 or 2 the program prints an invalid message and prompts again.
            print('Invalid, try again.')  # Invalid message is printed to console.
            continue
        while True:
            exit_prompt = input('Would you like to generate another result (y/n)')  # an exit method when user is done.
            if exit_prompt.lower() == 'y':
                break  # program breaks from loop, continuing the program.
            elif exit_prompt.lower() == 'n':  # if the user inputs 'n' the program will stop.
                return  # program stops by exiting main function.
            else:
                print('Invalid, try again.')


if __name__ == '__main__':
    main()
