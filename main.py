import streamlit as st
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
  analysis = TextBlob(text)
  sentiment_polarity = analysis.sentiment.polarity

  if sentiment_polarity > 0:
    return "Positive"
  elif sentiment_polarity < 0:
    return "Negative"
  else:
    return "Neutral"

st.title("Sentiment Analysis App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  df['Sentiment'] = df['text'].apply(analyze_sentiment)
  st.subheader("Result")
  st.write(df)
  # st.dataframe(df)

  sentiment_counts = df['Sentiment'].value_counts()
  st.subheader("Sentiment Distribution")
  st.bar_chart(sentiment_counts)

st.subheader("Manual Sentiment Analysis")
user_input = st.text_area("Enter text: ")
if st.button("Analyze"):
  if user_input:
    result = analyze_sentiment(user_input)
    st.write(f"Sentiment: {result}")

st.sidebar.subheader("About")
st.sidebar.text("This app performs sentiment analyses on textual data.")