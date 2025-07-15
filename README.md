# 📊 Sentiment Analysis Web App

A simple and interactive **Streamlit** web application for performing **sentiment analysis** on text data using **TextBlob**. Users can either upload a CSV file with textual data for bulk analysis or manually enter text to get instant sentiment feedback. The app also features Lottie animations and sentiment distribution visualization using Plotly.

---

## 🚀 Features

* Upload CSV files and analyze sentiment of a selected text column
* Display sentiment results directly in a new column (customizable name)
* Visualize sentiment distribution using a pie chart
* Perform manual sentiment analysis on custom input text
* Interactive UI with Lottie animations for better user experience
* Built-in error handling and clean text preprocessing

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **TextBlob**
* **CleanText**
* **Plotly**
* **Lottie (via `streamlit-lottie`)**

---

## 📂 File Upload Instructions

1. Upload a `.csv` file with at least one column containing text.
2. Select the column you want to analyze.
3. Choose a name for the result column (existing columns will be overwritten).
4. The app will:

   * Clean the text,
   * Analyze sentiment,
   * Display results and sentiment distribution.

---

## 📝 Manual Sentiment Analysis

1. Scroll down to the "Manual Sentiment Analysis" section.
2. Enter any text in the text box.
3. Click **Analyze** to see the sentiment (Positive 😊, Neutral 😐, Negative 😔).

---

## 📌 How to Run

Make sure you have Python installed, then install the dependencies and run the app:

```bash
pip install streamlit pandas textblob clean-text streamlit-lottie plotly
python -m textblob.download_corpora
streamlit run app.py
```

> Replace `app.py` with the actual filename if different.

---

## 📁 Folder Structure

```
.
├── app.py
├── animations/
│   ├── girl statistic analysis.json
│   └── 3 smiley faces.json
└── sample.csv (optional for testing)
```

---

## ✅ Example Use Cases

* Customer review sentiment classification
* Survey response analysis
* Social media comment analysis
* Educational sentiment-based projects

---

## 📌 Notes

* Ensure your CSV file has no missing values in the selected column.
* Only textual data is supported for sentiment analysis.
* Lottie animations require the `.json` files in the `animations/` directory.
