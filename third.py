import streamlit as st
st.set_page_config(page_title='风景',page_icon='✈')
images=[
    {
        'ur1':'https://www.10wallpaper.com/wallpaper/1920x1440/1704/Russia_highest_mountain-Nature_Scenery_Wallpaper_1920x1440.jpg',
        'parm':'风景'
    },
    {
        'ur1':'https://cdn.audleytravel.com/-/-/79/210031149142101052004074089220161086008213071165.jpg',
        'parm':'风景'
    },
    {
        'ur1':'https://cdn.wallpapersafari.com/18/42/mYxvzp.jpg',
        'parm':'风景'
    }
]

if  'ind' not in st.session_state:
    st.session_state['ind']=0

def nextlmg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(images)
st.image(images[st.session_state['ind']]['ur1'],caption=images[st.session_state['ind']]['parm'])
c1,c2=st.columns(2)
with c1:
    st.button('上一张',on_click=nextlmg,use_container_width=True)

with c2:
    st.button('下一张',on_click=nextlmg)
