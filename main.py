from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
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

while True:

    #LLM thinks and responds
    response = llm_with_tools.invoke(messages)

    #Add LLM response to messahe history
    messages.append(response)

    #Check if LLM wants to use tools
    if not response.tool_calls:
        print("The agent has the answer. No need of the tools...")
        break # exit the loop

    for tool_call in response.tool_calls:
        print(f"Agent using tool: {tool_call['name']}")
        print(f"With input: {tool_call['args']}\n")

    #which tool to run
    if tool_call["name"] == "duckduckgo_search":
        tool_result = search_tool.invoke(tool_call["args"])

    elif tool_call["name"] == "get_word_count":
        tool_result = get_word_count.invoke(tool_call["args"])

    #append the responses gather with the help of tool
    messages.append(ToolMessage(
        content = str(tool_result),
        tool_call_id=tool_call["id"]
    ))

#Final instruction
messages.append(HumanMessage(
    content = "Based on your research, provide the final structured response"
))

#Attach the structure to the LLM
structured_llm = llm.with_structured_output(ResearchResponse)
response = structured_llm.invoke(messages)


# Print results
print("---------- SEARCH RESULTS ----------")
print(response.topic)
print(response.summary)
print(response.key_facts)
print(response.conclusion)