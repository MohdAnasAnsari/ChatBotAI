# from flask import Flask, request, jsonify, render_template
# from langchain.llms import Ollama
# from langchain.memory import ConversationBufferWindowMemory

# app = Flask(__name__)

# # Initialize Ollama (Using API Mode)
# llm = Ollama(model="gemma", base_url="http://localhost:11434")

# # Memory to store conversation (keeps last 5 messages)
# memory = ConversationBufferWindowMemory(k=5)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_input = request.json.get("message")
    
#     # Get chat history
#     history = memory.load_memory_variables({}).get("history", "")

#     # Create the prompt
#     prompt = f"{history}\nUser: {user_input}\nChatbot:"

#     # Generate response
#     response = llm.invoke(prompt)
    
#     # Store new interaction in memory
#     memory.save_context({"input": user_input}, {"output": response})

#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(debug=True)
# ================================
from flask import Flask, render_template, request, Response
import time
import ollama  # Ollama for local AI model

app = Flask(__name__)

def stream_response(user_input):
    """Stream words one by one for real-time effect"""
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
    bot_response = response['message']['content']

    # Send response word by word with formatting
    for word in bot_response.split():
        yield f"{word} "  # Append space after each word
        time.sleep(0.05)  # Delay for smooth effect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    return Response(stream_response(user_message), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
