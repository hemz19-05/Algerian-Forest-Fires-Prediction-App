### Algerian Forest Fire Prediction (ML + Flask + AWS Deployment)

This project predicts the Fire Weather Index (FWI) for Algerian forest fire regions using a Machine Learning model.
The primary objective of this project was to practice:

🌐 Building and deploying a full end-to-end ML application

⚙️ Developing REST APIs using Flask

☁️ Deploying production-ready apps on AWS Elastic Beanstalk

🧩 Understanding real-world MLOps deployment workflows

This project is based on the ML deployment course by Krish Naik, and I extended it with my own deployment + pipeline setup.

🚀 Demo

Live App on AWS Elastic Beanstalk:

👉 http://algerianforestfiresprediction-env.eba-wvnihueh.ap-southeast-2.elasticbeanstalk.com/predictdata

🔍 Problem Overview

Forest fires are a major environmental and safety issue in Algeria.
This application predicts the FWI using several meteorological features:

1. Temperature
2. Relative Humidity
3. Wind Speed
4. Rain
5. FFMC
6. DMC
7. ISI
8. Region + Classes

🧠 Model Used

Ridge Regression (Scikit-Learn)

Features scaled using StandardScaler

Model artifacts saved as:

model/ridg.pkl  
model/scaler.pkl

🧰 Tech Stack
ML & Backend

Python

Flask (REST APIs)

Scikit-learn

Pandas, NumPy

Deployment & DevOps

AWS Elastic Beanstalk

EC2

Gunicorn

.ebextensions config

Linux virtual server environment

⚙️ Application Architecture
app/
│
├── application.py         # Flask API
├── wsgi.py                # Entry point for Gunicorn
├── model/                 # ML artifacts
├── templates/             # HTML interface
├── requirements.txt
├── Procfile               # Gunicorn entry
└── .ebextensions/         # AWS config

🖥️ How It Works

You enter the inputs:

Temperature, Rain, RH, Wind, FFMC, DMC, ISI, etc.


The app:

Validates form input

Passes it into the model

Predicts the Fire Weather Index (FWI)

Returns the result to the UI

☁️ Deployment Workflow

🔥 Full deployment done on AWS:

Packaged app into deployment zip

Added Procfile + Gunicorn

Created EB environment

Configured WSGI using .ebextensions/python.config

Deployed successfully on AWS

Key AWS Concepts Covered

✔ Elastic Beanstalk deployment
✔ E2C running Python 3.14
✔ WSGI server + Gunicorn
✔ Directory and WSGI routing
✔ Environment updates & logs troubleshooting

📝 REST API Endpoint
POST /predictdata


Request type: form data
Response: predicted FWI

🧪 Local Setup
pip install -r requirements.txt
python application.py


Then visit:

http://127.0.0.1:5000/

🛠 Future Improvements

Add UI styling (Bootstrap)

Add Docker + CI/CD

Use AWS RDS for logging predictions

Build API versioning + JWT auth

📌 Motivation

This wasn’t just about building an ML model —
It was specifically to learn real-world deployment for ML apps, which is often the hardest part.

This helped me practice:

Full-stack ML pipeline

Deployment on cloud infrastructure

Working with production server configurations

😊 Acknowledgements

Inspired by Krish Naik’s deployment course.
