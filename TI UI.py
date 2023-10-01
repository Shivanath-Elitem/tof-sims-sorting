from tkinter import *

def section_button_click(section_num, button_num):
    # Define actions when a button in a specific section is clicked
    pass

root = Tk()
root.title("Multi-Section GUI")

'''
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))
   
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
'''
sections = []

'''''
python
# Change the background color of the section when a button in that section is clicked
if section_num == 1:
    change_background_color("red")
elif section_num == 2:
    change_background_color("blue")
else:
    change_background_color("green")
'''''
# Create and label each section

# section 1
section_1 = Frame(root, relief= RAISED, borderwidth=20)
section_1_label = Label(section_1, text= "SINGLE-PEAK SUBSTR, CMPD OR FRAG SEARCH")
section_1_label.pack()
section_1.pack(side= LEFT, padx=10, pady=10)

# Section 2
section_2 = Frame(root, relief= RAISED, borderwidth=20)
section_2_label = Label(section_2, text= "SELECT TABLE RESULTS")
section_2_label.pack()
section_2.pack(side= LEFT, padx=10, pady=10)

# Section 3
section_3 = Frame(root, relief= RAISED, borderwidth=20)
section_3_label = Label(section_3, text= "SPECTRUM SUBSTR, CMPD OR FRAG SRCH")
section_3_label.pack()
section_3.pack(side= LEFT, padx=10, pady=10)

# Section 4
section_4 = Frame(root, relief= RAISED, borderwidth=20)
section_4_label = Label(section_4, text= "CMPD AND FRAG SRCH")
section_4_label.pack()
section_4.pack(side= LEFT, padx=10, pady=10)

# Section 5
section_5 = Frame(root, relief= RAISED, borderwidth=20)
section_5_label = Label(section_5, text="EXPORT SUBSTAR, CMPD AND FRAG SUM")
section_5_label.pack()
section_5.pack(side= LEFT, padx=10, pady=10)

# Section 6
section_6 = Frame(root, relief= RAISED, borderwidth=20)
section_6_label = Label(section_6, text="OPEN SS, CMPD, FRAG SUM")
section_6_label.pack()
section_6.pack(side=LEFT, padx=10, pady=10)

# Section 7
section_7 = Frame(root, relief= RAISED, borderwidth=20)
section_7_label = Label(section_7, text="CMPD SRCH")
section_7_label.pack()
section_7.pack(side= LEFT, padx=10, pady=10)

# Section 8
section_8 = Frame(root, relief= RAISED, borderwidth=20)
section_8_label = Label(section_8, text="MASS TOL")
section_8_label.pack()
section_8.pack(side= LEFT, padx=10, pady=10)

# Section 9
section_9 = Frame(root, relief= RAISED, borderwidth=20)
section_9_label = Label(section_9, text="OPEN EXCL SUBSTAR, CMPD OR FRAG SUM")
section_9_label.pack()
section_9.pack(side= LEFT, padx=10, pady=10)

# Section 10
section_10 = Frame(root, relief= RAISED, borderwidth=20)
section_10_label = Label(section_10, text="CMPD SRCH")
section_10_label.pack()
section_10.pack(side= LEFT, padx=10, pady=10)


# Add buttons and text display for section 1 (customize as needed)
button_1_1 = Button(section_1, text="Button 1", command=lambda: section_button_click(1, 1))
button_1_2 = Button(section_1, text="Button 2", command=lambda: section_button_click(1, 2))
button_1_3 = Button(section_1, text="Button 3", command=lambda: section_button_click(1, 3))
text_display_1 = Text(section_1, height=1, width=10)

button_1_1.pack()
button_1_2.pack()
button_1_3.pack()
text_display_1.pack()

# Add buttons for section 2 (customize as needed)
button_2_1 = Button(section_2, text="Button 1", command=lambda: section_button_click(2, 1))
button_2_2 = Button(section_2, text="Button 2", command=lambda: section_button_click(2, 2))
button_2_3 = Button(section_2, text="Button 3", command=lambda: section_button_click(2, 3))

button_2_1.pack()
button_2_2.pack()
button_2_3.pack()

# Add buttons for section 3 (customize as needed)

