from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
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

#Attach the structure to the LLM
structured_llm = llm.with_structured_output(ResearchResponse)

#Create Parser that expects JSON
# parser = JsonOutputParser()


# Create system prompt to respond in JSON format
system_prompt = """
You are a research assistant.
Research the given topic thoroughly and respond with accurate information.
    """

messages = [
    SystemMessage(content=system_prompt),
    HumanMessage(content="Research about Black Holes")
]

response = structured_llm.invoke(messages)

#Print raw response
# print("RAW RESPONSE - ", response.content)

# Parse the raw text into a Python dictionary
# result = parser.parse(response.content)

# Print results
print(response.topic)
print(response.summary)
print(response.key_facts)
print(response.conclusion)


















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
