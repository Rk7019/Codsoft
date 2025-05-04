import tkinter as tk
from tkinter import messagebox # For showing messages

# --- Global List to Store Tasks (in-memory only) ---
# This list will hold our to-do items (as strings)
tasks = []

# --- GUI Functions ---

def populate_listbox():
    """Clears and refills the listbox based on the global tasks list."""
    listbox_tasks.delete(0, tk.END) # Clear all items from the listbox
    if not tasks:
        listbox_tasks.insert(tk.END, "  (List is empty)") # Placeholder message
        listbox_tasks.itemconfig(0, {'fg': 'grey'}) # Make placeholder grey
    else:
        for i, task in enumerate(tasks):
            listbox_tasks.insert(tk.END, f"{i + 1}. {task}") # Add task with number
            listbox_tasks.itemconfig(i, {'fg': 'black'}) # Ensure text is black


def add_task_gui():
    """Adds a task from the entry field to the list."""
    task_description = entry_task.get().strip() # Get text from the entry field
    if task_description:
        tasks.append(task_description) # Add to the Python list
        populate_listbox() # Update the listbox display
        entry_task.delete(0, tk.END) # Clear the entry field
        print(f"Task '{task_description}' added (in memory).") # Optional console log
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty.")

def delete_task_gui():
    """Deletes the selected task from the list."""
    try:
        # Get the index of the currently selected item
        selected_index_tuple = listbox_tasks.curselection()

        # Check if anything is selected
        if not selected_index_tuple:
             messagebox.showwarning("Selection Error", "Please select a task to delete.")
             return

        selected_index = selected_index_tuple[0] # Get the first selected index

        # Make sure the selected index is valid (and not the placeholder)
        if tasks and 0 <= selected_index < len(tasks):
            # Optional: Confirmation dialog
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete:\n'{tasks[selected_index]}'"):
                removed_task = tasks.pop(selected_index) # Remove from Python list
                populate_listbox() # Update the listbox display
                print(f"Task '{removed_task}' deleted (in memory).") # Optional console log
        elif not tasks:
             messagebox.showinfo("Info", "List is already empty.")
        else:
             # This case handles selecting the "(List is empty)" placeholder
             messagebox.showwarning("Selection Error", "Cannot delete the placeholder text.")

    except IndexError:
        # This might happen if the list changes unexpectedly, though less likely here
         messagebox.showerror("Error", "Selected index is out of range.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# --- Set up the main GUI window ---
root = tk.Tk()
root.title("Simple To-Do List (Not Saved)")
root.geometry("400x350") # Set window size (width x height)
root.configure(bg='#f0f0f0') # Optional: Light grey background for the window

# --- Create GUI Widgets ---

# Frame for input and add button
input_frame = tk.Frame(root, bg='#f0f0f0') # Match window background
input_frame.pack(pady=10) # Add padding above/below

label_entry = tk.Label(input_frame, text="New Task:", bg='#f0f0f0') # Match frame background
label_entry.pack(side=tk.LEFT, padx=5)

entry_task = tk.Entry(input_frame, width=30, font=('Arial', 10)) # Specify font
entry_task.pack(side=tk.LEFT, padx=5)
# Allow pressing Enter in the entry field to add task
entry_task.bind("<Return>", lambda event: add_task_gui())

# --- MODIFIED: Add Task Button with Color ---
button_add_task = tk.Button(
    input_frame,
    text="Add Task",
    command=add_task_gui,
    bg="#28a745",  # Green background color
    fg="white",    # White text color
    activebackground="#218838", # Slightly darker green when clicked
    activeforeground="white",
    borderwidth=0, # Remove border for a flatter look
    relief=tk.FLAT # Use flat relief style
    )
button_add_task.pack(side=tk.LEFT, padx=5, ipady=2) # ipady adds internal padding

# Frame for the listbox and scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True) # Allow frame to expand

# Listbox to display tasks
listbox_tasks = tk.Listbox(
    list_frame,
    height=10,
    width=50,
    selectmode=tk.SINGLE,
    font=('Arial', 10),
    borderwidth=0,
    highlightthickness=1, # Add a subtle border around listbox
    highlightbackground="#cccccc"
    )
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar for the listbox
scrollbar_tasks = tk.Scrollbar(list_frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Link scrollbar to listbox
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# --- MODIFIED: Delete Task Button with Color ---
button_delete_task = tk.Button(
    root,
    text="Delete Selected Task",
    command=delete_task_gui,
    width=20,
    bg="#dc3545",  # Red background color
    fg="white",    # White text color
    activebackground="#c82333", # Slightly darker red when clicked
    activeforeground="white",
    borderwidth=0, # Remove border
    relief=tk.FLAT # Use flat relief style
    )
button_delete_task.pack(pady=10, ipady=2) # ipady adds internal padding

# --- Initial Population and Main Loop ---
populate_listbox() # Show initial state (empty list placeholder)

root.mainloop() # Start the Tkinter event loop (makes the window interactive)