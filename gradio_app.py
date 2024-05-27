import gradio as gr
from llm_backend import generate_sql_query, get_schema_info, query_database, reset_connection, correct_sql_error

def respond(message, chat_history):
    try:
        schema_info = get_schema_info()
        sql_query, llm_response = generate_sql_query(message, schema_info)
        try:
            result = query_database(sql_query)
            # Format the result for better readability
            result_str = "\n".join([str(row) for row in result])
            bot_message = f"SQL Query:\n{sql_query}\n\nResult:\n{result_str}"
        except Exception as e:
            # If an error occurs, attempt to correct the SQL query
            corrected_sql_query = correct_sql_error(schema_info, sql_query, str(e))
            try:
                result = query_database(corrected_sql_query)
                # Format the result for better readability
                result_str = "\n".join([str(row) for row in result])
                bot_message = f"Original SQL Query:\n{sql_query}\n\nError:\n{e}\n\nCorrected SQL Query:\n{corrected_sql_query}\n\nResult:\n{result_str}"
            except Exception as correction_error:
                if "current transaction is aborted" in str(correction_error):
                    reset_connection()
                    bot_message = "Error: Transaction aborted. Restarted the backend service."
                else:
                    bot_message = f"Error after correction attempt: {correction_error}\n\nOriginal SQL Query:\n{sql_query}\n\nError:\n{e}"
            llm_response = f"Original Response:\n{llm_response}\n\nCorrection Response:\n{correction_error}"
    except Exception as e:
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

demo.launch()