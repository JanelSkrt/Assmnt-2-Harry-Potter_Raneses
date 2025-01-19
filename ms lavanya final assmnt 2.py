import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Character data with added image field
character_data = [
    {"name": "Harry Potter", "house": "Gryffindor", "role": "The protagonist and the 'Boy Who Lived.'", "image_path": "C:/Users/dell/Downloads/harry.png"},
    {"name": "Hermione Granger", "house": "Gryffindor", "role": "Harry's intelligent and resourceful best friend.", "image_path": "C:/Users/dell/Downloads/hermione.png"},
    {"name": "Ron Weasley", "house": "Gryffindor", "role": "Harry's loyal best friend from the Weasley family.", "image_path": "C:/Users/dell/Downloads/Ron.png"},
    {"name": "Albus Dumbledore", "house": "Gryffindor", "role": "The wise headmaster of Hogwarts.", "image_path": "C:/Users/dell/Downloads/Albus.png"},
    {"name": "Severus Snape", "house": "Slytherin", "role": "The enigmatic Potions Master and key figure in the story."},
    {"name": "Lord Voldemort", "house": "Slytherin", "role": "The main antagonist and dark wizard."},
    {"name": "Rubeus Hagrid", "house": "Gryffindor", "role": "The gentle half-giant and Hogwarts gamekeeper."},
    {"name": "Draco Malfoy", "house": "Slytherin", "role": "Harry's school rival and a Slytherin student."},
    {"name": "Ginny Weasley", "house": "Gryffindor", "role": "Ron’s sister and Harry’s eventual love interest."},
    {"name": "Neville Longbottom", "house": "Gryffindor", "role": "A brave Gryffindor student who plays a crucial role."},
    {"name": "Luna Lovegood", "house": "Ravenclaw", "role": "The quirky and insightful Ravenclaw student."},
    {"name": "Sirius Black", "house": "Gryffindor", "role": "Harry’s godfather and a member of the Order of the Phoenix."},
    {"name": "Remus Lupin", "house": "Gryffindor", "role": "A kind werewolf and former Defense Against the Dark Arts professor."},
    {"name": "Bellatrix Lestrange", "house": "Slytherin", "role": "A devoted Death Eater and Voldemort's follower."},
    {"name": "Molly Weasley", "house": "Gryffindor", "role": "The caring matriarch of the Weasley family."},
    {"name": "Arthur Weasley", "house": "Gryffindor", "role": "The curious and kind patriarch of the Weasley family."},
    {"name": "Fred Weasley", "house": "Gryffindor", "role": "One of Ron's mischievous twin brothers."},
    {"name": "George Weasley", "house": "Gryffindor", "role": "Fred's twin and co-creator of Weasleys' Wizard Wheezes."},
    {"name": "Minerva McGonagall", "house": "Gryffindor", "role": "The strict yet fair Transfiguration professor."},
    {"name": "Dolores Umbridge", "house": "None", "role": "The tyrannical Ministry official and Defense Against the Dark Arts professor."}
]

# Function to search for a character
def fetch_character_data(character_name):
    for character in character_data:
        if character_name.lower() == character["name"].lower():
            return character
    return None

# Function to display the character data
def display_character_info(character):
    if character:
        # Load and resize the character image
        try:
            # Open the image using PIL
            character_image = Image.open(character["image_path"])

            # Resize the image to a fixed size (e.g., 100x100 pixels)
            character_image = character_image.resize((100, 100))  # We can change this size as needed

            # Convert the image to a PhotoImage format that Tkinter can use
            character_image_tk = ImageTk.PhotoImage(character_image)

            # Update the image in the label
            character_image_label.config(image=character_image_tk)
            character_image_label.image = character_image_tk

        except:
            character_image_label.config(image=None)

        # Display character information
        info = f"Name: {character['name']}\nHouse: {character['house']}\nRole: {character['role']}"
        result_label.config(text=info)
    else:
        result_label.config(text="Character not found.")
        character_image_label.config(image=None)  # Hide the image if character is not found

# Function to handle search button click
def on_search_button_click():
    character_name = search_entry.get()
    if character_name:
        character = fetch_character_data(character_name)
        display_character_info(character)
    else:
        messagebox.showwarning("Input Error", "Please enter a character name.")

# Set up the GUI
root = tk.Tk()
root.title("Harry Potter Search App")
root.geometry("800x600")  # Set window size

# Add a background image (optional)
bg_image = tk.PhotoImage(file="C:/Users/dell/Downloads/hrypotter.png")  # Replace with your image path
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Define the color scheme (Purple and Gray)
purple_color = "#6a0dad"
gray_color = "#808080"

# Create the main search frame with gray color background
search_frame = tk.Frame(root, bg=gray_color, highlightbackground="white", highlightthickness=1)
search_frame.pack(pady=20)

# Entry widget with purple border and gray background
search_entry = tk.Entry(search_frame, width=30, font=("Helvetica", 14), bg=gray_color, fg=purple_color, relief="solid", bd=2)
search_entry.grid(row=0, column=0, padx=10)

# Search button with purple background and white text
search_button = tk.Button(search_frame, text="Search Character", command=on_search_button_click, font=("Helvetica", 14), bg=purple_color, fg="white", relief="solid")
search_button.grid(row=0, column=1, padx=10)

# Frame to hold both character information and image
result_frame = tk.Frame(root, bg=gray_color)
result_frame.pack(pady=20)

# Label to display the character's image beside the info (left side)
character_image_label = tk.Label(result_frame, bg=gray_color)
character_image_label.grid(row=0, column=0, padx=10)

# Label to display search results with purple text (right side)
result_label = tk.Label(result_frame, text="Results will be displayed here.", font=("Helvetica", 16), justify=tk.LEFT, bg=gray_color, fg=purple_color)
result_label.grid(row=0, column=1, padx=20)

# Start the Tkinter main loop
root.mainloop()
