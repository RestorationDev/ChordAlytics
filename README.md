# ChordAlytics

ChordAlytics is a data-driven project that analyzes and generates chord progressions through pattens in music datasets. Leveraging Math and DS techniques, this project identifies chord similarities, progression patterns, and other song relationships all while providing interesting visualizations. 

# Features

	•	Chord Progression Analysis: Uses Markov Chains to model the *probability of chord transitions*.
	•	Graph-Based Visualizations: *Graph song representations*, where nodes correspond to chords, and undirected edges represent transitions.
	•	Clustering for Song Similarity: Graph *clustering techniques* for song similarities (Wasserstein).
	•	Eigenvalue Centrality: Ranks chords by their importance within progression paths, identifying central chords.
	•	Data Preprocessing: Parses and organizes *raw chord data into structured graph* representations for analysis, and 3 chord strings to offer more insight for a progression.
	•	Generative Capabilities: *Generates realistic chord sequences* based on observed patterns, aiding in music composition and analysis.

 # Technical Approach
	1.	Cleaning and Structuring
	•	Parsed *thousands of chord progressions from songs. Parsed in an arrangement of 3 chord sequences for contextual information about each chord
	•	Organized the data into graph structures where nodes represent chords.
	2.	Mathematical Modeling
	•	Markov Chains: Modeled chord transitions to predict future progressions.
	•	Eigenvalue Centrality: Used to rank the influence of individual chords in a song.
	•	Clustering: Applied clustering algorithms (e.g., Wasserstein) to group similar songs based on their graph properties.
 	•	Similarity: Further similarity analysis with matrix multiplications
	3.	Graph-Based Visualization
	•	Created visualizations using libraries like NetworkX to represent chord relationships and similarities between songs.

 # Technologies Used
	•	Python: Primary programming language.
 
	•	Libraries:
 	•	Pandas/Numpy for structuring graph/preprocessing and matrix operations.
	•	NetworkX for graph visualization.
	•	SciPy for optimizations and clustering.
	•	Matplotlib for plotting and visualizations.

# Applications
	•	Music Composition: Generate chord progressions to inspire musicians and composers.
	•	Music Similarity Analysis: Identify relationships and similarities between different songs.
	•	Educational Tool: Understand how chords interact and progress within songs.

 
 
