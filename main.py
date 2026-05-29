from dotenv import load_dotenv
# from pydantic import BaseModel
from groq import Groq
from langchain_groq import ChatGroq
import os

load_dotenv()

print(os.getenv("YOUR_GROQ_API_KEY"))
llm = ChatGroq(model="llama-3.3-70b-versatile")
response = llm.invoke("What is the meaning of life")
print(response.context)

#set up an LLM
# llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")
# response = llm.invoke("What is the meaning of life?")
# print(response)

# client = Groq(api_key=os.getenv("YOUR_GROQ_API_KEY"))

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "What is the meaning of life",
#         }
#     ],
#     model="llama-3.3-70b-versatile",
# )

# print(chat_completion.choices[0].message.content)
