import streamlit as st
import pandas as pd
from textblob import TextBlob
import cleantext

def analyze_sentiment(text: str):
  text = cleantext.clean(text=text, clean_all=True)
  analysis = TextBlob(text) # can add classifier by loading one from another file.
  sentiment_polarity = analysis.sentiment.polarity

  if sentiment_polarity > 0:
    return "Positive 😊"
  elif sentiment_polarity < 0:
    return "Negative 😔"
  else:
    return "Neutral 😐"

st.title("Sentiment Analysis App")

# the help parameter can be used to add different instructions for each element, it appears as a help tooltip above the element.
uploaded_file = st.file_uploader(label="Upload a CSV file", type=["csv"])

try:
  if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Removing all NA values from all columns.
    df.dropna(inplace=True)
    resultant_column = st.text_input(label="Enter column name to display result", value="Sentiment", help="Providing an existing column name would overwrite the existing")
    content_column = st.selectbox(label="Select a column to analyse", options=df.columns, index=None)
    try:
      df[resultant_column] = df[content_column].apply(analyze_sentiment)
    except pd.errors.ParserError as e:
      st.error("There was an issue parsing the file. Please check the file format.")
    except pd.errors.EmptyDataError as e:
      st.error("The file is empty. Please upload a non-empty CSV file.")
    except KeyError as e:
      # st.error("The selected column does not exist in the CSV file.")
      st.info("Please select a column.") # by default, there will be no column selected and the user would get confused. 
    except TypeError as e:
      print(e.with_traceback)
      st.error("The selected column contains non-textual data. Please choose a different column.")
    except Exception as e:
      st.write(f"An exception ocurred while processing the file: {e}")
    st.subheader("Result")
    st.write(df)

    if "Sentiment" in df.columns:
      sentiment_counts = df["Sentiment"].value_counts()
      st.subheader("Sentiment Distribution")
      st.bar_chart(sentiment_counts)

  st.subheader("Manual Sentiment Analysis")
  user_input = st.text_area("Enter text: ")
  if st.button("Analyze"):
    try:
      if user_input:
        result = analyze_sentiment(user_input)
        st.write(f"Sentiment: {result}")
      else:
        st.error("Please enter text for analysis")
    except Exception as e:
      print(f"An error ocurred during manual sentiment analysis: {e}")
except Exception as e:
  st.error(f"An expected error ocurred: {e}")

# Either we can add meaningful information here or remove the sidebar.
st.sidebar.subheader("About")
st.sidebar.text("This app performs sentiment analyses on textual data.")