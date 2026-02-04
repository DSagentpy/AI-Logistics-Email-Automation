from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from models import ProgramacaoEntrega
from dotenv import load_dotenv

load_dotenv()

parser = PydanticOutputParser(pydantic_object=ProgramacaoEntrega)

prompt = ChatPromptTemplate.from_template(
"""
Você é um assistente logístico.

Extraia do email:

- material
- volume
- data e horário previsto

Email:
{email}

Formato:
{format_instructions}
"""
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chain = prompt | llm | parser

def extrair_dados(email_texto):
    return chain.invoke({
        "email": email_texto,
        "format_instructions": parser.get_format_instructions()
    })
