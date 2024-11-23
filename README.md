
# ChromaDB Test Application
> This application demonstrates the integration of [**Chromadb**](https://docs.trychroma.com/) with a [**Streamlit**](https://docs.streamlit.io/) interface to create, store, and search documents using embeddings. The app allows users to create documents, insert them into a ChromaDB collection, and perform search queries to retrieve relevant results.

## Features
* Document Management: Create and display a list of documents with unique identifiers.
* Integration with ChromaDB:
    1. Store documents into a ChromaDB collection.
    2. Perform semantic searches to find similar documents.
* Streamlit Interface:
    1. User-friendly and interactive design.
    2. Real-time feedback with dynamic updates.

## Prerequisites

Ensure the following are installed:

* Python 3.8 or later
* Required Python packages (see Installation)

## Installation

1. Clone this repository:
```
git clone https://github.com/JustEmkay/Learn.Chroma.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Install ChromaDB:
```
pip install chromadb
```

4. Run the Streamlit application:
```
streamlit run app.py
```

## Usage

1. Create Documents:

    * Enter text in the input field and click "Create doc" to add a new document.
    * View the list of created documents in a table.

2. Insert into ChromaDB:

    * After creating documents, click "Insert into ChromaDB" to store them in the database.

3. Search Documents:

    * Enter a query in the "Search query using ChromaDB" section and click "Search query".
    * The search results are displayed in an expandable panel.

4. Clear Documents:

    * Use the "Clear all" button to remove all created documents from the session state.
