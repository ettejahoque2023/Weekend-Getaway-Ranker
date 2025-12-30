import pandas as pd

# Load Kaggle dataset
df = pd.read_csv("travel_data.csv")

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

def recommend_weekend_places(city, top_n=5):
    # Filter by city
    city_df = df[df["city"].str.lower() == city.lower()].copy()

    if city_df.empty:
        return f"❌ No places found for city: {city}"

    # --- SCORING LOGIC ---

    # Rating score
    city_df["rating_score"] = (
        city_df["google_review_rating"] /
        city_df["google_review_rating"].max()
    )

    # Popularity score (number of reviews)
    city_df["popularity_score"] = (
        city_df["number_of_google_review_in_lakhs"] /
        city_df["number_of_google_review_in_lakhs"].max()
    )

    # Time suitability (ideal weekend visit ≤ 3 hours)
    city_df["time_score"] = city_df["time_needed_to_visit_in_hrs"].apply(
        lambda x: 1 if x <= 3 else 0.6
    )

    # Budget friendliness (lower entry fee = better)
    max_fee = city_df["entrance_fee_in_inr"].max()
    city_df["budget_score"] = 1 - (
        city_df["entrance_fee_in_inr"] / max_fee if max_fee > 0 else 0
    )

    # Final weighted score
    city_df["final_score"] = (
        0.40 * city_df["rating_score"]
        + 0.30 * city_df["popularity_score"]
        + 0.20 * city_df["time_score"]
        + 0.10 * city_df["budget_score"]
    )

    # Rank places
    ranked = city_df.sort_values(by="final_score", ascending=False)

    return ranked[
        [
            "name",
            "type",
            "google_review_rating",
            "number_of_google_review_in_lakhs",
            "time_needed_to_visit_in_hrs",
            "entrance_fee_in_inr",
            "final_score",
        ]
    ].head(top_n)


# ------------------ USER INPUT ------------------
if __name__ == "__main__":
    user_city = input("Enter city you want to travel to: ")
    print(f"\nTop Weekend Places to Visit in {user_city}")
    print(recommend_weekend_places(user_city))
