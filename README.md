# 🌿 Pepper Leaf Disease Detection

A deep learning-based system for detecting diseases in pepper leaves using image processing.

## 📌 Features
- Uses **CNN (Convolutional Neural Networks)** for disease detection.
- Supports **multiple types of pepper leaf diseases**.
- Provides a **web-based interface** using **Streamlit**.
- Achieves **high accuracy** (~95% training, ~90% validation).
- Open-source under the **MIT License**.

## 📥 Dataset & Model Download
The dataset and trained model are too large to be stored in this repository.

🔹 **Dataset:** [Download from Google Kaggle](https://www.kaggle.com/datasets/udi17live/black-pepper-leaf-blight-and-yellow-mottle-virus/data)  
🔹 **Pre-trained Model:** [Download from Google Drive](YOUR_MODEL_LINK)  

Once downloaded, place them in the respective folders:
```
/dataset/  (for images)
/models/   (for trained models)
```

---

## 🚀 Installation
### **1️⃣ Install Dependencies**
Run the following command to install all required dependencies:
```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Training the Model
To train the model on your dataset, run:
```bash
python train.py
```

---

## 📊 Testing the Model
To predict disease from a sample leaf image:
```bash
python predict.py --image sample_leaf.jpg
```

---

## 🎨 Web App Deployment
To run the Streamlit web application:
```bash
streamlit run app.py
```

---

## 🤖 Model Performance
- **Training Accuracy:** ~95%  
- **Validation Accuracy:** ~90%  
- **Optimizer:** Adam Optimizer  

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🌐 Links
- 🔗 **GitHub Repository:** [Your Repository Link](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME)
- 🎯 **Web App (if deployed):** [Live Demo](YOUR_DEPLOYMENT_LINK)

---

## 👨‍💻 Author
Developed by **W G Lahiru Dhananjaya Bandara** 🚀
