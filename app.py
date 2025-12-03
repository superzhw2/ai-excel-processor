import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Excel处理器", layout="wide")
st.title("🤖 AI Excel智能处理器")

st.write("欢迎使用AI Excel处理器！这是一个演示应用。")

# 简单的文件上传演示
uploaded_file = st.file_uploader("上传Excel文件", type=['xlsx', 'xls'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(f"📊 成功读取文件: {uploaded_file.name}")
    st.write(f"数据形状: {df.shape}")
    st.dataframe(df.head())

st.success("✅ 应用运行正常！")