# HexaLite

### Ranked First in Code Innovation Series - associated with GitHub (08/2021)

An unsupervised method for text searching based on contextual similarity within a corpus.

![DEMO](/demo.gif)

### Pitch:

Have you ever felt pressured to find relevant information from a given subtext of a corpus of books? Have you ever been in a time crunch where you could not find relevant information while preparing notes or revising before important tests? In an online environment, where all our classes are recorded as video lectures and all notes provided as separate PDFs, it is increasingly difficult to coordinate and manage this data.

An indexing and searching tool, which uses AI (NLP) for maximal utilization in finding contextually similar scripts/paragraphs will greatly benefit students. We leverage statistical tools for indexing each page of a particular pdf and/or book as provided within the dataset. Contextual linguistic tools also allow us to manage multiple topics, discussions, and even subjects for a better and broader use case.

On the other hand, professional researchers, professors, and academia can use this as a quick surveying tool for citation searching. Allowing them to utilize large corpora of related work to find and distill only those with similar implementations to said discussion. The same can be applied in other field professions such as law and finance, where corresponding laws and/or analogous economy-bound cases can be picked up in a more refined manner.

The use of this product will cut down on manual labor, allowing more freedom towards important parts of the job. As we include modularity and lower the complexity of execution, we enable our product to be run on edge devices, such as mobile phones, tablets, or other personal devices. We deliver high-quality results and recommendations in record time, thus cutting down on time complexity.

## Usage:

### Step 1: Save PDFs

Save all your pdfs in a topic-wise manner, 

Eg: `./data/pdfs/topic_1/`

### Step 2: Pre-Process

```py
python preprocess.py
```

### Step 3: Search

Save you question in a `.txt` file, such as `question.txt` and proceed as follows:

```py
python search.py
```
