import streamlit as st
import torch
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
import torch.nn as nn

# Load trained model
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
model = models.resnet18(weights=None)  # Load ResNet18 model without pre-trained weights
model.fc = nn.Linear(in_features=512, out_features=2)
model.load_state_dict(torch.load(r"model\ResNet18_CatDog_224_Norm.pth", map_location=DEVICE))  # Load your trained model
model.to(DEVICE)
model.eval()

# Define class names
class_names = ["Cat", "Dog"]

# Define image transformations
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((224, 224))
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Streamlit UI
st.title("🐱 Cat or. Dog 🐶")
st.write("Upload an image to classify it as a **Cat or Dog**")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load and display image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image",  use_container_width=True)

    # Preprocess the image
    image = transform(image).unsqueeze(0).to(DEVICE)

    # Predict
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        label = class_names[predicted.item()]

    # Show result
    st.success(f"Prediction: **{label}** 🎯")