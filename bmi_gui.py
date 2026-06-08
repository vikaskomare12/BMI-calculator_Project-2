import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "bmi_data.csv"


def calculate_bmi():
    try:
        name = name_entry.get()

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Error",
                "Weight and Height must be positive values."
            )
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        save_data(
            name,
            weight,
            height,
            bmi,
            category
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid values."
        )


def save_data(name, weight, height, bmi, category):

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%d-%m-%Y"),
            name,
            weight,
            height,
            round(bmi, 2),
            category
        ])


def view_history():

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")

    text = tk.Text(history_window,
                   width=70,
                   height=20)

    text.pack()

    try:
        with open(CSV_FILE, "r") as file:
            text.insert(tk.END, file.read())

    except FileNotFoundError:
        text.insert(
            tk.END,
            "No history found."
        )


def show_graph():

    dates = []
    bmi_values = []

    try:
        with open(CSV_FILE, "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:
                dates.append(row[0])
                bmi_values.append(float(row[4]))

        plt.figure(figsize=(8, 4))
        plt.plot(
            dates,
            bmi_values,
            marker="o"
        )

        plt.title("BMI Trend")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.grid(True)

        plt.show()

    except:
        messagebox.showinfo(
            "Info",
            "No data available."
        )


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x350")

tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg)").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m)").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi
).pack(pady=10)

tk.Button(
    root,
    text="View History",
    command=view_history
).pack(pady=5)

tk.Button(
    root,
    text="Show BMI Graph",
    command=show_graph
).pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)

result_label.pack(pady=10)

root.mainloop()