import streamlit as st
import pandas as pd

# Load Excel file once
xls = pd.ExcelFile("Material_Selection_Notes.xlsx")
sheet_names = xls.sheet_names

st.title("Material Selection Interface")
st.markdown("Select a sheet to explore and query material data.")

# Dropdown for sheet selection
selected_sheet = st.selectbox("Select a Sheet", sheet_names)

# Try to read the sheet
try:
    if selected_sheet == "Materials":
        # Skip first row, set proper headers from second row
        df = pd.read_excel(xls, sheet_name=selected_sheet, header=1)
    else:
        df = pd.read_excel(xls, sheet_name=selected_sheet)

    st.subheader(f"Preview of `{selected_sheet}`")
    st.dataframe(df)

    # Optional: Search functionality
    search_query = st.text_input("Search materials (by keyword):")

    if search_query:
        result_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
        st.write(f"🔍 Results for: `{search_query}`")
        st.dataframe(result_df)

except Exception as e:
    st.error(f"Failed to read sheet `{selected_sheet}`: {e}")