button_3_1 = Button(section_3, text="Button 1", command=lambda: section_button_click(3, 1))
button_3_2 = Button(section_3, text="Button 2", command=lambda: section_button_click(3, 2))
button_3_3 = Button(section_3, text="Button 3", command=lambda: section_button_click(3, 3))

button_3_1.pack()
button_3_2.pack()
button_3_3.pack()

# Add buttons for section 4 (customize as needed)

button_4_1 = Button(section_4, text="Button 1", command=lambda: section_button_click(4, 1))
button_4_2 = Button(section_4, text="Button 2", command=lambda: section_button_click(4, 2))
button_4_3 = Button(section_4, text="Button 3", command=lambda: section_button_click(4, 3))

button_4_1.pack()
button_4_2.pack()
button_4_3.pack()

# Add buttons for section 5 (customize as needed)

button_5_1 = Button(section_5, text="Button 1", command=lambda: section_button_click(5, 1))

"""
button_5_2 = tk.Button(section_5, text="Button 2", command=lambda: section_button_click(5, 2))
button_5_3 = tk.Button(section_5, text="Button 3", command=lambda: section_button_click(5, 3))
"""

button_5_1.pack()

"""
button_5_2.pack()
button_5_3.pack()
"""

# Add buttons for section 6 (customize as needed)

button_6_1 = Button(section_6, text="Button 1", command=lambda: section_button_click(6, 1))

"""
button_6_2 = tk.Button(section_6, text="Button 2", command=lambda: section_button_click(6, 2))
button_6_3 = tk.Button(section_6, text="Button 3", command=lambda: section_button_click(6, 3))
"""

button_6_1.pack()

"""
button_6_2.pack()
button_6_3.pack()
"""

# Add buttons for section 7 (customize as needed)

button_7_1 = Button(section_7, text="Button 1", command=lambda: section_button_click(7, 1))
button_7_2 = Button(section_7, text="Button 2", command=lambda: section_button_click(7, 2))
button_7_3 = Button(section_7, text="Button 3", command=lambda: section_button_click(7, 3))

button_7_1.pack()
button_7_2.pack()
button_7_3.pack()

# Add buttons for section 8 (customize as needed)

button_8_1 = Button(section_8, text="Button 1", command=lambda: section_button_click(8, 1))
button_8_2 = Button(section_8, text="Button 2", command=lambda: section_button_click(8, 2))
button_8_3 = Button(section_8, text="Button 3", command=lambda: section_button_click(8, 3))
button_8_4 = Button(section_8, text="Button 4", command=lambda: section_button_click(8, 4))
button_8_5 = Button(section_8, text="Button 5", command=lambda: section_button_click(8, 5))
button_8_6 = Button(section_8, text="Button 6", command=lambda: section_button_click(8, 6))
button_8_7 = Button(section_8, text="Button 7", command=lambda: section_button_click(8, 7))
button_8_8 = Button(section_8, text="Button 8", command=lambda: section_button_click(8, 8))
button_8_9 = Button(section_8, text="Button 9", command=lambda: section_button_click(8, 9))
button_8_10 =Button(section_8, text="Button 10", command=lambda: section_button_click(8, 10))

button_8_1.pack()
button_8_2.pack()
button_8_3.pack()
button_8_4.pack()
button_8_5.pack()
button_8_6.pack()
button_8_7.pack()
button_8_8.pack()
button_8_9.pack()
button_8_10.pack()

# Add buttons for section 9 (customize as needed)

button_9_1 = Button(section_9, text="Button 1", command=lambda: section_button_click(9, 1))
button_9_2 = Button(section_9, text="Button 2", command=lambda: section_button_click(9, 2))
button_9_3 = Button(section_9, text="Button 3", command=lambda: section_button_click(9, 3))

button_9_1.pack()
button_9_2.pack()
button_9_3.pack()

# Add buttons for section 10 (customize as needed)

button_10_1 = Button(section_10, text="Button 1", command=lambda: section_button_click(10, 1))
button_10_2 = Button(section_10, text="Button 2", command=lambda: section_button_click(10, 2))

"""
button_10_3 = tk.Button(section_10, text="Button 3", command=lambda: section_button_click(10, 3))
"""

button_10_1.pack()
button_10_2.pack()

"""
button_10_3.pack()
"""

root.mainloop()
