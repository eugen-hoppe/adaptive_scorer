from src.adaptive_scorer import AdaptiveScorer


allocation_parameters = {
    "price": (1.0, 0.7),
    "duration": (1.0, 0.6),
    "difficulty": (1.0, 0.9),
    "rating": (1.0, 0.9)
}

total_rating_capacity = 20.0

user_preferences = {
    "price": 0.9,
    "duration": 0.8,
    "difficulty": 0.8,
    "rating": 0.6,
}

course_listings = {
    "Course A": {
        "price": 1.0,
        "duration": 0.7,
        "difficulty": 0.6,
        "rating": 0.8,
    },
    "Course B": {
        "duration": 0.8,
        "difficulty": 0.5,
        "rating": 0.7,
    },
    "Course C": {
        "price": 1.0,
        "duration": 0.6,
    }
}

scorer = AdaptiveScorer()

user_resource_usage = {}
remaining_capacity = total_rating_capacity

for feature in user_preferences:
    try:
        remaining_capacity, adjusted_rating = scorer.compute_resource_allocation(
            property_id=feature,
            usage_amount=user_preferences[feature],
            allocation_parameters=allocation_parameters,
            is_demand=True,
            available_resources=remaining_capacity,
            scale_factor=5  # From 1 to 5 stars
        )
        user_resource_usage[feature] = user_preferences[feature]
        print(f"{feature}: {adjusted_rating:.2f}, balance: {remaining_capacity:.2f}")
    except ValueError as e:
        print("Insufficient resources! Balance:", remaining_capacity)
        break

course_scores = {}

for course_name, features in course_listings.items():
    course_scores[course_name] = scorer.compute_score(
        scorer.create_complete_dict(allocation_parameters, user_resource_usage),
        scorer.create_complete_dict(allocation_parameters, features)
    )
    print(f"{course_name}: {course_scores[course_name]:.2f}%")
