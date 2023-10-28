import streamlit as st
import pandas as pd
from textblob import TextBlob
import cleantext

def analyze_sentiment(text):
  text = cleantext.clean(text=text, clean_all=True)
  analysis = TextBlob(text) # can add classifier by loading one from another file.
  sentiment_polarity = analysis.sentiment.polarity

  if sentiment_polarity > 0:
    return "Positive"
  elif sentiment_polarity < 0:
    return "Negative"
  else:
    return "Neutral"

st.title("Sentiment Analysis App")

uploaded_file = st.file_uploader(label="Upload a CSV file", type=["csv"])

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  # content_column = st.text_input(label="Enter column name to analyse", value="text")
  content_column = st.selectbox(label="Select a column to analyse", options=df.columns, index=None)
  try:
    df["Sentiment"] = df[content_column].apply(analyze_sentiment)
  except KeyError as e:
    print(e.with_traceback)
  except TypeError as e:
    print(e.with_traceback)
    st.write("Non-textual data in selected column")
  st.subheader("Result")
  st.write(df)

  if "Sentiment" in df.columns:
    sentiment_counts = df["Sentiment"].value_counts()
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