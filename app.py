from matplotlib.image import thumbnail
import streamlit as st
from streamlit_option_menu import option_menu
from googleapiclient.discovery import build
import requests
import time
from annotated_text import annotated_text
# import re
# import pandas as pd
# import seaborn as sns
# import numpy as np


api_key = 'AIzaSyCP4oQ89ADb7YeDPlOwFLdsek3neSCUv0g'
youtube = build('youtube', 'v3', developerKey=api_key)

st.set_page_config(page_title="TubeStack ", page_icon=":zap:", layout="wide")

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("TUBESTACK TOOLS")

selected = option_menu(
    menu_title="Best Tools For Video Optimization",
    options=["Video SEO Checker",
             "Video Engagement Checker", "Video Best Practices"],
    default_index=0,
    orientation="horizontal",
)

#############################   Tool Number 1   ##################################


if selected == "Video SEO Checker":
    st.title("Video SEO Calculator For Tracking A Video's Performance 🔥")
    st.write("\n")
    st.text("➡️ You want to about the mistakes you are doing while uploading videos? NO ISSUE we got solution for all your problem regarding Video SEO!")
    st.text("TubeStack provides Video SEO Tool which detects the SEO mistakes you are doing which have to be done correctly")

    link = \
        st.text_input('YOUTUBE VIDEO LINK   (eg -> https://www.youtube.com/watch?******************* )'
                      )

    def seoChecker(youtube):
        parsed = link.split("v=")
        Id = parsed[1]
        request = youtube.videos().list(part="snippet,contentDetails,statistics", id=Id)
        response = request.execute()
        tags = []
        title_score = 0
        desc_score = 0
        tags_score = 0
        tdt_score = 0
        td_score = 0
        seo_score = 0

        if 'tags' in response['items'][0]['snippet'].keys():
            tags.append(response['items'][0]['snippet']['tags'])
        str_tags = "".join(str(tags))
        str_tags = str_tags.replace("[[\'", "")
        str_tags = str_tags.replace("\']]", "")
        str_tags = str_tags.replace("\', \'", " ")
        str_tags = str_tags.lower()
        # st.write(str_tags)
        tagsList = list(str_tags.split(" "))
        # st.write(tagsList)
        tags_set = set(tagsList)
        title = response['items'][0]['snippet']['title']
        title = str(title)
        title = title.lower()
        titleList = list(title.split(" "))
        # st.write(titleList)
        title_set = set(titleList)
        st.subheader("TUBESTACK SEO SCORE FOR THIS VIDEO! ")
        if (title_set & tags_set):
            title_score = title_score + 20
            st.subheader(f"✔️ Tags in Title: {title_score}/20")
        else:
            st.subheader(f"❌ Tags in Title: {title_score}/20")

        description = response['items'][0]['snippet']['description']
        description = str(description)
        description = description.lower()
        descList = list(description.split(" "))
        desc_set = set(descList)
        if (desc_set & tags_set):
            desc_score = desc_score + 20
            st.subheader(f"✔️ Tags in Description: {desc_score}/20")
        else:
            st.subheader(f"❌ Tags in Description: {desc_score}/20")

        if ((title_set & tags_set) and (desc_set & tags_set)):
            tdt_score = tdt_score + 20
            st.subheader(f"✔️ Tags in Title & Description: {tdt_score}/20")
        else:
            st.subheader(f"❌ Tags in Title & Description: {tdt_score}/20")

        if(len(tagsList) > 50):
            tags_score = tags_score + 20
            st.subheader(f"✔️ Total Tag Characters: {tags_score}/20")
        else:
            st.subheader(f"❌ Total Tag Characters: {tags_score}/20")

        if (title_set & desc_set):
            td_score = td_score + 20
            st.subheader(f"✔️ Title Words in Description: {td_score}/20")
        else:
            st.subheader(f"❌ Title Words in Description: {td_score}/20")

        seo_score = title_score + desc_score + tags_score + tdt_score + td_score

        st.title(f"VIDEO SEO SCORE: {seo_score} / 100")

    if(len(link) != 0):
        time.sleep(3)
        st.text("Here is the SEO details of your video ⬇️")
        st.write("\n")
        st.write("\n")
        response = seoChecker(youtube)
        print(response)


#############################   Tool Number 2   ##################################


