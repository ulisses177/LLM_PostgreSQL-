**Gradio SQL Chatbot with LangChain and Ollama**
====================================================

Introduction
------------

This project demonstrates a chatbot application that generates and
executes SQL queries based on natural language input. The chatbot 
uses Gradio for the user interface, LangChain with Ollama for 
natural language processing, and PostgreSQL as the database.

**Features**

* Natural Language Processing (NLP) using LangChain with Ollama
* User-friendly interface provided by Gradio
* Ability to generate and execute SQL queries based on user input

**Components**
-------------

### llm_backend.py

This file contains the backend code for the chatbot. It uses 
LangChain with Ollama to process natural language input and 
generate SQL queries.

### gradio_app.py

This file contains the Gradio app code, which provides a 
user-friendly interface for interacting with the chatbot.

**Setup**
------

To run this project, you'll need to:

1. Install the required dependencies using `pip install -r 
requirements.txt`
2. Set up your PostgreSQL database and configure the connection 
details in `llm_backend.py`
4. Run `python gradio_app.py` to start the Gradio app

**Usage**
------

To use the chatbot, simply navigate to the URL provided by Gradio 
(e.g., `http://localhost:7860`) and start interacting with the 
chatbot using natural language input.

**Example Output**
-----------------

Here are some examples of how the chatbot might respond to user 
input:

* User: "What is the name of the municipality where Água Verde 
neighborhood is located?"
Chatbot: "The Água Verde neighborhood is located in the Curitiba 
municipality."
* User: "What are the names of all the bairros in Pinhais 
municipality?"
Chatbot: "The bairros in Pinhais municipality are: Afonso Pena, 
Centro, Weissópolis."
* User: "What is the name of the rua that intersects with Avenida 
Visconde de Guarapuava in Batel neighborhood?"
Chatbot: "The rua that intersects with Avenida Visconde de 
Guarapuava in Batel neighborhood is Rua XV de Novembro."

**Code Explanation**
-------------------

### llm_backend.py

This file contains functions for generating and executing SQL 
queries. The `get_schema_info()` function retrieves database 
schema information, the `query_database()` function executes a SQL
query and returns the result, the `extract_sql_query()` function 
extracts the generated SQL query from the response, and the 
`generate_sql_query()` function generates a SQL query based on 
user input.

### gradio_app.py

This file contains the Gradio app code. The `respond()` function 
processes user input, generates a SQL query, executes the query, 
formats the result for better readability, and handles any errors 
that may occur during execution. The `demo.launch(share=True)` 
line starts the Gradio app.

**Examples from Schema**
-------------------------

Here are some examples of how you can use the chatbot to query the
schema:

* User: "What is the name of the municipality where Água Verde 
neighborhood is located?"
Chatbot: "The Água Verde neighborhood is located in the Curitiba 
municipality."
* User: "What are the names of all the bairros in Pinhais 
municipality?"
Chatbot: "The bairros in Pinhais municipality are: Afonso Pena, 
Centro, Weissópolis."
* User: "What is the name of the rua that intersects with Avenida 
Visconde de Guarapuava in Batel neighborhood?"
Chatbot: "The rua that intersects with Avenida Visconde de 
Guarapuava in Batel neighborhood is Rua XV de Novembro."

**Contributing**
--------------

If you'd like to contribute to this project or report any issues, 
please feel free to open a pull request or create an issue on 
GitHub.

**License**
--------

This project is licensed under the MIT License. See `LICENSE` for 
details.

