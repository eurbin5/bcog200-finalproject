import csv
import os
import matplotlib.pyplot as plt


SUMMARY_FILE = "data/summary.csv"
FIGURES_FOLDER = "figures"


def load_sound_class_counts(filename):

    data = {}

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    current_shape_type = ""

    for row in rows:
        if len(row) == 0:
            continue

        if len(row) >= 3 and row[1] == "sound_class":
            current_shape_type = row[0]
            data[current_shape_type] = {}

        elif current_shape_type != "" and len(row) >= 3:
            shape_type = row[0]
            sound_class = row[1]
            count = row[2]

            if shape_type == current_shape_type and count.isdigit():
                data[current_shape_type][sound_class] = int(count)

    return data


def convert_counts_to_percentages(data):

    percentage_data = {}

    for shape_type in data:
        total = sum(data[shape_type].values())
        percentage_data[shape_type] = {}

        for sound_class in data[shape_type]:
            if total > 0:
                percentage = data[shape_type][sound_class] / total * 100
            else:
                percentage = 0

            percentage_data[shape_type][sound_class] = percentage

    return percentage_data


def make_sound_class_graph(data):

    if not os.path.exists(FIGURES_FOLDER):
        os.makedirs(FIGURES_FOLDER)

    shape_types = ["sharp", "rounded", "mixed"]

    sound_classes = [
        "sonorant",
        "voiceless_stop",
        "voiced_stop",
        "fricative",
        "affricate",
        "high_vowel",
        "mid_vowel",
        "low_vowel"
    ]

    x_positions = list(range(len(shape_types)))
    bar_width = 0.09

    plt.figure(figsize=(12, 6))

    for i, sound_class in enumerate(sound_classes):
        percentages = []

        for shape_type in shape_types:
            if shape_type in data and sound_class in data[shape_type]:
                percentages.append(data[shape_type][sound_class])
            else:
                percentages.append(0)

        shifted_positions = []

        for x in x_positions:
            shifted_positions.append(x + i * bar_width)

        plt.bar(
            shifted_positions,
            percentages,
            width=bar_width,
            label=sound_class
        )

    center_positions = []

    for x in x_positions:
        center_positions.append(x + bar_width * (len(sound_classes) - 1) / 2)

    plt.xticks(center_positions, shape_types)
    plt.xlabel("Shape Type")
    plt.ylabel("Percentage of Sounds")
    plt.title("Sound Class Percentages by Shape Type")
    plt.legend(fontsize=8)
    plt.tight_layout()

    plt.savefig("figures/sound_class_percentages.png")
    plt.show()


def main():
    sound_class_counts = load_sound_class_counts(SUMMARY_FILE)
    percentage_data = convert_counts_to_percentages(sound_class_counts)
    make_sound_class_graph(percentage_data)

    print("Graph complete!")
    print("Graph saved to figures/sound_class_percentages.png")


if __name__ == "__main__":
    main()