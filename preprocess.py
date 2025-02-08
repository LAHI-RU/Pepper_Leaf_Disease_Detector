import os
import cv2
import numpy as np

IMAGE_SIZE = (224, 224)

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, IMAGE_SIZE)
    image = image / 255.0  # Normalize
    return image

def load_dataset(folder):
    images, labels = [], []
    for label, category in enumerate(["healthy", "diseased"]):
        folder_path = os.path.join(folder, category)
        for file in os.listdir(folder_path):
            img_path = os.path.join(folder_path, file)
            images.append(preprocess_image(img_path))
            labels.append(label)
    return np.array(images), np.array(labels)

# Example usage
X, y = load_dataset("dataset")
print("Dataset loaded:", X.shape, y.shape)
