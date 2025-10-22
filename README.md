# 🧠 Image Classification Web App (CNN & Fine-Tuned Xception)

This project is a **binary image classification** web application built using **TensorFlow/Keras** and deployed through **Streamlit**.  
It classifies images into two categories (e.g., cats vs dogs or similar) using both a **custom CNN architecture** and a **fine-tuned Xception model**.  
The app provides an interactive interface to upload an image and view the classification result instantly.

---
# 🎥 Demo

A short introductory video is included at the beginning of the Streamlit interface, explaining how the application works.

https://github.com/HMGUNASEKARA/Cat-and-Dog-Identifier-Using-CNN-and-Streamlit/issues/1#issue-3539740011

---
## 🧩 Model Development

### 1. **Baseline CNN Model**

- **Framework:** TensorFlow + Keras Sequential API  
- **Reason:** Simple linear model architecture for initial experimentation  
- **Architecture Summary:**
  - Data Augmentation Layer  
  - 3 × Convolutional Layers  
    - Filters: 64 → 128 → 256  
    - Kernel Size: (3 × 3)  
    - Activation: ReLU  
  - 3 × MaxPooling Layers  
  - Dropout Layers (rate = 0.25)  
  - Batch Normalization Layers  
  - 3 × Dense Layers (128 units, ReLU)  
  - Final Dense Layer (1 unit, Sigmoid)  

- **Compilation:**
  
  optimizer = 'adam'
  loss = 'binary_crossentropy'
  metrics = ['accuracy']

  ### 🧠 Model Training and Evaluation

#### **Training (Baseline CNN Model)**

- **Epochs:** 20  
- **Evaluation Metrics:** Precision, Recall, and Accuracy  

**Performance Results:**
- Precision: **0.74**  
- Recall: **0.81**  
- Accuracy: **0.77**  

---

### ⚙️ Fine-Tuned Model (Xception)

To enhance performance, **Transfer Learning** was applied using **Google’s pre-trained Xception model** (trained on ImageNet).

**Changes Made:**
- Removed top layer of Xception (originally built for multi-class classification)  
- Input image size: **(128 × 128)**  
- Added custom dense layers:

  Dense(128, activation='relu')
  Dense(128, activation='relu')
  Dense(64, activation='relu')
  Dropout(0.2)
  Dense(1, activation='sigmoid')


### ⚙️ Fine-Tuned Model (Xception)

To enhance performance, **Transfer Learning** was applied using **Google’s pre-trained Xception model** (trained on ImageNet).

**Changes Made:**
- Removed top layer of Xception (originally built for multi-class classification)  
- Input image size: **(128 × 128)**  
- Added custom dense layers:

  Dense(128, activation='relu')
  Dense(128, activation='relu')
  Dense(64, activation='relu')
  Dropout(0.2)
  Dense(1, activation='sigmoid')

### ⚙️ Model Optimization

Used the **same optimizer**, **loss function**, and **metrics** as the baseline model.

---

### 🏋️ Training Details

- **Epochs:** 3 (initially faced overfitting)  
- **Regularization:** Added **Dropout (0.2)** → Improved results significantly  

**Final Performance:**  
- **Accuracy:** ≈ **0.89**

---

### 🖥️ Streamlit Web Application

A simple **Streamlit interface** was developed for easy model interaction and prediction.

#### Features
- 🎞 **Introductory video** explaining how Streamlit works  
- 🖼 **Image upload section** to classify pictures in real-time  
- 📊 **Instant classification results** with confidence levels  
- 📈 **Responsive and minimal user interface**



