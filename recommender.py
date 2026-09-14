def calculate_score(food, budget, max_distance):
    """
    Score a restaurant from 0-100.

    Weighting:
    Price       30%
    Distance    25%
    Food type   20%
    Rating      15%
    Open status 10%
    """

    # Price score: cheaper options score higher.
    price_score = max(0, (4 - food["price"]) / 3) * 30

    # Distance score: closer options score higher.
    distance_score = max(
        0, (max_distance - food["distance"]) / max_distance
    ) * 25

    # Rating score.
    rating_score = (food["rating"] / 5) * 15

    # Being open gets the full availability points.
    open_score = 10 if food["open"] else 0

    # Base score.
    score = price_score + distance_score + rating_score + open_score

    return score


def recommend_food(
    restaurants,
    budget,
    food_type,
    dietary,
    max_distance,
    min_rating,
    open_only
):
    """Filter restaurants and rank them by match score."""

    matches = []

    for food in restaurants:

        # Budget filter
        if food["price"] > budget:
            continue

        # Food type filter
        if food_type != "Any" and food["type"] != food_type:
            continue

        # Dietary filter
        if dietary == "Vegetarian" and not food["vegetarian"]:
            continue

        if dietary == "Vegan" and not food["vegan"]:
            continue

        # Distance filter
        if food["distance"] > max_distance:
            continue

        # Rating filter
        if food["rating"] < min_rating:
            continue

        # Open filter
        if open_only and not food["open"]:
            continue

        food_copy = food.copy()

        # Extra preference bonus for food type and dietary match.
        score = calculate_score(food_copy, budget, max_distance)

        if food_type != "Any":
            score += 20

        if dietary != "Any":
            score += 5

        # Cap score at 100.
        food_copy["score"] = min(score, 100)

        matches.append(food_copy)

    # Highest score first.
    matches.sort(key=lambda x: x["score"], reverse=True)

    return matches
