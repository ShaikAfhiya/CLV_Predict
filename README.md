📊 Customer Lifetime Value (CLV) Prediction
🚀 Project Overview

This project predicts Customer Lifetime Value (CLV) using Machine Learning.
It helps businesses estimate how valuable a customer will be over time based on their behavior, purchase patterns, and interaction data.

The application is built using:

FastAPI for backend
HTML (Jinja2 Templates) for frontend
Scikit-learn for model training
🎯 Features
Predict customer lifetime value instantly
User-friendly web interface
Handles multiple customer attributes
End-to-end ML pipeline (training → deployment)
🧠 Machine Learning Model

The model is trained using:

Customer demographics (Age, Gender, City)
Purchase behavior (Product Category, Quantity, Price)
Engagement metrics (Session Duration, Pages Viewed)
Customer feedback (Rating, Returning Customer)

Model file:

clv.pkl
📂 Project Structure
📁 project-folder
│
├── app.py              # FastAPI application
├── train.py           # Model training script
├── clv.pkl            # Trained ML model
├── templates/
│   └── index.html     # Frontend UI
├── requirements.txt   # Dependencies
└── README.md          # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/clv-prediction.git
cd clv-prediction
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Application
uvicorn app:app --reload

Open in browser:

http://127.0.0.1:8000
🧾 Input Features
Feature	Description
Age	Customer age
Gender	Male/Female
City	Customer location
Product_Category	Purchased product type
Unit_Price	Price per product
Quantity	Number of items
Discount_Amount	Discount applied
Payment_Method	Payment type
Device_Type	Device used
Session_Duration_Minutes	Time spent
Pages_Viewed	Number of pages visited
Is_Returning_Customer	True/False
Delivery_Time_Days	Delivery duration
Customer_Rating	Rating given
📸 Output
Displays predicted Customer Lifetime Value on the same page
