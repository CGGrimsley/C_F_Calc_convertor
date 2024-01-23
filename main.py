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
    temperature = float(entry.get())

    if choice == 1:
        result_label.config(text=f"{fahrenheit_to_celsius(temperature):.2f} °C")
    elif choice == 2:
        result_label.config(text=f"{celsius_to_fahrenheit(temperature):.2f} °F")
    elif choice == 3:
        result_label.config(text=f"{fahrenheit_to_kelvin(temperature):.2f} °K")
    elif choice == 4:
        result_label.config(text=f"{celsius_to_kelvin(temperature):.2f} °K")
    elif choice == 5:
        result_label.config(text=f"{kelvin_to_celsius(temperature):.2f} °C")
    elif choice == 6:
        result_label.config(text=f"{kelvin_to_fahrenheit(temperature):.2f} °F")


# Create the main window
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

# Start the GUI main loop
window.mainloop()
