import string
import random
import tkinter as tk


def generate_password():
    global length1  # Add this line to access the global length1 variable
    length1 = int(length_entry.get())
    str = string.ascii_lowercase
    str1 = string.ascii_uppercase
    str2 = string.digits
    str3 = string.punctuation
    s = []
    s += list(str) + list(str1) + list(str2) + list(str3)
    random.shuffle(s)
    # print(s)
    # print("The password generated is: ")
    password = "".join(s[0:length1])  # .join function will concatenate all he elements of s
    result_label.config(text=f"The generated password is: {password}")

root = tk.Tk()
root.title("Password Generator")
root.geometry("600x600")
root.configure(bg="purple")

# Labels and Entry for password length
length_label = tk.Label(root, text="Enter length of password:", bg="yellow",font=("Arial",20))
length_label.pack(pady=5)
length_entry = tk.Entry(root,font=("Arial",20))
length_entry.pack(pady = 5)
length1 = 0


generate_button = tk.Button(root, text="Generate Password",bg="yellow" ,command=lambda: generate_password(),font=("Arial",20))
generate_button.pack(pady=5)

result_label = tk.Label(root, text="",font=("Arial",20))
result_label.pack(pady=5)

root.mainloop()