import tkinter as tk


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return ((fahrenheit - 32) * 5 / 9) + 273.15


def kelvin_to_celsius(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def kelvin_to_fahrenheit(kelvin):
    return kelvin + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature():
    choice = choice_var.get()
    temperatures = entry.get().split(',')  # allows user to enter an array seperated by commas

    conversion_map = {  # map so that we can reduce repetition
        1: (fahrenheit_to_celsius, "{0.2f} °F is {1:.2f} °C"),
        2: (celsius_to_fahrenheit, "{0.2f} °C is {1:.2f} °F"),
        3: (fahrenheit_to_kelvin, "{0.2f} °F is {1:.2f} °K"),
        4: (celsius_to_kelvin, "{0.2f} °C is {1:.2f} °K"),
        5: (kelvin_to_celsius, "{0.2f} °K is {1:.2f} °C"),
        6: (kelvin_to_fahrenheit, "{0.2f} °K is {1:.2f} °F")
    }

    results = []
    for temp_str in temperatures:
        try:
            temperature = float(temp_str.strip())
            conversion_function, format_string = conversion_map[choice]
            converted = conversion_function(temperature)
            results.append(format_string.format(temperature, converted))
        except ValueError:
            results.append("Invalid, try again")

    result_label.config(text="\n".join(results))


window = tk.Tk()
window.title("Temperature Converter")

choice_var = tk.IntVar()
choice_var.set(1)

# Creates buttons for selecting Celsius or Fahrenheit or Kelvin
C_to_F_radio = tk.Radiobutton(window, text="°C to °F", variable=choice_var, value=2)
F_to_C_radio = tk.Radiobutton(window, text="°F to °C", variable=choice_var, value=1)
F_to_K_radio = tk.Radiobutton(window, text="°F to °K", variable=choice_var, value=3)
C_to_K_radio = tk.Radiobutton(window, text="°C to °K", variable=choice_var, value=4)
K_to_C_radio = tk.Radiobutton(window, text="°K to °C", variable=choice_var, value=5)
K_to_F_radio = tk.Radiobutton(window, text="°K to °F", variable=choice_var, value=6)

# Creates a field for temperature input
entry_label = tk.Label(window, text="Enter Temperature:")
entry = tk.Entry(window)

# Creates a button that initiates the conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature)

# Creates a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 14))

# Put the widgets in the window
C_to_F_radio.pack()
F_to_C_radio.pack()
F_to_K_radio.pack()
C_to_K_radio.pack()
K_to_C_radio.pack()
K_to_F_radio.pack()
entry_label.pack()
entry.pack()
convert_button.pack()
result_label.pack()

window.mainloop()
