# pip install langchain, unstructured, openai, chromadb, Cython, tiktoken, pdfminer, pdfminer.six, pyproject, streamlit, streamlit-chat

# Import the Packages
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator


# Import API Keys
import os
os.environ["OPENAI_API_KEY"] = 'OPENAI API KEY HERE'

# Import Streamlit
import streamlit as st
from streamlit_chat import message

# Setup the Streamlit App
# Display the Page Title and the text box for the user to ask the question
st.title('APP#2: 🦜️🔗 Ask :red[Questions] to PDF') #Shows the title in the web app
st.header('Please Wait while we get ready🎈')


root_dir = "D:/Torr\PROMPT_ENGINEER/23-Ask_a_PDF"

pdf_folder_path = f'{root_dir}/data'
print(os.listdir(pdf_folder_path))

loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]
print(loaders)

index = VectorstoreIndexCreator().from_loaders(loaders)
print(index)


prompt = st.text_input("Enter your query about the PDF/PDFs")

if prompt:
    response = index.query_with_sources(prompt)
    # The response is a dict with 3 items. Lets split the items
    question = response['question']
    answer = response['answer']
    sources = response['sources']

    # Write the results from the LLM to the UI
    st.write("<b>" + question + "</b><br><i>" + answer + "</i>" + "</b><br>" + "Sources:  "+ sources + "<hr>", unsafe_allow_html=True )


