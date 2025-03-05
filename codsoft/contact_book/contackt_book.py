import tkinter as tk
from tkinter import messagebox
import json 
import re 

#contact book
contact_book = 'contact_book/contact.json'

#load contact from book
def load_contact():
    try:
        with open(contact_book, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
#save contact 
def save_contact(contacts):
    with open(contact_book, 'w') as f:
        json.dump(contacts, f, indent=4)

#add new contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error"," name and number required " )
        return
    
    if not phone.isdigit or len(phone) != 10:
        messagebox.showwarning("Input Error", "Phone number must contains only 10 digit...")
        return 

    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if email and not re.match(email_pattern, email):
        messagebox.showwarning("Input Error", "Invalid email format!")
        return
    
    contacts = load_contact()
    
    for contact in contacts:
        if contact["phone"] == phone:
            messagebox.showwarning("Duplicate Error", "This phone number is already added!")
            return
    
    contacts = load_contact()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contact(contacts)

    messagebox.showinfo("succes", "contact save succsefully ")
    entry_name.delete(0,tk.END)
    entry_phone.delete(0,tk.END)
    entry_email.delete(0,tk.END)
    entry_address.delete(0,tk.END)

    view_contacts()

#views all contacts
def view_contacts():
    contacts = load_contact()
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f'{contact['name']}- {contact['phone']}')

#search contact
def search_contact():
    search_term = entry_search.get()
    contacts = load_contact()
    listbox.delete(0,tk.END)
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact ['phone']:
            listbox.insert(0,tk.END, f"{contact['name']}- {contact['phone']}")


#delete contact
def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("selection error", 'plse select for delete')
        return
    contacts = load_contact()
    contacts.pop(selected[0])
    save_contact(contacts)
    messagebox.showinfo("succses", 'contact deleted')
    view_contacts()

#gui setup
root  = tk.Tk()
root.title("contact book")
root.geometry("500x500")

#lebel  and entry filed
tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="phone:").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text = "email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text = "address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

# buttons
tk.Button(root, text='add contact', command= add_contact).pack()

tk.Button(root, text="voew contct", command= view_contacts).pack()

#search features
tk.Label(root, text="search:").pack()
entry_search  = tk.Entry(root)
entry_search.pack() 
tk.Button(root, text='search', command= search_contact).pack()

#listbox to display  contact
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand= True)

#delete button
tk.Button(root, text= 'Delete contact', command= delete_contact).pack()

view_contacts()

root.mainloop()






        