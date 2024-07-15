from src.adaptive_scorer import AdaptiveScorer


allocation_parameters = {
    "price": (1.0, 0.8),
    "location": (1.0, 0.7),
    "size": (1.0, 0.6),
    "rooms": (1.0, 0.5),
    "age": (1.0, 0.4)
}

total_rating_capacity = 20.0


user_preferences = {
    "price": 0.4,
    "location": 0.3,
    "size": 0.5,
    "rooms": 0.2,
    "age": 0.9
}

property_listings = {
    "Property A": {
        "price": 0.4,
        "location": 0.7,
        "size": 0.6,
        "rooms": 0.3,
        "age": 0.2
    },
    "Property B": {
        "price": 0.6,
        "location": 0.8,
        "size": 0.7,
    },
    "Property C": {
        "price": 0.2,
        "location": 0.6,
        "rooms": 0.6,
        "age": 0.9
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
            scale_factor=10
        )
        user_resource_usage[feature] = user_preferences[feature]
        print(f"{feature}: {adjusted_rating:.2f}, balance: {remaining_capacity:.2f}")
    except ValueError as e:
        print("Insufficient resources! Balance:", remaining_capacity)
        break

property_scores = {}


for property_name, features in property_listings.items():
    property_scores[property_name] = scorer.compute_score(
        scorer.create_complete_dict(allocation_parameters, user_resource_usage),
        scorer.create_complete_dict(allocation_parameters, features)
    )
    print(f" {property_name}: {property_scores[property_name]:.2f}%")


best_match_property = max(property_scores, key=property_scores.get)
print(best_match_property)
