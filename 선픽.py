html_ad = ""
for item in champions_ad:
    name = item["name"]
    src = item["image_url"]
    html_ad += f"<a href='#' id='{name}'><img src='{src}'></a>"

html_sup = ""
for item in champions_sup:
    name = item["name"]
    src = item["image_url"]
    html_sup += f"<a href='#' id='{name}'><img src='{src}'></a>"

# Central container for alignment
col1, col2 = st.columns(2)
clicked = None
with col1:
    with st.container():
        clicked = click_detector(html_ad)

with col2:
    with st.container():
        st.write(clicked)
        result = call_example(clicked)

        st.subheader("Team")
        cols_team = st.columns(len(result['team']))
        for idx, item in enumerate(result['team']):
            for champ in champions_ad + champions_sup:
                if champ["name"] == item:
                    cols_team[idx].image(champ['image_url'])

        st.subheader("Counter")
        cols_counter = st.columns(len(result['counter']))
        for idx, item in enumerate(result['counter']):
            for champ in champions_ad + champions_sup:
                if champ["name"] == item:
                    cols_counter[idx].image(champ['image_url'])

st.divider()

col1, col2 = st.columns(2)
clicked = None
with col1:
    with st.container():
        clicked = click_detector(html_sup)

with col2:
    with st.container():
        st.write(clicked)
        result = call_example(clicked)

        st.subheader("Team")
        cols_team = st.columns(len(result['team']))
        for idx, item in enumerate(result['team']):
            for champ in champions_ad + champions_sup:
                if champ["name"] == item:
                    cols_team[idx].image(champ['image_url'])

        st.subheader("Counter")
        cols_counter = st.columns(len(result['counter']))
        for idx, item in enumerate(result['counter']):
            for champ in champions_ad + champions_sup:
                if champ["name"] == item:
                    cols_counter[idx].image(champ['image_url'])
