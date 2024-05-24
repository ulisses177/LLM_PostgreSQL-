import psycopg2
import re
from langchain_community.llms import Ollama

# Database connection setup
conn = psycopg2.connect(
    dbname="my_database",
    user="my_user",
    password="1123",
    host="localhost",
    port="5432"
)

# Initialize LangChain with Ollama
llm = Ollama(model="llama3")

def get_schema_info():
    schema_info = ""
    with conn.cursor() as cursor:
        cursor.execute("""
        SELECT table_name, column_name 
        FROM information_schema.columns 
        WHERE table_schema = 'public'
        """)
        rows = cursor.fetchall()
        tables = {}
        for table_name, column_name in rows:
            if table_name not in tables:
                tables[table_name] = []
            tables[table_name].append(column_name)
        
        for table_name, columns in tables.items():
            schema_info += f"Table: {table_name}\nColumns: {', '.join(columns)}\n\n"
    return schema_info

def query_database(query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def extract_sql_query(response):
    # Use regex to extract the SQL query
    match = re.search(r"```sql\n(.*?)\n```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        raise ValueError(f"The generated response does not contain a valid SQL query.\n\nFull response:\n{response}")

def generate_sql_query(message, schema_info):
    prompt = (f"Generate a valid SQL query to retrieve data based on the following request, focus on the sql command, no need to explain it further: {message}\n"
              f"Database schema information:\n{schema_info}\n"
              "Example: SELECT * FROM table WHERE condition;")
    response = llm.invoke(prompt).strip()
    # Log the generated response for debugging
    print(f"Generated Response: {response}")
    sql_query = extract_sql_query(response)
    return sql_query, response

def reset_connection():
    global conn
    conn.close()
    conn = psycopg2.connect(
        dbname="my_database",
        user="my_user",
        password="1123",
        host="localhost",
        port="5432"
    )