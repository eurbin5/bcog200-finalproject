# bcog200-naming_shapes_project

In 1916 the principle of the arbitrariness of the sign first appeared in the foundational work of the Swiss linguist/philosopher, Ferdinand de Saussure in "Cours de linguistique générale."The principle states that there is no inherent/natural connection between words and what they signify, so their relationship is arbitrary. Then, in 1929, Wolfgang Köhler, a German psychologist, described the phenomenon we commonly know as the "Bouba Kiki effect." The modern version of the experiment observes a statistically significant number of people name the softer/rounded looking objects as "bouba," and the sharp/jagged looking shapes with "kiki." Then add onomatopoeia, with words like "POW," "buzz," and "woof," and we begin to see a pattern. So is the link really that arbitrary?

The goal of this project/experiment will be to explore the contrast between arbitrariness and perceived meaningfulness with abstract shapes and sounds in the English language. (Native English speaking) Participants will be tasks with creating a name for a number of novel shapes, each with their own set of properties such as: number of angles to represent "jaggedness," number of curves to represent "softness" etc. At the end of the naming process, a program will identify the letters/sounds(1) in the name and categorize them by their phonetic features, ex: place of articulation, manner of articulation, voice vs voiceless etc.
Another program will analyze the distrubution of these sounds and identify any recurring patterns that appear. For example, we may see a higher proportion of plosive sounds such as [t] [k] [p], which constrict the vocal tract, in shapes with a higher number of angles. By that same vein, perhaps more sonerant or nasal sounds appear with shapes that are more curved. 

Expected possible functions: 

collect_shape_names
This function would record the names each participant assigns to each shape and stores them. Every entry would link the participant's choice of name with the specific shape and its various properties.

analyze_phonetic_features
This function would break down a given name into its individual letters/sounds and categorizes them according to their phonetic features, storing the resulting feature data so it can compared later. 

identify_sound_shape_patterns
This function then analyzes all the phonetic data collected and examples whether certain sound types occure more or less frequently with particular shape properties, summarizes any recurring patterns found. 


1. (Deeper phonological/orthographical distinction between letters/sound to be explained later) 
