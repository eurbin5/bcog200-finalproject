import random
import csv
import os
import tkinter as tk
from PIL import Image, ImageTk


DATA_FILE = "data/responses.csv"

shape_files = sorted(os.listdir("stimuli"))
shape_files = [file for file in shape_files if file.endswith(".png")]

random.shuffle(shape_files)

current_shape_index = 0
participant_id = ""
participant_name = ""


def get_next_participant_id():
    if not os.path.exists(DATA_FILE):
        return "001"

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        return "001"

    existing_ids = []

    for row in rows[1:]:
        if len(row) > 0 and row[0].isdigit():
            existing_ids.append(int(row[0]))

    if len(existing_ids) == 0:
        return "001"

    next_id = max(existing_ids) + 1
    if next_id < 10:
        participant_id = "00" + str(next_id)
    elif next_id < 100:
        participant_id = "0" + str(next_id)
    else:
        participant_id = str(next_id)

    return participant_id


def write_header_if_needed():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "participant_id",
                "participant_name",
                "trial_number",
                "shape_name",
                "response"
            ])


def load_image(shape_file):
    image = Image.open(os.path.join("stimuli", shape_file))
    image.thumbnail((500, 500))
    return ImageTk.PhotoImage(image)


def start_experiment():
    global participant_id, participant_name, photo

    participant_name = name_entry.get().strip()

    if participant_name == "":
        start_prompt.config(text="Please enter your name to begin.")
        return

    write_header_if_needed()
    participant_id = get_next_participant_id()

    start_prompt.pack_forget()
    name_entry.pack_forget()
    start_button.pack_forget()

    id_label.config(text=f"Participant ID: {participant_id}")
    id_label.pack()

    photo = load_image(shape_files[current_shape_index])
    image_label.config(image=photo)

    prompt.config(text="What would you name this shape?")
    prompt.pack()

    entry.pack()
    button.pack()


def save_response():
    global current_shape_index, photo

    response = entry.get().strip()
    shape_file = shape_files[current_shape_index]
    trial_number = current_shape_index + 1

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            participant_id,
            participant_name,
            trial_number,
            shape_file,
            response
        ])

    entry.delete(0, tk.END)
    current_shape_index += 1

    if current_shape_index >= len(shape_files):
        image_label.config(image="")
        prompt.config(text="Experiment complete! Thank you.")
        entry.pack_forget()
        button.pack_forget()
    else:
        photo = load_image(shape_files[current_shape_index])
        image_label.config(image=photo)


root = tk.Tk()
root.title("Shape Naming Experiment")
root.geometry("900x550")

start_prompt = tk.Label(root, text="Enter your name:")
start_prompt.pack()

name_entry = tk.Entry(root)
name_entry.pack()

start_button = tk.Button(root, text="Start Experiment", command=start_experiment)
start_button.pack()

id_label = tk.Label(root)

image_label = tk.Label(root)
image_label.pack()

prompt = tk.Label(root)

entry = tk.Entry(root)

button = tk.Button(root, text="Next", command=save_response)

root.mainloop()