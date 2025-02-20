from encrypt import encrypt_text
from cipher import cipher,decipher
from decrypt import decrypt_text
import tkinter as tk
from tkinter import messagebox

def calculate():
    text=entry_text.get()
    try:
        P=int(entry_p.get())
        Q=int(entry_q.get())
    except ValueError:
        messagebox.showerror(title="Error",message="Fill All Box")
        return    
    if len(str(P))==0 or len(str(Q))==0 or len(text)==0:
        messagebox.showwarning(title='Error',message='Please Fill All Required Boxs')
    else:
        try:
            values=encrypt_text(P,Q,cipher(text))
            N=values[0]
            PHI=values[1]
            E=values[2]
            D=values[3]
            ENCRYPTED=""
            for char in values[4]:
                ENCRYPTED+=str(char)
            DECRYPTED=decipher(decrypt_text(D,N,values[4]))
            display(N,PHI,E,D,ENCRYPTED,DECRYPTED)
        except ValueError as e:
            messagebox.showwarning(title='Error',message='Please Enter Odd Numbers')
            return

def display(N,PHI,E,D,ENCRYPTED,DECRYPTED):
    label_n_value.config(text=f"{N}")
    label_phi_value.config(text=f"{PHI}")
    label_e_value.config(text=f"{E}")
    label_d_value.config(text=f"{D}")
    label_encrypted_value.config(text=f"{ENCRYPTED}")
    label_decrypted_value.config(text=f"{DECRYPTED.title()}")

##########################################################################################

window = tk.Tk()
window.title("RSA Encryption/Decryption")

# P input
label_p = tk.Label(window, text="Enter P (Prime Number):")
label_p.grid(row=0, column=0, padx=10, pady=10)
entry_p = tk.Entry(window)
entry_p.grid(row=0, column=1, padx=10, pady=10)

# Q input
label_q = tk.Label(window, text="Enter Q (Prime Number):")
label_q.grid(row=1, column=0, padx=10, pady=10)
entry_q = tk.Entry(window)
entry_q.grid(row=1, column=1, padx=10, pady=10)

# Text input
label_text = tk.Label(window, text="Enter Text:")
label_text.grid(row=2, column=0, padx=10, pady=10)
entry_text = tk.Entry(window)
entry_text.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Display N
label_n = tk.Label(window, text="N (P * Q):")
label_n.grid(row=4, column=0, padx=10, pady=10)
label_n_value = tk.Label(window, text="")
label_n_value.grid(row=4, column=1, padx=10, pady=10)

# Display PHI
label_phi = tk.Label(window, text="PHI ((P-1) * (Q-1)):")
label_phi.grid(row=5, column=0, padx=10, pady=10)
label_phi_value = tk.Label(window, text="")
label_phi_value.grid(row=5, column=1, padx=10, pady=10)

# Display E
label_e = tk.Label(window, text="E (Public Key):")
label_e.grid(row=6, column=0, padx=10, pady=10)
label_e_value = tk.Label(window, text="")
label_e_value.grid(row=6, column=1, padx=10, pady=10)

# Display D
label_d = tk.Label(window, text="D (Private Key):")
label_d.grid(row=7, column=0, padx=10, pady=10)
label_d_value = tk.Label(window, text="")
label_d_value.grid(row=7, column=1, padx=10, pady=10)

# Display Encrypted Text
label_encrypted = tk.Label(window, text="Encrypted Text:")
label_encrypted.grid(row=8, column=0, padx=10, pady=10)
label_encrypted_value = tk.Label(window, text="")
label_encrypted_value.grid(row=8, column=1, padx=10, pady=10)

# Display Decrypted Text
label_decrypted = tk.Label(window, text="Decrypted Text:")
label_decrypted.grid(row=9, column=0, padx=10, pady=10)
label_decrypted_value = tk.Label(window, text="")
label_decrypted_value.grid(row=9, column=1, padx=10, pady=10)


window.mainloop()