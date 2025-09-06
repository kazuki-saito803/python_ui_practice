from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd


col1, col2 = st.columns(2)

with col1:
    st.title('サプーアプリ')
    st.caption('これはテストアプリです。')
    st.subheader('自己紹介')
    st.text('pythonに関する情報をYoutube上で発信しているPython VTuverサプーです。¥n'
            'よろしければチャンネル登録お願いします！')
    code = '''
    import streamlit as st

    st.title(サプーアプリ)
    '''
    st.code(code, language='python')

    # 画像
    # image = Image.open('sapu.png')
    # st.image(image, width=200)

    age_category = st.selectbox(
        '年齢層',
        ('子供', '大人')
    )


with col2:
    with st.form(key='profile_form'):
        name = st.text_input('name')
        address = st.text_input('address')
        # print(name)

        # ボタン
        submit_btn = st.form_submit_button('submit')
        cancel_btn = st.form_submit_button('cancel')
        
        age_category = st.radio(
            '年齢層',
            ('子供', '大人')
        )
        hobby = st.multiselect(
            '趣味',
            ('sport', 'read', 'programing', 'anime', 'movie')
        )
        if submit_btn:
            print(name)
            
    markdown = '''
    # はじめに
    1. a
    1. b
    1. c
    '''
    st.markdown(markdown)
    df = pd.DataFrame({
        'a_column':[1, 2, 3, 4, 5],
        'b_column':[6, 7, 8, 9,10]
    })
    st.dataframe(df)
