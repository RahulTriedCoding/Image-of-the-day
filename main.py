import streamlit as st
import requests

api_key = "6iiy1Nk3y6bowZs973YgnwCZZeCzFpGJKSzqaWGP"

url = "https://api.nasa.gov/planetary/apod?"f"api_key={api_key}"

response = requests.get(url)
print(response)

# content = response.content
data = response.json()
print(type(data))
# print(content)
print(data)

# response2 = requests.get(data['url'])
# content = response2.content
# with open('img.png', 'wb') as file:
#     file.write(content)


cols = st.columns(1)
header = st.header(data['title'])
# image = st.image('img.png')
# st.write(data)
# print(content['url'])o


if data["media_type"] == "video":
    st.video(data['url'])
elif data["media_type"] == "image":
    st.image(data['url'])
else:
    st.write("The media type is not supported")

st.info(data['explanation'])



