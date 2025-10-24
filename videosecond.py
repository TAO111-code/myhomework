import streamlit as st
st.subheader("展示视频")
st.set_page_config(page_title='视频网站',page_icon='📺')
video_ur1=[{
    'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/02/17/28943451702/28943451702-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=771356656&uipk=5&gen=playurlv3&os=cosovbv&platform=html5&trid=fe9416912da2498c9eb17212bf7b901h&deadline=1761302137&nbs=1&og=hw&upsig=6d3c0fd97f731e522bf39df86e7b3c03&uparams=e,mid,oi,uipk,gen,os,platform,trid,deadline,nbs,og&bvc=vod&nettype=0&bw=773496&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
    'title':'奶龙搞怪大作战',
    'episode':'1'
},
    {
    'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/83/71/27329957183/27329957183-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&oi=771356656&uipk=5&trid=d215eaa7a68e4045ae28352fe8cd86bh&platform=html5&mid=0&gen=playurlv3&og=hw&deadline=1761302287&os=cosovbv&upsig=20a5812c0cce598e3c14b0394885bcb0&uparams=e,nbs,oi,uipk,trid,platform,mid,gen,og,deadline,os&bvc=vod&nettype=0&bw=799933&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
    'title':'奶龙爆笑嘉年华',
    'episode':'2'
    },
        {
    'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/58/15/28235991558/28235991558-1-192.mp4?e=ig8euxZM2rNcNbRghWdVhwdlhWN1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&uipk=5&trid=5f90a4de668b4d30bfcce4f6b474898h&oi=771356656&gen=playurlv3&og=cos&deadline=1761302414&platform=html5&mid=0&os=cosovbv&upsig=cd12570a6ac4313ce4b33dd9ff83064d&uparams=e,nbs,uipk,trid,oi,gen,og,deadline,platform,mid,os&bvc=vod&nettype=0&bw=972761&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
    'title':'奶龙抓螃蟹',
    'episode':'3'
}]
if 'ind' not in st.session_state:
    st.session_state['ind']=0
st.title(video_ur1[st.session_state['ind']]['title']+'-第'+video_ur1[st.session_state['ind']]['episode']+'集')
st.video(video_ur1[st.session_state['ind']]['ur1'])

c1,c2,c3=st.columns(3)

def play(arg):
    st.text(arg)
    st.session_state['ind']=int(arg)
for i in range(len(video_ur1)):
    st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
