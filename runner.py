import streamlit as st
from schema_analyzer import sql_scheme_analysis, create_update_schema

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
    generate_code_button = st.button("Generate Updated Schema")

    # Result text area (initially disabled)
    if 'analysis_result' not in st.session_state:
        st.session_state['analysis_result'] = ""
    if 'updated_schema' not in st.session_state:
        st.session_state['updated_schema'] = ""

    # Display result only if button is clicked
    if analyze_button:
        with st.spinner("Analyzing schema..."):
            analysis_result = sql_scheme_analysis(selected_database, schema)
            st.session_state['analysis_result'] = analysis_result
            st.text_area("Schema Result", height=400, value=analysis_result, key="result")

    if generate_code_button:
        with st.spinner("Generating updated schema..."):
            updated_schema = create_update_schema(selected_database, schema, st.session_state['analysis_result'])
            st.session_state['updated_schema'] = updated_schema
            st.text_area("Updated Schema", height=400, value=updated_schema, key="updated_schema")


if __name__ == "__main__":
    main()
