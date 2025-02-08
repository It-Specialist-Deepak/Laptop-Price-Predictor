# 💻 Laptop Price Predictor  

A machine learning-based **Laptop Price Prediction** web application built using **Python, Streamlit, and Scikit-Learn**.  
It helps users estimate the price of a laptop based on its specifications such as **brand, RAM, storage, GPU, CPU, touchscreen, etc.**  

---

## 🚀 Features  
✔️ **Predicts laptop prices** based on user input  
✔️ Uses **Scikit-learn** for model training and prediction  
✔️ **Data visualization** using Seaborn & Matplotlib  
✔️ **Interactive frontend** built with Streamlit  
✔️ Simple and easy-to-use interface  

---

## 🛠️ Technologies Used  
| Technology  | Purpose |
|------------|---------|
| **Python** | Programming Language |
| **Pandas** | Data Manipulation |
| **Seaborn & Matplotlib** | Data Visualization |
| **Scikit-learn (sklearn)** | Machine Learning |
| **Streamlit** | Web App Framework |

---

## 📊 Data & Model Training  
- The dataset used for this project contains various **laptop specifications and prices**.  
- The data was **cleaned and preprocessed** using Pandas.  
- The model was trained using **Scikit-learn's pipeline with OneHotEncoding & Linear Regression**.  
- **Visualizations** were created using **Matplotlib & Seaborn** to analyze trends in laptop pricing.  
- The trained model (`pipe.pkl`) is loaded in **Streamlit** for real-time predictions.

---

## ▶️ How to Run the Project  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/It-Specialist-Deepak/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
```

### 2️⃣ **Run Command **
```sh
python -m streamlit run app.py
