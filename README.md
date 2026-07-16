# IMDb Sentiment Analysis using DistilBERT

A sentiment analysis web application built with **DistilBERT**, **Hugging Face Transformers**, and **Gradio**. This project fine-tunes a pretrained DistilBERT model on the IMDb movie review dataset to classify reviews as **Positive** or **Negative**.

## Features

* Fine-tuned DistilBERT model for sentiment analysis
* Interactive Gradio web interface
* Trained on the IMDb movie review dataset
* Deployed model hosted on Hugging Face
* Fast inference with confidence scores

## Demo

Model Repository:
https://huggingface.co/abdurrehmanshah/imdb-sentiment-distilbert

## Tech Stack

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Hugging Face Hub
* Gradio
* NumPy

## Project Structure

```
imdb-sentiment-app/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/abdurrehmanshah/imdb-sentiment-app.git
cd imdb-sentiment-app
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the local URL shown in the terminal (usually http://127.0.0.1:7860).

## Model

The application automatically downloads and loads the fine-tuned model from Hugging Face:

```
abdurrehmanshah/imdb-sentiment-distilbert
```

## Example Predictions

**Input**

```
This movie was absolutely amazing. The acting and story were fantastic!
```

**Prediction**

```
😊 Positive
Confidence: 99.5%
```

---

**Input**

```
This was one of the worst movies I have ever watched.
```

**Prediction**

```
😞 Negative
Confidence: 99.3%
```

## Training

The model was fine-tuned from:

* DistilBERT Base Uncased

Dataset:

* IMDb Movie Reviews

Framework:

* Hugging Face Trainer API

## Future Improvements

* Deploy the application on Hugging Face Spaces
* Add batch prediction support
* Display prediction probabilities with charts
* Support multiple languages
* Add model comparison with BERT and RoBERTa

## Author

**Abdur Rehman Shah**

GitHub: https://github.com/abdurrehmanshah1005

Hugging Face: https://huggingface.co/abdurrehmanshah
