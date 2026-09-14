# 🍔 Campus Food Finder

A Python + Streamlit application that recommends campus dining options based on user preferences.

## Features

- Budget filtering
- Food-type filtering
- Vegetarian/vegan filtering
- Walking-distance filtering
- Minimum rating
- Open-now filtering
- Weighted recommendation algorithm
- Ranked match scores
- Simple interactive UI

## Project Structure

```text
campus_food_finder/
├── app.py
├── restaurants.py
├── recommender.py
├── requirements.txt
└── README.md
```

## Run the App

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start Streamlit:

```bash
streamlit run app.py
```

5. Open the local address Streamlit gives you, usually:

```text
http://localhost:8501
```

## Customize It

Open `restaurants.py` and replace the example restaurants with real campus dining locations.

Each restaurant needs:

- name
- type
- price
- price_label
- distance
- rating
- vegetarian
- vegan
- open
- description

## Recommendation Algorithm

The current algorithm uses:

- 30% price
- 25% distance
- 20% food-type preference
- 15% rating
- 10% availability

The project can later be expanded with a database, live hours, maps, user accounts, favorites, and personalized recommendations.
