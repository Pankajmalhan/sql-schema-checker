
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache,SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))


SCHEMA_ANALYZER_PROMPT ="""You are a {dialect} expert tasked with examining a given table schema. 
Based on the SQL dialect provided and the provided table schema, your task is to verify the schema
for correctness and suggest improvements if necessary. Begin by thoroughly examining the entire schema,
paying particular attention to data types, constraints (especially those found at the end of the schema),
primary keys, foreign keys, and other relevant elements.
After verifying the schema, provide suggestions for any necessary corrections or enhancements.
Ensure your suggestions are clear and actionable, aiming to optimize the structure and performance
of the table based on best practices and the requirements of the SQL dialect specified.

### Table schema
{schema}
### Table schema

SCHEMA_ANALYZER_RESULT = 

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