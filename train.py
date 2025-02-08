import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from preprocess import load_dataset

# Load dataset
X, y = load_dataset("dataset")
y = tf.keras.utils.to_categorical(y, 2)  # One-hot encoding

# Build CNN Model
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')  # 2 classes (Healthy/Diseased)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train Model
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

# Save Model
model.save("models/model.h5")
print("Model saved!")
