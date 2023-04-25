import streamlit as st
from transformers import pipeline

# Load the pre-trained model and tokenizer
classifier = pipeline("zero-shot-classification")

# Create a text input field and a list of candidate labels
text = st.text_input("Enter text to classify:")
labels = ["politics", "sports", "entertainment"]

# Generate the zero-shot classification scores for each label
scores = classifier(text, labels)["scores"]

# Display the results in a table
st.write("Label\tScore")
for i, label in enumerate(labels):
    st.write(f"{label}\t{scores[i]:.2f}")

