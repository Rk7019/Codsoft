import turtle
import random
import string
import time # Optional: for slight pauses

# --- Constants ---
PRIMARY_COLOR = "#FFDEDE" # Define the requested color as a constant
ERROR_COLOR = "red"
CANCEL_COLOR = "orange"
BACKGROUND_COLOR = "#8F87F1"

# --- Screen and Writer Turtle Setup ---
screen = turtle.Screen()
screen.title("Turtle Password Generator")
screen.setup(width=400, height=300) # Adjust window size if needed
screen.bgcolor(BACKGROUND_COLOR)

# Create a turtle specifically for writing text
writer = turtle.Turtle()
writer.hideturtle() # We don't need to see the turtle icon
writer.penup()      # Don't draw lines when moving
writer.speed(0)     # Fastest speed for writing
writer.color("black") # Set the initial color
PROMPT_FONT = ("Arial", 14, "normal")
PASSWORD_FONT = ("Courier", 18, "bold") # Use a monospace font for password
ERROR_FONT = ("Arial", 12, "normal")
EXIT_FONT = ("Arial", 10, "italic")

def display_message(message, y_pos=50, font=PROMPT_FONT, color="black"):
    """Clears previous messages and displays a new one."""
    writer.clear() # Clear previous text written by this turtle
    writer.color("black") # Use the specified color (defaults to PRIMARY_COLOR)
    writer.goto(0, y_pos)
    writer.write(message, align="center", font=font)
    writer.color("black") # Reset to the primary color after writing

# --- Password Generation Logic (Unchanged) ---
def generate_password(length):
    """Generates a password of the specified length."""
    # Define characters
    elements = string.ascii_letters + string.digits + string.punctuation
    # Generate password
    password = ''.join(random.choice(elements) for _ in range(length)) # Use _ for unused loop variable
    return password

# --- Main Application Logic ---

display_message("Password Generator", 80)
time.sleep(0.5) # Optional pause

# Get password length from the user via turtle dialog
length = None
while length is None:
    display_message("Requesting password length...", 50) # Uses default PRIMARY_COLOR
    length_str = screen.textinput("Password Length", "Enter the desired password length:")

    if length_str is None: # User pressed Cancel
        display_message("Operation cancelled by user.", 0, font=ERROR_FONT, color="black")
        time.sleep(2)
        length = 0 # Set length to 0 to indicate cancellation downstream
        break # Exit the loop

    try:
        length_val = int(length_str)
        if length_val > 0:
            length = length_val # Assign the valid integer length
            # No need to break here, loop condition (length is None) becomes false
        else:
            display_message(f"Length '{length_val}' is not positive.\nPlease enter a positive number.", 0, font=ERROR_FONT, color="black")
            time.sleep(2) # Give time to read the error
    except ValueError:
        display_message(f"Invalid input: '{length_str}'.\nPlease enter a valid number.", 0, font=ERROR_FONT, color="black")
        time.sleep(2) # Give time to read the error

# Check if we got a valid length (or if it was cancelled)
if length and length > 0:
    # Generate and print the password using turtle
    display_message("Generating password...", 50) # Uses default PRIMARY_COLOR
    password = generate_password(length)
    time.sleep(0.5) # Simulate generation time

    # Display the final password
    writer.clear()
    writer.goto(0, 20)
    # Explicitly set color here if needed, but display_message already resets it
    writer.color("black")
    writer.write("Generated Password:", align="center", font=PROMPT_FONT)
    writer.goto(0, -20)
    # Ensure password also uses the primary color (or choose another if desired)
    writer.color("black")
    writer.write(password, align="center", font=PASSWORD_FONT)
else:
    # Handle the case where length wasn't set (e.g., cancellation or initial error)
    if length == 0: # Specifically check for our cancellation signal
         # Cancellation message was already displayed with CANCEL_COLOR
         # Optional: Display a final cancellation confirmation if needed
         display_message("Password generation cancelled.", 0, color="black") # Re-display if needed
    else: # Should ideally not happen with current logic, but good practice
        display_message("Could not generate password.", 0, font=ERROR_FONT, color="black")


# --- Keep Window Open ---
writer.goto(0,-100)
writer.color("black") # Ensure exit message uses the primary color
writer.write("Click on the screen to exit.", align="center", font=EXIT_FONT)
screen.exitonclick()