import tkinter as tk
from tkinter import ttk, messagebox

def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:]

def octal_to_decimal(octal_number):
    return int(octal_number, 8)

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

def hexadecimal_to_decimal(hexadecimal_number):
    return int(hexadecimal_number, 16)

def binary_to_octal(binary_number):
    decimal_number = binary_to_decimal(binary_number)
    return decimal_to_octal(decimal_number)

def octal_to_binary(octal_number):
    decimal_number = octal_to_decimal(octal_number)
    return decimal_to_binary(decimal_number)

def binary_to_hexadecimal(binary_number):
    decimal_number = binary_to_decimal(binary_number)
    return decimal_to_hexadecimal(decimal_number)

def hexadecimal_to_binary(hexadecimal_number):
    decimal_number = hexadecimal_to_decimal(hexadecimal_number)
    return decimal_to_binary(decimal_number)

def convert():
    input_number = entry.get()
    conversion_type = combo.get()

    try:
        if conversion_type == "Decimal to Binary":
            result.set(decimal_to_binary(int(input_number)))
        elif conversion_type == "Binary to Decimal":
            result.set(binary_to_decimal(input_number))
        elif conversion_type == "Decimal to Octal":
            result.set(decimal_to_octal(int(input_number)))
        elif conversion_type == "Octal to Decimal":
            result.set(octal_to_decimal(input_number))
        elif conversion_type == "Decimal to Hexadecimal":
            result.set(decimal_to_hexadecimal(int(input_number)))
        elif conversion_type == "Hexadecimal to Decimal":
            result.set(hexadecimal_to_decimal(input_number))
        elif conversion_type == "Binary to Octal":
            result.set(binary_to_octal(input_number))
        elif conversion_type == "Octal to Binary":
            result.set(octal_to_binary(input_number))
        elif conversion_type == "Binary to Hexadecimal":
            result.set(binary_to_hexadecimal(input_number))
        elif conversion_type == "Hexadecimal to Binary":
            result.set(hexadecimal_to_binary(input_number))
        else:
            messagebox.showerror("Error", "Please select a valid conversion type.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input for the selected conversion type.")

root = tk.Tk()
root.title("Конвертер Сис.Счислении")
root.geometry("700x500")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

frame.columnconfigure(0, weight=2)
frame.rowconfigure(0, weight=2)

label = ttk.Label(frame, text="Enter number:", padding="10")
label.grid(column=0, row=0, sticky=tk.W)

entry = ttk.Entry(frame, width=50)
entry.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=5)

combo = ttk.Combobox(frame, state="readonly", values=[
    "Decimal to Binary",
    "Binary to Decimal",
    "Decimal to Octal",
    "Octal to Decimal",
    "Decimal to Hexadecimal",
    "Hexadecimal to Decimal",
    "Binary to Octal",
    "Octal to Binary",
    "Binary to Hexadecimal",
    "Hexadecimal to Binary"
])
combo.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=5)
combo.set("Выберите типы конвертации")

convert_button = ttk.Button(frame, text="конвертировать", command=convert)
convert_button.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=10)

result_label = ttk.Label(frame, text="Результат:", padding="5")
result_label.grid(column=0, row=3, sticky=tk.W)

result = tk.StringVar()
result_display = ttk.Label(frame, textvariable=result, font=("Arial", 14, "bold"), padding="5")
result_display.grid(column=1, row=3, sticky=(tk.W, tk.E))

style = ttk.Style()
style.configure("TEntry", padding=10, relief="flat")
style.configure("TButton", padding=5, relief="flat")
style.configure("TLabel", padding=5)
style.map("TEntry",
          relief=[("active", "flat")],
          bordercolor=[("!disabled", "#bfbfbf")])

# Run the GUI
root.mainloop()

