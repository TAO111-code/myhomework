import streamlit as st
st.subheader("展示视频")
st.set_page_config(page_title='视频网站',page_icon='📺')
video_ur1=[{
    'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/15/80/33356448015/33356448015-1-192.mp4?e=ig8euxZM2rNcNbRMhWdVhwdlhWK1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&trid=64660f58a29d4ca3be70c9a0a214d1fh&mid=0&gen=playurlv3&os=cosovbv&og=cos&uipk=5&deadline=1761901018&nbs=1&oi=771356656&upsig=d2fb4ce4e14b9c737832571ea528eb1b&uparams=e,platform,trid,mid,gen,os,og,uipk,deadline,nbs,oi&bvc=vod&nettype=0&bw=1129506&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
    'title':'西湖奶龙',
    'episode':'1'
},
    {
    'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/89/39/28525333989/28525333989-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=997a8d3d5fac41fc8fd519c1a8a5d28h&os=cosovbv&uipk=5&gen=playurlv3&og=cos&mid=0&deadline=1761901495&platform=html5&nbs=1&oi=771356656&upsig=d7e840a284653135a2f2fb98f2ece78c&uparams=e,trid,os,uipk,gen,og,mid,deadline,platform,nbs,oi&bvc=vod&nettype=0&bw=627118&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'奶龙',
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
