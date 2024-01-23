import tkinter as tk


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature():
    choice = choice_var.get()
    temperature = float(entry.get())

    if choice == 1:
        result_label.config(text=f"{fahrenheit_to_celsius(temperature):.2f} °C")
    elif choice == 2:
        result_label.config(text=f"{celsius_to_fahrenheit(temperature):.2f} °F")


# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create a variable to store the choice (Fahrenheit = 1, Celsius = 2)
choice_var = tk.IntVar()
choice_var.set(1)  # Default choice is Fahrenheit

# Creates buttons for selecting Celsius or Fahrenheit
celsius_radio = tk.Radiobutton(window, text="Celsius", variable=choice_var, value=2)
fahrenheit_radio = tk.Radiobutton(window, text="Fahrenheit", variable=choice_var, value=1)

# Creates a field for temperature input
entry_label = tk.Label(window, text="Enter Temperature:")
entry = tk.Entry(window)

# Creates a button that initiates the conversion
convert_button = tk.Button(window, text="Convert", command=convert_temperature)

# Creates a label to display the result
result_label = tk.Label(window, text="", font=("Helvetica", 14))

# Put the widgets in the window
celsius_radio.pack()
fahrenheit_radio.pack()
entry_label.pack()
entry.pack()
convert_button.pack()
result_label.pack()

# Start the GUI main loop
window.mainloop()
