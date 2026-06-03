from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

#This is the search tool
search = DuckDuckGoSearchRun()

search_tool = Tool(
    name = "search_web",
    func = search.run,
    description = "Search the web for information",
)