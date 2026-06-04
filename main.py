from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
from tools import search_tool, get_word_count
import os

#Load .env
load_dotenv()

#Initialize Groq LLM
# to test the API - print(os.getenv("GROQ_API_KEY"))
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("YOUR_GROQ_API_KEY")
)

#define the structure we want from LLM - pydantic
class ResearchResponse(BaseModel):
    topic: str = Field(description="Title of the object")
    summary: str = Field(description="2-3 sentences line summary")
    key_facts: list[str] = Field(description="list few facts")
    conclusion: str = Field(description="one line conclusion")


#All available tools
tools= [search_tool, get_word_count]

#Bind tools to agent
llm_with_tools = llm.bind_tools(tools)  

# Create system prompt to respond in JSON format
system_prompt = """
You are a research assistant.
Research the given topic thoroughly and respond with accurate information.
    """

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content="Research about Black Holes")
]

#=======THE AGENT LOOP========

print("Agent starting...")



#Attach the structure to the LLM
structured_llm = llm.with_structured_output(ResearchResponse)
response = structured_llm.invoke(messages)


# Print results
print("---------- SEARCH RESULTS ----------")
print(response.topic)
print(response.summary)
print(response.key_facts)
print(response.conclusion)