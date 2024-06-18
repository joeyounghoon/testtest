import streamlit as st

# Streamlit 페이지 구성
st.set_page_config(layout="wide")

# 사이드바에 들어가는 타이틀
st.sidebar.title('OptimalBotAI')

# Streamlit 페이지에 CSS 적용하기!
st.markdown(
    """
    <style>
    body {
        overflow: hidden;
    }
    .main {
        background-color: #f0f2f6;
        display: flex;
        flex-direction: row;
        height: 100vh;
        justify-content: center; /* 가운데 정렬 추가 */
    }
    .sidebar {
        padding: 10px;
        background-color: #d3d3d3;
        position: relative;
        user-select: auto;
        width: 336px;
        height: 842px;
        box-sizing: border-box;
        flex-shrink: 0;
    }
    .champion-section {
        width: 100%;
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
        align-items: center; /* 가운데 정렬 추가 */
    }
    .champion-list-content {
        width: 300px;
        height: 350px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
    }
    .recommend-champ-title {
        margin-top: 10px;
        font-size: 15px;
        font-weight: bold;
        text-align: left;
        color: black;
    }
    .divider {
        width: 100%;
        height: 2px;
        position: absolute;
        top: 50%;
        z-index: 99999;
        background-color: black;
    }

    /* 미디어 쿼리 패딩 제거 */
    @media (min-width: 576px) {
        .st-emotion-cache-1jicfl2 {
            padding-left: 0 !important;
            padding-right: 0 !important;
        }
    }

    /* 스크롤바 제거 */
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 0;
        min-width: auto;
        max-width: initial;
    }

    /* streamlit 기본 상단 바 제거 */
    .st-emotion-cache-h4xjwg {
        height: 0;
    }

    /* 여백 안남게 scroll-margin 제거 */
    .st-emotion-cache-1jzia57 h1, 
    .st-emotion-cache-1jzia57 h2, 
    .st-emotion-cache-1jzia57 h3, 
    .st-emotion-cache-1jzia57 h4, 
    .st-emotion-cache-1jzia57 h5, 
    .st-emotion-cache-1jzia57 h6, 
    .st-emotion-cache-1jzia57 span {
        scroll-margin-top: 0;
    }

    /* streamlit에서 기본으로 제공하는 공유, 깃허브 링크 등등 바 설정 */
    .st-emotion-cache-15ecox0.ezrtsby0 {
        background-color: black;
        border-radius: 10px;
    }

    /* 화면 상단 gap 제거 */
    .st-emotion-cache-1wmy9hl div {
        gap: 0;
    }

    /* 여백 제거 */
    .st-emotion-cache-ul70r3 {
        margin-bottom: 0;
    }

    .champion-image {
        border-radius: 50%;
        width: 160px;
        height: 160px;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit markdown으로 구성!
st.markdown(
    """
    <div class='divider'></div>
    <div class='sidebar'>
        <div class='champion-section'>
            <h5 class='recommend-champ-title'>원딜 추천 챔피언</h5>
            <div class="champion-list-content">
            </div>
        </div>
        <div class='champion-section'>
            <h5 class='recommend-champ-title'>서폿 추천 챔피언</h5>
            <div class="champion-list-content">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)

champions_ad=[{
    "name" : "애쉬",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ashe.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"카이사",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kaisa.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"케이틀린",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Caitlyn.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"징크스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jinx.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"진",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jhin.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"자야",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Xayah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"바루스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Varus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"이즈리얼",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ezreal.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"사미라",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Samira.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"베인",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Vayne.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"스몰더",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Smolder.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"제리",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zeri.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"드레이븐",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Draven.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"루시안",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lucian.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"미스포츈",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/MissFortune.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"닐라",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nilah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"시비",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Sivir.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"코그모",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/KogMaw.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"코르키",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Corki.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"트리스타나",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Tristana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"트위치",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Twitch.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"아펠리오스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Aphelios.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"직스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ziggs.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"칼리스타",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kalista.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
]

champions_sup=[{
    "name" : "노틸러스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nautilus.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"럭스",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lux.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"블리츠크랭크",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Blitzcrank.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"마오카이",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Maokai.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"레오나",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Leona.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"쓰레쉬",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Thresh.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"유미",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Yuumi.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"브라움",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Braum.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"모르가나",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Morgana.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"소나",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Sona.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"소라카",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Soraka.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"스웨인",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Swain.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"자크",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zac.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"룰루",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Lulu.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"니코",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Neeko.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"뽀삐",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Poppy.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"알리스타",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Alistar.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"세라핀",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Seraphine.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"렐",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Rell.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"라칸",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Rakan.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"자이라",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Zyra.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"파이크",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Pyke.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"흐웨이",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Hwei.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
{
    "name":"나미",
    "image_url":"https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Nami.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
},
              
]

# 중앙 정렬을 위한 컨테이너
col1, col2 = st.columns(2)
with col1:
    with st.container():
        cols = st.columns(6)
        for i in range(len(champions_ad)):
            with cols[i % 6]:
                champion_ad = champions_ad[i]
                st.image(champion_ad["image_url"], caption=champion_ad["name"])
with col2:
    with st.container():
        st.write("test")

st.divider()

with st.container():
    cols = st.columns(6)
    for i in range(len(champions_sup)):
        with cols[i % 6]:
            champion_sup = champions_sup[i]
            st.image(champion_sup["image_url"], caption=champion_sup["name"])
