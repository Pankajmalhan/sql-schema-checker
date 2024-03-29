
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache,SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))

SCHEMA_ANALYZER_PROMPT = SCHEMA_ANALYZER_PROMPT = """
You are a {dialect} expert tasked with analyzing a table schema.
Based on the provided SQL dialect and the current table schema, your objective is to verify the schema's 
correctness and suggest improvements if necessary.
Begin by thoroughly examining the entire schema, focusing on data types, constraints 
(especially those found at the end of the schema), primary keys, foreign keys, and other relevant elements.
After verifying the schema, provide clear and actionable suggestions to optimize the structure and performance
of the table. Ensure your suggestions adhere to best practices and meet the requirements of the specified SQL dialect.
Please provide your suggestions as a bullet list below.

### Table Schema:
{schema}
### Table Schema:

Suggestions:
"""

GENERATE_UPDATED_SCHEMA_TABLE = """
As a {dialect} expert, you will receive the current table schema and instructions for updating it.
Your objective is to generate the updated schema based on the provided instructions, 
ensuring correctness, actionability, and optimization of the table structure and performance according to best practices.

### Current Table Schema:
{schema}
### Current Table Schema:

### Instructions:
{instructions}
### Instructions:

Updated Table Schema:
"""


def sql_scheme_analysis(dialect:str, schema:str):
    """
    Given a SQL dialect and a table schema, this function will return a string
    containing the analysis result.
    """
    prompt = ChatPromptTemplate.from_template(
        SCHEMA_ANALYZER_PROMPT
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-3.5-turbo")
    chain = (
          prompt
        | model
        | output_parser
    )

    return chain.invoke({"dialect":dialect, "schema":schema})

def create_update_schema(dialect:str, schema:str, instructions:str):
    print(instructions)
    """
    Given a SQL dialect, schema and instruction . Generated the updated schema
    for given dialect
    """

    prompt = ChatPromptTemplate.from_template(
        GENERATE_UPDATED_SCHEMA_TABLE
    )
    output_parser = StrOutputParser()
    model = ChatOpenAI(model="gpt-3.5-turbo")
    chain = (
          prompt
        | model
        | output_parser
    )

    return chain.invoke({"dialect":dialect, "schema":schema, "instructions":instructions})  