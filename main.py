from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    source: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-5")
#response = llm.invoke("What is the meaning of life?")
#print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse) # This parser will now allow us to essentially
# take the output of the llm and parse it into this (class ResearchResponse(BaseModel) model and then we use it like
# a normal python object inside of our code.

# Next we need to set up a prompt.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools.
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),


    ]
)