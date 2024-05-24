import gradio as gr
from llm_backend import generate_sql_query, get_schema_info, query_database, reset_connection

def respond(message, chat_history):
    try:
        schema_info = get_schema_info()
        sql_query, llm_response = generate_sql_query(message, schema_info)
        result = query_database(sql_query)
        # Format the result for better readability
        result_str = "\n".join([str(row) for row in result])
        bot_message = f"SQL Query:\n{sql_query}\n\nResult:\n{result_str}"
    except Exception as e:
        if "current transaction is aborted" in str(e):
            reset_connection()
            bot_message = "Error: Transaction aborted. Restarted the backend service."
        else:
            bot_message = f"Error: {e}"
        llm_response = str(e)
    chat_history.append((message, bot_message))
    chat_history.append(("LLM Response", llm_response))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch(share=True)
