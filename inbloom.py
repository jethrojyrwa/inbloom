import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from PIL import Image
import os 

import nltk
nltk.download('punkt')
nltk.download('stopwords')


def preprocess_text(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Load Data (Replace with your actual file path)
data = pd.read_csv('event_feedback_dataset.csv')
data_filtered = data.copy()

st.title("INBLOOM '25")

# Event-wise Participation
st.header('Event-wise Participation')
events = st.multiselect('Select Event', options=data['Event_Name'].unique())
if events:
    data_filtered = data_filtered[data_filtered['Event_Name'].isin(events)]
st.bar_chart(data_filtered.groupby('Event_Name')['Participant_ID'].count())

# Day-wise Participation
st.header('Day-wise Participation')
st.line_chart(data_filtered.groupby('Event_Date')['Participant_ID'].count())

# College-wise Participation
st.header('College-wise Participation')
colleges = st.multiselect('Select Colleges', options=data['College'].unique())
if colleges:
    data_filtered = data_filtered[data_filtered['College'].isin(colleges)]
college_wise_data = data_filtered.groupby(['Event_Date', 'College'])['Participant_ID'].count().unstack(fill_value=0)
st.area_chart(college_wise_data)

# State-wise Participation (Line Chart)
st.header('State-wise Participation')
states = st.multiselect('Select States', options=data['State'].unique())
if states:
    data_filtered = data_filtered[data_filtered['State'].isin(states)]
state_counts = data_filtered.groupby('State')['Participant_ID'].count()
st.line_chart(state_counts)

# Overall Participation Comparison (Bar Chart)
st.header('Overall Participation Comparison')
overall_comparison = data_filtered.groupby(['Event_Name', 'College'])['Participant_ID'].count().unstack(fill_value=0).sum(axis=1)
st.bar_chart(overall_comparison)


#TEXT ANALYSIS
#Word CLoud

st.header("Word Cloud of Feedback from Participants")
all_feedback = " ".join(data['Feedback_Text'].astype(str))

tokens = preprocess_text(all_feedback)

words = "" 
words += " ".join(tokens) + " "
wordcloud = WordCloud(width = 800, height = 800,
                      background_color="white",
                      stopwords=STOPWORDS, 
                      min_font_size=10).generate(words)

fig = plt.figure(figsize=(3,3), facecolor="white",edgecolor="blue")
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)
st.pyplot(fig)

## Word Cloud Comparison for Feedback within Each Event
st.header("Word Cloud Comparison of Feedback within Each Event")
event_names = data['Event_Name'].unique()

fig, axes = plt.subplots(2, 5, figsize=(20, 15))
fig.suptitle('Word Cloud Comparison for Different Events', fontsize=20)

for i, event in enumerate(event_names):
    row, col = divmod(i, 5)
    event_feedback = " ".join(data[data['Event_Name'] == event]['Feedback_Text'].astype(str))
    tokens = preprocess_text(event_feedback)
    words = " ".join(tokens)
    wordcloud = WordCloud(width=800, height=800, background_color="white", stopwords=STOPWORDS, min_font_size=10).generate(words)
    
    axes[row, col].imshow(wordcloud)
    axes[row, col].axis('off')
    axes[row, col].set_title(event)

plt.tight_layout()
st.pyplot(fig)



# Image Processing Module
st.header("Day-wise Image Gallery")

image_paths = [
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image1.jpg',
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image2.jpg',
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image3.jpg',
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image4.jpg',
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image5.jpg',
    'D:\\MCA\\3rd Trimester\\Advanced Python Programming\\2447122_ETE3\\image6.jpg'
]

image_captions = [
    'Day 1',
    'Day 2',
    'Day 3',
    'Day 4',
    'Day 5',
    'Extras'
]

i=0
for path in image_paths:
    if os.path.exists(path):
        
        img = Image.open(path)
        st.image(img, caption=image_captions[i], use_container_width=True)
        i = i + 1


st.header("Custom Image Processing")
selected_path = st.selectbox("Select an Image to Process", image_paths)

if os.path.exists(selected_path):
    img = Image.open(selected_path)
    st.image(img, caption='Original Image', use_container_width=True)

    # Example of a simple image processing operation
    grayscale_img = img.convert('L')
    st.image(grayscale_img, caption='Grayscale Image', use_container_width=True)



