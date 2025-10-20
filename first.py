import streamlit as st
import pandas as pd
st.markdown('# 学生 粟梦桃-数字档案')
st.markdown('## 🔑基础信息')
st.markdown(':green[注册时间⏲:2025-10-20 |精神状态:活人微死😵]')
st.markdown(':green[当前教室🌏:实训楼204 | 安全等级:一般]')
st.subheader('天气情况🌥︎')
c1, c2, c3 = st.columns(3)
c1.metric(label="温度🌡", value="22℃", delta="-1.5℃")
c2.metric(label="湿度", value="63%", delta="6%")
c3.metric(label="空气质量", value="良好", delta="0", delta_color="off")
st.subheader('任务日志🗓️')
data = {
    '日期':['2025/10/20','2025/10/21','2025/10/22'],
    '任务':['学习📚︎','旅游✈','睡觉💤'],
    '状态':['完成☑︎','未完成🗙','进行中⏩️']}
index = pd.Series(['1', '2', '3'])
df = pd.DataFrame(data, index=index)
st.write(df)
st.subheader('最新代码成果')
st.subheader('Python代码块')
python_code = '''def hello():
    print("你好，Streamlit！")
'''
st.code(python_code, language=None)
st.code(python_code)
st.markdown('>>SYSTEM MESSAGE:下一个任务目标已解锁...')
st.markdown(':red[>>TARGET:课程管理系统]')
st.markdown('***')
st.markdown('>>COUNTDOWM:2025-10-20 14:30:25')
st.markdown('系统状态：在线 连接状态：已加密')
