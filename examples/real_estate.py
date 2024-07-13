from typing import Dict, Tuple

from src.adaptive_scorer import AdaptiveScorer


# Real Estate Platform Example
# ============================


class RealEstatePlatform(AdaptiveScorer):
    def __init__(self):
        self.lower_bound = 0.05
        self.upper_bound = 0.95
        self.scale_factor = 50.0

    def create_real_estate_dict(
        self, property_catalog: Dict[str, str], real_estate_dict: Dict[str, float]
    ) -> Dict[str, float]:
        return super().create_complete_dict(property_catalog, real_estate_dict)

    def compute_real_estate_score(
        self, real_estate_dict_1: Dict[str, float], real_estate_dict_2: Dict[str, float]
    ) -> float:
        return super().compute_score(
            real_estate_dict_1,
            real_estate_dict_2,
            self.lower_bound,
            self.upper_bound,
        )

    def compute_real_estate_resource_usage(
        self,
        property_id: str,
        weight: float,
        learning_parameters: Dict[str, Tuple[float, float]],
        is_demand: bool,
        current_resources: float,
    ) -> Tuple[float, float]:
        return super().compute_resource_usage(
            property_id,
            weight,
            learning_parameters,
            is_demand,
            current_resources,
            self.scale_factor,
        )


# Example usage
real_estate_property_catalog = {
    "feature_1": "Location",
    "feature_2": "Size",
    "feature_3": "Price",
    "feature_4": "Condition",
}

real_estate_dict_1 = {
    "feature_1": 0.7,
    "feature_2": 0.8,
    "feature_3": 0.9,
}

real_estate_dict_2 = {
    "feature_1": 0.6,
    "feature_2": 0.9,
    "feature_3": 0.85,
    "feature_4": 0.7,
}

real_estate_platform = RealEstatePlatform()

complete_real_estate_dict_1 = real_estate_platform.create_real_estate_dict(
    real_estate_property_catalog, real_estate_dict_1
)
complete_real_estate_dict_2 = real_estate_platform.create_real_estate_dict(
    real_estate_property_catalog, real_estate_dict_2
)
print("Real Estate Platform Complete Dicts:")
print(complete_real_estate_dict_1)
print(complete_real_estate_dict_2)

real_estate_score = real_estate_platform.compute_real_estate_score(
    complete_real_estate_dict_1, complete_real_estate_dict_2
)
print(f"Real Estate Platform Score: {real_estate_score:.2f}%")


# Resource Usage
# ==============


learning_parameters = {"feature_1": (0.4, 0.7)}
current_resources = 100.0
weight = 0.8
property_id = "feature_1"
is_demand = True

try:
    new_resources, cost = real_estate_platform.compute_real_estate_resource_usage(
        property_id, weight, learning_parameters, is_demand, current_resources
    )
    print(
        f"Real Estate Platform - Remaining resources: {new_resources:.2f}, Assigned resource usage: {cost:.2f}"
    )
except ValueError as e:
    print(f"Error: {e}")
