import streamlit as st
import pandas as pd
from textblob import TextBlob
import cleantext
from streamlit_lottie import st_lottie
import json
import plotly.express as px
@st.cache_data

def load_lottiejson(path):
  with open(path, 'r') as json_file:
    return json.load(json_file)

col1, col2 = st.columns([1, 1])
with col1:
  st.title("Sentiment Analysis App")
  st.markdown(
  """
  <style>
    #sentiment-analysis-app {
      padding-top: 6rem;
    }
  </style>
  """, unsafe_allow_html=True)
with col2:
  girl_statistic_animation = load_lottiejson("./animations/girl statistic analysis.json")
  st_lottie(girl_statistic_animation, key="box-animation", width=300, height=300)

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
      fig = px.pie(sentiment_counts, names=sentiment_counts.index, values=sentiment_counts.values)
      st.plotly_chart(fig)

  st.markdown(
  """
  <hr style="height: 1rem;">
  """, unsafe_allow_html=True)

  smiley_faces_animation = load_lottiejson("./animations/3 smiley faces.json")
  col3, col4 = st.columns([1, 1])
  with col3:
    st.title("Manual Sentiment Analysis")
    st.markdown(
    """
    <style>
      #manual-sentiment-analysis {
        padding-top: 1rem;
      }
    </style>
    """, unsafe_allow_html=True)
  with col4:
    st_lottie(smiley_faces_animation, key="smiley-face", width=200, height=200)
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

st.sidebar.subheader("Project Guidelines")
st.sidebar.markdown("1. Upload a CSV file containing text data for sentiment analysis.")
st.sidebar.markdown("2. Select a column to analyze and specify a column for the result.")
st.sidebar.markdown("3. Click the 'Analyze' button to perform sentiment analysis on the selected text column.")
st.sidebar.markdown("4. View the result in the main section, including a pie chart of sentiment distribution.")
st.sidebar.markdown("5. You can also perform manual sentiment analysis by entering text in the text area.")
st.sidebar.markdown("6. Click 'Analyze' to analyze the manually entered text for sentiment")