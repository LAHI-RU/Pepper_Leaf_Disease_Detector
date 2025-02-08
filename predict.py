import tensorflow as tf
import numpy as np
import cv2

MODEL_PATH = "models/model.h5"
IMAGE_SIZE = (224, 224)
LABELS = ["Healthy", "Diseased"]

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, IMAGE_SIZE)
    image = np.expand_dims(image, axis=0) / 255.0  # Normalize

    prediction = model.predict(image)
    label = LABELS[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return label, confidence

# Example usage
image_path = "C:/Users/-A R R O W L I N E-/Desktop/one.jpg"  # Change to your test image path
label, confidence = predict_image(image_path)
print(f"Prediction: {label} ({confidence:.2f}%)")
