import csv
from collections import Counter


DATA_FILE = "data/responses.csv"
SUMMARY_FILE = "data/summary.csv"


SHAPE_TYPES = { "shape01.png": "sharp", "shape02.png": "rounded", "shape03.png": "sharp", "shape04.png": "rounded", "shape05.png": "sharp", "shape06.png": "rounded", "shape07.png": "mixed", "shape08.png": "mixed", "shape09.png": "mixed", "shape10.png": "sharp", "shape11.png": "rounded", "shape12.png": "sharp", "shape13.png": "sharp", "shape14.png": "rounded", "shape15.png": "rounded", "shape16.png": "mixed", "shape17.png": "mixed", "shape18.png": "mixed" }


DIGRAPHS = ["ch", "sh", "th", "ph", "wh"]


SOUND_CLASSES = {
    "m": "sonorant",
    "n": "sonorant",
    "l": "sonorant",
    "r": "sonorant",
    "w": "sonorant",
    "y": "sonorant",

    "p": "voiceless_stop",
    "t": "voiceless_stop",
    "k": "voiceless_stop",

    "b": "voiced_stop",
    "d": "voiced_stop",
    "g": "voiced_stop",

    "f": "fricative",
    "v": "fricative",
    "s": "fricative",
    "z": "fricative",
    "h": "fricative",
    "sh": "fricative",
    "th": "fricative",
    "ph": "fricative",
    "wh": "fricative",

    "ch": "affricate",
    "j": "affricate",

   "a": "low_vowel",

    "e": "mid_vowel",
    "o": "mid_vowel",

    "i": "high_vowel",
    "u": "high_vowel"
}


def clean_response(response):
    response = response.lower().strip()
    response = response.replace("-", "")
    response = response.replace(" ", "")
    response = response.replace("'", "")

    return response 

def get_sounds(response):
    response = clean_response(response)

    sounds = []
    index = 0

    while index < len(response):
        if index + 1 < len(response):
            two_letters = response[index:index + 2]

            if two_letters in DIGRAPHS:
                sounds.append(two_letters)
                index += 2
            else:
                letter = response[index]

                if letter.isalpha():
                    sounds.append(letter)

                index += 1
        else:
            letter = response[index]

            if letter.isalpha():
                sounds.append(letter)

            index += 1

    return sounds


def get_sound_class(sound):
    if sound in SOUND_CLASSES:
        return SOUND_CLASSES[sound]

    return "other"


def load_responses(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return rows


def summarize_category(responses):
    all_sounds = []
    all_sound_classes = []
    response_lengths = []
    blank_responses = 0

    for response in responses:
        clean_name = clean_response(response)

        if clean_name == "":
            blank_responses += 1
        else:
            response_lengths.append(len(clean_name))

            sounds = get_sounds(clean_name)

            for sound in sounds:
                all_sounds.append(sound)
                all_sound_classes.append(get_sound_class(sound))

    sound_counts = Counter(all_sounds)
    sound_class_counts = Counter(all_sound_classes)

    total_responses = len(responses)
    total_sounds = len(all_sounds)
    unique_names = len(set(responses))

    if len(response_lengths) > 0:
        average_length = sum(response_lengths) / len(response_lengths)
    else:
        average_length = 0

    summary = {
        "total_responses": total_responses,
        "blank_responses": blank_responses,
        "unique_names": unique_names,
        "average_length": average_length,
        "total_sounds": total_sounds,
        "sound_counts": sound_counts,
        "sound_class_counts": sound_class_counts
    }

    return summary


def summarize_by_shape_type(rows):

    responses_by_type = {
        "rounded": [],
        "sharp": [],
        "mixed": []
    }

    for row in rows:
        shape_name = row["shape_name"]
        shape_type = SHAPE_TYPES[shape_name]

        response = clean_response(row["response"])
        responses_by_type[shape_type].append(response)

    category_summaries = {}

    for shape_type in responses_by_type:
        summary = summarize_category(responses_by_type[shape_type])
        category_summaries[shape_type] = summary

    return category_summaries


def save_summary(category_summaries, filename):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["shape_type", "measure", "value"])

        for shape_type in category_summaries:
            summary = category_summaries[shape_type]

            writer.writerow([shape_type, "total_responses", summary["total_responses"]])
            writer.writerow([shape_type, "blank_responses", summary["blank_responses"]])
            writer.writerow([shape_type, "unique_names", summary["unique_names"]])
            writer.writerow([shape_type, "average_length", summary["average_length"]])
            writer.writerow([shape_type, "total_sounds", summary["total_sounds"]])

            writer.writerow([])
            writer.writerow([shape_type, "sound_class", "count"])

            for sound_class, count in summary["sound_class_counts"].items():
                writer.writerow([shape_type, sound_class, count])

            writer.writerow([])
            writer.writerow([shape_type, "sound", "count"])

            for sound, count in summary["sound_counts"].items():
                writer.writerow([shape_type, sound, count])

            writer.writerow([])


def main():
    rows = load_responses(DATA_FILE)
    category_summaries = summarize_by_shape_type(rows)
    save_summary(category_summaries, SUMMARY_FILE)

    print("Analysis complete!")
    print("Summary saved to data/summary.csv")


if __name__ == "__main__":
    main()