from io import BytesIO
import streamlit as st
import pandas as pd


@st.cache
def convert_df_csv(df):
    '''
    Convert pandas dataframe into csv file
    '''
    return df.to_csv(encoding='utf-8', index=False)

@st.cache
def convert_df_excel_binary(df):
    '''
    Convert pandas dataframe into binary file
    '''
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    value = output.getvalue()
    return value


def download_button(data, file_type):
    '''
    Generate download button based on file type
    '''
    if file_type == 'CSV':
        st.download_button(label = 'Download CSV',
                           data = data,
                           file_name = 'file.csv',
                           mime = 'text/csv')

    elif file_type == 'Excel':
        st.download_button(label='Download Excel',
                           data=data,
                           file_name = 'file.xlsx',
                           mime = 'application/octet-stream')


def main_page():

    st.title('Hello World! This is a test')

    uploaded_file = st.file_uploader(label='Upload your Excel file here', type=['xlsx', 'csv'])

    if uploaded_file is not None:
        st.write('File loaded: ', uploaded_file.name)
        if '.xlsx' in uploaded_file.name:
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        st.dataframe(df)


        selection = st.radio(label="select download file type",
                             options=['CSV', 'Excel'])

        if selection == "CSV":
            csv = convert_df_csv(df)
            download_button(csv, selection)
        elif selection == "Excel":
            excl = convert_df_excel_binary(df)
            download_button(excl, selection)
        else:
            pass

if __name__ == "__main__":
    main_page()