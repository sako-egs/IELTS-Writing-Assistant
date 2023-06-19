import streamlit as st
from langchain.llms import OpenAI

st.set_page_config(layout="wide")
st.markdown('## ✏️ IELTS Writing Task2 Evaluation System with ChatGPT')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type="password")

def generate_response(input_prompt):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_prompt))

with st.form('my_form'):
    question = st.text_area('Input a task:', '')
    essay = st.text_area(f'Input your essay:', '', height=250)
    submitted_ct = st.form_submit_button('word count')
    if submitted_ct and essay:
        words_ct = len(essay.split())
        st.write(f'現在{words_ct}文字')
    else:
        st.write(f'現在0文字')
  
    prompt =f"""
    You know everything about scoring IELTS essays. You assess the given essay of the given question and provide feedback and specify mistakes and suggest corrections.
    Your output must be a JSON following this structure: ｛"band": the band, "feedback": your feedback (maximum 100 words), "mistakes":[｛"mistake 1": the whole sentence,"correction 1": a correction for that sentence｝,｛"mistake 2": ・・・｝]｝
  
    Question: {question}
  
    Essay:{essay}
  
    JSON:
    """
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
   
    if submitted and openai_api_key.startswith('sk-'):
        if not question or not essay:
            st.warning('質問あるいはエッセイが入力されていません。', icon='⚠') 
        else:
            with st.spinner("評価中..."):
                generate_response(prompt)
