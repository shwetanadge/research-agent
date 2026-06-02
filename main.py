from dotenv import load_dotenv
from pydantic import BaseModel
# from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
import os

#Load .env
load_dotenv()

#define the structure we want from LLM
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

#Initialize Groq LLM
# to test the API - print(os.getenv("GROQ_API_KEY"))
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("YOUR_GROQ_API_KEY")
)

#Create Parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)


# Create prompt template
prompt = ChatPromptTemplate.from_template(
    """
You are a research assistant.

Answer the following question.

Return your response ONLY in the format below:

{format_instructions}

Question:
{query}
"""
)


# Build prompt
formatted_prompt = prompt.invoke(
    {
        "query": "What is the capital of Germany?",
        "format_instructions": parser.get_format_instructions(),
    }
)


# Send to model
response = llm.invoke(formatted_prompt)


# Parse into Pydantic object
parsed_response = parser.parse(response.content)


# Print results
print(parsed_response)
print()
print("Topic:", parsed_response.topic)
print("Summary:", parsed_response.summary)
print("Sources:", parsed_response.sources)
print("Tools Used:", parsed_response.tools_used)


# #Create Prompt Template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
#             You are a research assistant that will help generate a research paper.
#             Answer the user query and use neccessary tools. 
#             Wrap the output in this format and provide no other text\n{format_instructions}
#             """,
#         ),
#         ("placeholder", "{chat_history}"),
#         ("human", "{query}"),
#         ("placeholder", "{agent_scratchpad}"),
#     ]
# ).partial(format_instructions=parser.get_format_instructions())

# # agent = create_agent(
# #     llm=llm,
# #     prompt=prompt,
# #     tools=[]
# # )

# agent = create_agent(
#     model=llm,
#     tools=[]
# )

# agent_executor = create_agent(agent=agent, tools=[], verbose=True)

# response = agent.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "What is the capital of Germany?"
#             }
#         ]
#     }
# )
# -----------------------------------------------------

# raw_response = agent_executor.invoke({"query": "What is the capital of Germany?"})
# print(raw_response)









# response = llm.invoke("What is the meaning of life")
# print(response.content)

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
