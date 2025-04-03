🐶🐱 Cat vs Dog Classifier - Streamlit App

📌 Overview

This project is a simple and interactive web application built using Streamlit to classify images of cats and dogs using a deep learning model. It utilizes a fine-tuned ResNet18 model to provide accurate predictions.



🚀 Features

🖼️ Upload an image of a cat or dog for classification

🤖 Uses a fine-tuned ResNet18 model for image classification

📊 Displays prediction confidence scores

📈 Simple and interactive UI

📌 Installation

To run this Streamlit app locally, follow these steps:

Clone the repository

git clone https://github.com/your-username/cat-vs-dog-classifier.git
cd cat-vs-dog-classifier

Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies
```
pip install -r requirements.txt
```
Run the Streamlit app
```
streamlit run app.py --server.fileWatcherType=none
```

🛠️ Usage

Open your browser and go to: http://localhost:8501

Upload an image of a cat or dog.

The model will classify the image and display the result with confidence scores.

Try different images to test the classifier!

📂 Project Structure

.
├── app.py                # Main Streamlit app script
├── model/                # Directory containing the trained model
│   └──  model.pth         # Trained deep learning model
├── requirements.txt      # Python dependencies
└── README.md            # Documentation

⭐ Star this repo if you found it useful!

For any issues or feature requests, open an issue.

