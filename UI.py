import tkinter as tk

def on_button_click(section_number, button_number):
    print(f"Section {section_number}, Button {button_number} clicked!")

root = tk.Tk()
root.title("User Interface with Sections")

# Create 10 sections
for section_number in range(1, 11):
    section_frame = tk.Frame(root, borderwidth=2, relief="ridge")
    section_frame.grid(row=0, column=section_number - 1, padx=5, pady=5, sticky="nsew")

    title_label = tk.Label(section_frame, text=f"Section {section_number}")
    title_label.pack(pady=5)

    # Define the number of buttons for each section
    num_buttons = 10 if section_number == 8 else 3

    # Create buttons for each section
    for button_number in range(1, num_buttons + 1):
        button = tk.Button(section_frame, text=f"Button {button_number}",
                           command=lambda s=section_number, b=button_number: on_button_click(s, b))
        button.pack()

# Adjust row and column weights for resizing
for i in range(10):
    root.grid_columnconfigure(i, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
