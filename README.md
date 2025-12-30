# 🧳 Weekend Getaway Ranker

A Python-based data engineering project that recommends the best weekend travel places within a city using a real Kaggle dataset of tourist attractions in India.  
The system ranks places based on ratings, popularity, visit duration, and budget friendliness.


## 📌 Problem Statement

When travelers visit a city for a short weekend, choosing the best places to visit can be difficult.  
This project solves the problem by analyzing tourism data and ranking places that are most suitable for a weekend trip.


## 🧠 Solution Overview

The recommendation engine uses a **multi-criteria weighted scoring algorithm** to rank tourist places.

### Ranking Factors:
- Google review rating
- Number of Google reviews (popularity)
- Time required to visit
- Entrance fee (budget friendliness)


## 🛠️ Technologies Used

- Python
- Pandas
- Kaggle Travel Dataset (India)


## 📁 Project Structure
<img width="306" height="203" alt="image" src="https://github.com/user-attachments/assets/82a3feb6-31c0-499b-9452-4ef5f7368e28" />



## ▶️ How to Run the Project
  ### 1️⃣ Install dependencies
pip install -r requirements.txt


  ## Run the program
python weekend_ranker.py

## Sample Input and OutPut
  ### 1️⃣ For Delhi
  #### Input-
  Enter city you want to travel to: Delhi
  #### OutPut
  <img width="672" height="221" alt="Screenshot 2025-12-30 213637" src="https://github.com/user-attachments/assets/f3fbc6bc-58e5-482b-a042-26d7a939920a" />

  
  ### 2️⃣For Kolkata
  #### Input-
  Enter city you want to travel to: kolkata
  #### Output-
  <img width="807" height="231" alt="Screenshot 2025-12-30 213230" src="https://github.com/user-attachments/assets/3efae3e2-64c9-4f62-9cf6-20db392d85aa" />

  
  ### 3️⃣For Bangalore
  #### Input-
  Enter city you want to travel to: Bangalore
  #### Output-
<img width="818" height="183" alt="Screenshot 2025-12-30 213602" src="https://github.com/user-attachments/assets/b8993d8d-eb11-4982-8b4a-ed5db33e3b6c" />

## ❌ City Not Found Handling

The system safely handles cases where the entered city is not present in the dataset.
Instead of crashing, it displays a clear message to the user.

  ### Input
  Enter city you want to travel to: Paris
  ### OutPut
  <img width="806" height="165" alt="image" src="https://github.com/user-attachments/assets/87a7badf-7839-4838-975c-f4cda04f1f83" />




