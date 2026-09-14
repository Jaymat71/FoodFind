import streamlit as st
import pandas as pd
from recommender import recommend_food
from restaurants import RESTAURANTS

st.set_page_config(
    page_title="Campus Food Finder",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Campus Food Finder")
st.caption("Find the best campus food option based on your preferences.")

with st.sidebar:
    st.header("Your Preferences")

    budget = st.slider(
        "Maximum price",
        min_value=1,
        max_value=3,
        value=2,
        help="$ = under $10, $$ = $10-$15, $$$ = over $15"
    )

    food_types = ["Any"] + sorted({r["type"] for r in RESTAURANTS})
    food_type = st.selectbox("Food type", food_types)

    dietary = st.selectbox(
        "Dietary preference",
        ["Any", "Vegetarian", "Vegan"]
    )

    max_distance = st.slider(
        "Maximum walking time (minutes)",
        min_value=1,
        max_value=20,
        value=10
    )

    min_rating = st.slider(
        "Minimum rating",
        min_value=1.0,
        max_value=5.0,
        value=3.5,
        step=0.1
    )

    open_only = st.checkbox("Only show places that are open", value=True)

    find_button = st.button("🔎 Find Food", use_container_width=True)

if find_button:
    results = recommend_food(
        restaurants=RESTAURANTS,
        budget=budget,
        food_type=food_type,
        dietary=dietary,
        max_distance=max_distance,
        min_rating=min_rating,
        open_only=open_only
    )

    st.subheader("Best Matches")

    if not results:
        st.warning("No restaurants match all of your preferences. Try relaxing one or two filters.")
    else:
        for index, food in enumerate(results):
            with st.container(border=True):
                col1, col2, col3 = st.columns([2.5, 1, 1])

                with col1:
                    medal = ["🥇", "🥈", "🥉"][index] if index < 3 else "🍽️"
                    st.markdown(f"### {medal} {food['name']}")
                    st.write(f"**{food['type']}** • {food['description']}")

                with col2:
                    st.metric("Match", f"{food['score']:.0f}%")
                    st.write(f"⭐ {food['rating']}/5")

                with col3:
                    st.write(f"🚶 **{food['distance']} min**")
                    st.write(f"💰 **{food['price_label']}**")
                    st.write("🟢 Open" if food["open"] else "🔴 Closed")

                badges = []
                if food["vegetarian"]:
                    badges.append("🥗 Vegetarian")
                if food["vegan"]:
                    badges.append("🌱 Vegan")
                if badges:
                    st.caption(" • ".join(badges))

        best = results[0]
        st.success(
            f"Best match: **{best['name']}** with a {best['score']:.0f}% match score."
        )

else:
    st.info("Choose your preferences in the sidebar, then click **Find Food**.")

    st.subheader("How it works")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 1. Filter")
        st.write("Remove food options that don't meet your requirements.")
    with c2:
        st.markdown("### 2. Score")
        st.write("Calculate how well each remaining option matches you.")
    with c3:
        st.markdown("### 3. Rank")
        st.write("Sort the options from best match to worst match.")

    st.subheader("Campus Locations")
    preview = pd.DataFrame(RESTAURANTS)[
        ["name", "type", "price_label", "distance", "rating", "open"]
    ].rename(columns={
        "name": "Restaurant",
        "type": "Type",
        "price_label": "Price",
        "distance": "Walk (min)",
        "rating": "Rating",
        "open": "Open"
    })
    st.dataframe(preview, use_container_width=True, hide_index=True)