if selected == "Video Engagement Checker":
    st.title("Engagement Calculator For Tracking A Video's Performance 🔥")
    st.write("\n")
    st.text("➡️ No more tricky questions about how a YouTube video is performing. TubeStack Engagement Calculator is a practical tool to see how much your audience is")
    st.text("    engaged with a certain video. No sign up is required!")

    link = \
        st.text_input('YOUTUBE VIDEO LINK   (eg -> https://www.youtube.com/watch?******************* )'
                      )

    likesSuggest = ""
    commentsSuggest = ""

    def views_to_like_ratio(views, likes, likesSuggest):
        likes_score = 0
        ratio = (likes / views) * 100
        if ratio >= 5:
            likes_score += 48
            likesSuggest = "✔️ Your Video is Performing excellent on the basis of views to likes ratio!"
        elif ratio >= 4.6:
            likes_score += 43
            likesSuggest = "✔️ Your Video is Performing great on the basis of views to likes ratio!"
        elif ratio >= 4.1:
            likes_score += 39
            likesSuggest = "✔️ Your Video is Performing good on the basis of views to likes ratio!"
        elif ratio >= 3.7:
            likes_score += 33
            likesSuggest = "❎ On the basis of views to likes ratio, your Video is Performing just OK, can get better!"
        elif ratio >= 2.9:
            likes_score += 27
            likesSuggest = "❌ On the basis of views to likes ratio, your Video is Performing bad!"
        else:
            likes_score += 19
            likesSuggest = "❌ On the basis of views to likes ratio, your Video is Performing poor!"

        return likes_score, likesSuggest

    def views_to_comments_ratio(views, comments, commentsSuggest):
        comments_score = 0
        ratio = (comments / views) * 100
        if ratio >= 0.6:
            comments_score += 48
            commentsSuggest = "✔️ Your Video is Performing excellent on the basis of views to comment ratio!"
        elif ratio >= 0.55:
            comments_score += 43
            commentsSuggest = "✔️ Your Video is Performing great on the basis of views to comment ratio!"
        elif ratio >= 0.5:
            comments_score += 39
            commentsSuggest = "✔️ Your Video is Performing good on the basis of views to comment ratio!"
        elif ratio >= 0.45:
            comments_score += 33
            commentsSuggest = "❎ On the basis of views to comments ratio, your Video is Performing just OK, can get better!"
        elif ratio >= 0.4:
            comments_score += 27
            commentsSuggest = "❌ On the basis of views to comments ratio, your Video is Performing bad!"
        else:
            comments_score += 19
            commentsSuggest = "❌ On the basis of views to comments ratio, your Video is Performing poor!"

        return comments_score, commentsSuggest

    def engagementChecker(youtube):
        parsed = link.split("v=")
        Id = parsed[1]
        request = youtube.videos().list(part="snippet,contentDetails,statistics", id=Id)
        response = request.execute()

        title = response['items'][0]['snippet']['title']
        thumb = response['items'][0]['snippet']['thumbnails']['default']['url']
        views = int(response['items'][0]['statistics']['viewCount'])
        likes = int(response['items'][0]['statistics']['viewCount'])
        comments = int(response['items'][0]['statistics']['commentCount'])

        l_score, l_suggest = views_to_like_ratio(views, likes, likesSuggest)
        c_score, c_suggest = views_to_comments_ratio(
            views, comments, commentsSuggest)
        engagement_score = l_score + c_score

        st.title(f"Video Engagement score: {engagement_score} / 100")
        st.subheader(l_suggest)
        st.subheader(c_suggest)

    if(len(link) != 0):
        time.sleep(3)
        st.text("Here is the engagement score of your video ⬇️")
        st.write("\n")
        st.write("\n")
        response = engagementChecker(youtube)
        print(response)



if selected == "Video Best Practices":
    st.title("Best Practices For Video Optimization 🔥")
    st.write("\n")
    st.text("➡️ You want your video to be optimized, NO ISSUE we got solution for all of your problem in just one click!")
    st.text("TubeStack provides best practices video feature which detects missing or recommended part on your video")
    st.text("So you can get to know about the weaknesses of your video and able to improve it!")
    
    link = \
    st.text_input('YOUTUBE VIDEO LINK   (eg -> https://www.youtube.com/watch?******************* )'
                    )
    
    def bestPractices(youtube):
        parsed = link.split("v=")
        Id = parsed[1]
        request = youtube.videos().list(part="snippet,contentDetails,statistics", id=Id)
        response = request.execute()


        chapters = ["0:00","(0:00)", "00:00","(00:00)","0:00:00","(0:00:00)", "00:00:00", "(00:00:00)"]
        chapters_set = set(chapters)
        description = response['items'][0]['snippet']['description']
        try:
            thumbnail = response['items'][0]['snippet']['thumbnails']['maxres']['url']
            st.subheader("✔️ High Resolution Thumbnail is added in this video")
        except:
            st.subheader("❌ High Resolution Thumbnail is not added in this video")
            
        description = str(description)
        description = description.lower()
        descList = list(description.split(" "))
        desc_set = set(descList)
        if (desc_set & chapters_set):
            st.subheader("✔️ Chapters are added in this video")
        else:
            st.subheader("❌ Chapters are not added in this video")
            
        
        captions = response['items'][0]['contentDetails']['caption']
        if captions == 'true':
            st.subheader("✔️ Video Captions are added in this video")
        else:
            st.subheader("❌ Video Captions are not added in this video")
        

    if(len(link) != 0):
        time.sleep(3)
        st.text("Here are the best practices for your video ⬇️")
        st.write("\n")
        st.write("\n")
        response = bestPractices(youtube)
        print(response)
