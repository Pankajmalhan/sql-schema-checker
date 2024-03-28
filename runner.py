import streamlit as st
from schema_analyzer import sql_scheme_analysis

# Replace with your function to list database names
def get_database_names():
    # Replace with actual logic to list databases from your environment
    return ["PostgreSQL", "Oracle", "MySQL", "SQLite", "Sql Server",]

# Placeholder function to analyze schema (replace with your logic)
def analyze_schema(schema):
    return f"Schema with {len(schema.splitlines())} lines analyzed."

def main():
    """
    Streamlit app to display database names, take table schema, and show results.
    """

    # Get list of database names
    database_names = get_database_names()

    # Title and selection of database
    st.title("Table Schema Analyzer")
    selected_database = st.selectbox("Select Database", database_names)

    # Multi-line text field for schema
    schema = st.text_area("Enter Table Schema", height=200)

    # Button to trigger analysis
    analyze_button = st.button("Analyze Schema")

    # Result text area (initially disabled)
    # schema_result = ""
    # disable_result = True
    # result = st.text_area("Schema Result", height=200, value=schema_result, disabled=disable_result, key="result")

    # Display result only if button is clicked
# Display result only if button is clicked
    if analyze_button:
        with st.spinner("Analyzing schema..."):
            
            analysis_result = sql_scheme_analysis(selected_database, schema)
            st.text_area("Schema Result", height=400, value=analysis_result, key="result")


if __name__ == "__main__":
    main()
