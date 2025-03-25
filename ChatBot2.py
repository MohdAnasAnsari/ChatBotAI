from langchain.chat_models import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

# Start Ollama API before running: ollama serve
Ollama_API_URL = "http://localhost:11434"

# Use a smaller, faster model
llm = ChatOllama(model="gemma", base_url=Ollama_API_URL)

# Limit memory to keep only the last 5 interactions
memory = ConversationBufferWindowMemory(k=5)

# Optimized prompt for speed
prompt = PromptTemplate(
    input_variables=["history", "user_input"],
    template="You're a smart chatbot. Keep replies short. \n{history}\nUser: {user_input}\nChatbot:"
)

def chatbot():
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        # Retrieve history and format prompt
        history = memory.load_memory_variables({}).get("history", "")
        formatted_prompt = prompt.format(history=history, user_input=user_input)
        
        # Stream the response for faster user feedback
        print("Chatbot: ", end="")
        response = llm.invoke(formatted_prompt)
        for chunk in response.content:
            print(chunk, end="", flush=True)
        print()
        
        # Store conversation history
        memory.save_context({"input": user_input}, {"output": response.content})

if __name__ == "__main__":
    chatbot()