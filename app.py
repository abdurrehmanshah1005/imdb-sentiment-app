import gradio as gr
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="abdurrehmanshah/imdb-sentiment-distilbert"
)

def predict_sentiment(text):
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    if label == "LABEL_1":
        sentiment = "😊 Positive"
    else:
        sentiment = "😞 Negative"

    return f"{sentiment}\nConfidence: {score:.2%}"


demo = gr.Interface(
    fn=predict_sentiment,

    inputs=gr.Textbox(
        lines=5,
        placeholder="Enter a movie review..."
    ),

    outputs=gr.Textbox(label="Prediction"),

    title="IMDb Movie Review Sentiment Analyzer",

    description="""
Enter a movie review and the AI will predict whether it is positive or negative.
""",

    examples=[
        ["This movie was absolutely amazing!"],
        ["Worst movie ever."],
        ["The acting was good but the story was boring."]
    ],

    submit_btn="Analyze Review"
)

demo.launch()

