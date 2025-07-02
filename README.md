# Cyber AI Enhanced Intrusion Detection System

![Banner](https://img.shields.io/badge/Cyber%20AI%20IDS-Powered%20by%20ML-brightgreen?style=for-the-badge)

![Banner](https://github.com/MilakeSuraj/Tic_Tac_Toe_Game/blob/main/Beige%20Modern%20Elegant%20Personal%20LinkedIn%20Banner%20(1).png?raw=true)



# Project Overview

***A full-stack web application for detecting web attacks using AI/ML, featuring a modern cyber-themed UI and real-time prediction.***


   
## Video

![Demo Video 1](https://raw.githubusercontent.com/MilakeSuraj/Cyber-Security-AI-Enhanced-Intrusion-Detection-System/main/Screenshots/mainpage.gif)



## Prediction Screen

![Prediction Demo](https://raw.githubusercontent.com/MilakeSuraj/Cyber-Security-AI-Enhanced-Intrusion-Detection-System/main/Screenshots/prediction.gif)


## Features

- **AI-Powered Detection:** Uses a trained Random Forest model for web attack prediction.
- **User-Friendly Web Interface:** Enter network flow features and get instant predictions.
- **Loader & Animated UI:** Modern cyberpunk design with animated loader and modal results.
- **Input Validation:** Ensures all required features are provided and valid.
- **Prediction Modal:** Displays prediction and input summary in a stylish popup.





---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript (Vanilla), Jinja2 (Flask templating)
- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn, imbalanced-learn, joblib
- **Model:** Random Forest Classifier (trained on 4 selected features)
- **Other:** Bootstrap (optional), Pandas, NumPy



## Project Structure

```
CYBER_PROJECT/
│
├── app.py                        # Flask backend
├── random_forest_model_4_features.joblib  # Trained ML model
├── web_attacks_balanced.csv      # Dataset (for reference/training)
├── Untitled.ipynb                # Model training notebook
├── static/
│   └── assets/
│       └── i-am-free-anonymous.960x540.mp4  # Background video
└── templates/
    └── index.html                # Main web UI
```

---






*For more details, see the code in [`CYBER_PROJECT`](./CYBER_PROJECT)*
