# Shape Naming Experiment


## Background

In 1916 the principle of the arbitrariness of the sign was described in the foundational work of the Swiss linguist/philosopher, Ferdinand de Saussure in *Cours de linguistique générale*. The principle states that there is no inherent or natural connection between words and what they signify, so their relationship is arbitrary.

Then, in 1929, Wolfgang Köhler, a German psychologist, described the phenomenon we commonly know as the "Bouba Kiki effect." The modern version of the experiment observes a statistically significant number of people naming softer, rounded objects as "bouba" and sharp, jagged shapes as "kiki."

Add in onomatopoeia, with words like "POW," "buzz," and "woof," and we begin to see a pattern. So is the link really that arbitrary?

The goal of this project/experiment is to explore the contrast between arbitrariness and perceived meaningfulness with abstract shapes and sounds in the English language. (Native English speaking)

Participants are tasked with creating a name for a number of novel shapes, each with their own set of properties such as number of angles to represent "jaggedness," number of curves to represent "softness," etc.

At the end of the naming process, a program identifies the letters/sounds in the name and categorizes them by their phonetic features (e.g., voice vs. voiceless, sonorant vs. fricative, vowel height, etc.).

Another program analyzes the distribution of these sounds and identifies any recurring patterns that appear. For example, we may see a higher proportion of plosive sounds such as [t], [k], and [p] in shapes with a higher number of angles. By that same vein, perhaps more sonorant or nasal sounds appear with shapes that are more curved.

## Project Structure

### `main.py`
Runs the shape naming experiment.

Participants are shown a series of novel abstract shapes and are asked to invent names for them. Responses are automatically saved to a CSV file along with:

- participant ID
- participant name
- trial number
- shape shown
- participant response

### `analysis.py`
Analyzes naming trends across shape categories.

Shapes are categorized into:

- sharp
- rounded
- mixed

The analysis identifies sounds across the entire invented word rather than only the beginning of the word.

Sound combinations such as:

`ch`, `sh`, `th`, `ph`

are treated as single sounds.

The program categorizes sounds by phonetic properties including:

- sonorants
- voiced stops
- voiceless stops
- fricatives
- affricates
- vowel height (high, mid, low)

Analysis results are saved to:

`data/summary.csv`

### `graphs.py`
Generates graphs showing sound distribution trends across shape categories.

Graphs compare the percentage of sound classes used in names assigned to:

- sharp shapes
- rounded shapes
- mixed shapes

Generated figures are saved to:

`figures/`

## Installation

Install required packages:

```bash
pip install -r requirements.txt
```

This project also uses `tkinter`, which comes with standard Python installations.

## How to Run

### Run the experiment

Launch the naming experiment:

```bash
python main.py
```

Participant responses will automatically be saved to:

`data/responses.csv`

### Run the analysis

Analyze sound trends in participant responses:

```bash
python analysis.py
```

Analysis results will be saved to:

`data/summary.csv`

### Generate graphs

Create graphs of sound distribution trends:

```bash
python graphs.py
```

Generated graphs will be saved to:

`figures/`

## Testing

The project includes tests for several core functions used in the analysis pipeline.

Tests include:

- cleaning participant responses
- extracting sounds from responses
- categorizing sound classes

Run tests with:

```bash
python tests/test_project.py
```

## Project Files

```text
main.py        → runs the experiment
analysis.py    → analyzes sound patterns
graphs.py      → generates figures

stimuli/       → experimental shape stimuli
data/          → participant responses and summaries
figures/       → generated graph
```

## Note

This project focuses on broad sound-symbolic trends in invented naming behavior rather than strict phonetic transcription. Because participants produce written responses, orthographic patterns are used as an approximation for phonological tendencies.