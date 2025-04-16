import turtle
import time # To add slight delays for readability

# --- Screen and Writer Turtle Setup ---
screen = turtle.Screen()
screen.title("Turtle Calculator")
screen.setup(width=400, height=300) # Adjust window size if needed
screen.bgcolor("#8F87F1")

# Create a turtle specifically for writing text
writer = turtle.Turtle()
writer.hideturtle() # We don't need to see the turtle icon
writer.penup()      # Don't draw lines when moving
writer.speed(0)     # Fastest speed for writing
writer.color("black")
FONT = ("Arial", 16, "normal")

def display_message(message, y_pos=40):
    """Clears previous messages and displays a new one."""
    writer.clear() # Clear previous text written by this turtle
    writer.goto(0, y_pos)
    writer.write(message, align="center", font=FONT)

def perform_operation_turtle():
    """Gets input via dialogs, performs calculation, and displays result."""

    display_message("Starting Calculation...")
    time.sleep(0.5) # Small pause

    num1 = None
    num2 = None
    operation = None

    # --- Get Number 1 ---
    while num1 is None:
        num1_str = screen.textinput("Input", "Enter number 1:")
        if num1_str is None: # User pressed Cancel
             display_message("Calculation cancelled.", -20)
             return False # Indicate cancellation
        try:
            num1 = float(num1_str)
        except ValueError:
            display_message(f"'{num1_str}' is not a valid number.\nPlease try again.", 0)
            time.sleep(1.5) # Give time to read the error
            display_message("Getting Number 1...", 50) # Reset prompt message


    # --- Get Number 2 ---
    while num2 is None:
        num2_str = screen.textinput("Input", f"Number 1 is {num1}\nEnter number 2:")
        if num2_str is None: # User pressed Cancel
             display_message("Calculation cancelled.", -20)
             return False # Indicate cancellation
        try:
            num2 = float(num2_str)
        except ValueError:
             display_message(f"'{num2_str}' is not a valid number.\nPlease try again.", 0)
             time.sleep(1.5)
             display_message("Getting Number 2...", 50) # Reset prompt message


    # --- Get Operation ---
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    prompt_ops = ', '.join(valid_operations)
    while operation is None:
        op_str = screen.textinput("Operation", f"Numbers are {num1}, {num2}\nEnter operation ({prompt_ops}):")
        if op_str is None: # User pressed Cancel
             display_message("Calculation cancelled.", -20)
             return False # Indicate cancellation

        op_str = op_str.lower().strip()
        if op_str in valid_operations:
            operation = op_str
        else:
            display_message(f"Invalid operation: '{op_str}'.\nChoose from: {prompt_ops}", 0)
            time.sleep(2)
            display_message("Getting Operation...", 50) # Reset prompt message

    # --- Perform Calculation ---
    result = None
    error = None

    display_message(f"Calculating {num1} {operation} {num2}...", 0)
    time.sleep(0.5)

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            error = "Error: Division by zero"
        else:
            result = num1 / num2

    # --- Display Result ---
    writer.clear() # Clear "Calculating..." message
    if error:
        writer.goto(0, 0)
        writer.color("red") # Use red for errors
        writer.write(error, align="center", font=FONT)
        writer.color("black") # Reset color
    elif result is not None:
        writer.goto(0, 20)
        writer.write(f"{num1} {operation} {num2} =", align="center", font=FONT)
        writer.goto(0, -20)
        writer.write(f"Result: {result}", align="center", font=("Arial", 20, "bold")) # Make result bigger
    else:
        # Should not happen with current logic, but good practice
        writer.goto(0,0)
        writer.write("An unexpected issue occurred.", align="center", font=FONT)

    return True # Indicate success


# --- Main Loop ---
display_message("Turtle Calculator\nBasic Arithmetic", 0)
time.sleep(1)

while True:
    calculation_completed = perform_operation_turtle()

    if not calculation_completed:
        # If cancelled, maybe ask again or just exit? Let's ask.
        time.sleep(1) # Pause after cancellation message

    # Ask if the user wants to continue using a text input dialog
    time.sleep(1) # Pause before asking to continue
    again = screen.textinput("Continue?", "Perform another calculation? (yes/no):")

    if again is None or again.lower().strip() != 'yes':
        break

# --- Cleanup ---
display_message("Calculator finished.\nClick screen to exit.", 0)
screen.exitonclick() # Keep the window open until clicked