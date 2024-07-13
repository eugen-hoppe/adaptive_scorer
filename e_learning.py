from typing import Dict, Tuple

from src.adaptive_scorer import AdaptiveScorer


# E-Learning Platform Example
# ===========================


class ELearningPlatform(AdaptiveScorer):

    def __init__(self):
        self.lower_bound = 0.2
        self.upper_bound = 0.9
        self.scale_factor = 5.0

    def create_course_dict(
        self, property_catalog: Dict[str, str], course_dict: Dict[str, float]
    ) -> Dict[str, float]:
        return super().create_complete_dict(property_catalog, course_dict)

    def compute_course_score(
        self, course_dict_1: Dict[str, float], course_dict_2: Dict[str, float]
    ) -> float:
        return super().compute_score(
            course_dict_1,
            course_dict_2,
            self.lower_bound,
            self.upper_bound,
            self.scale_factor,
        )

    def compute_course_resource_usage(
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
course_property_catalog = {
    "topic_1": "Mathematics",
    "topic_2": "Physics",
    "topic_3": "Computer Science",
    "topic_4": "Literature",
}

course_dict_1 = {
    "topic_1": 0.6,
    "topic_3": 0.8,
}

course_dict_2 = {
    "topic_1": 0.7,
    "topic_2": 0.5,
    "topic_3": 0.6,
    "topic_4": 0.85,
}

elearning_platform = ELearningPlatform()

complete_course_dict_1 = elearning_platform.create_course_dict(
    course_property_catalog, course_dict_1
)
complete_course_dict_2 = elearning_platform.create_course_dict(
    course_property_catalog, course_dict_2
)
print("E-Learning Platform Complete Dicts:")
print(complete_course_dict_1)
print(complete_course_dict_2)

course_score = elearning_platform.compute_course_score(
    complete_course_dict_1, complete_course_dict_2
)
print(f"E-Learning Platform Score: {course_score:.2f}%")

learning_parameters = {"topic_1": (0.5, 0.7)}
current_resources = 50.0
weight = 0.6
property_id = "topic_1"
is_demand = True

try:
    new_resources, cost = elearning_platform.compute_course_resource_usage(
        property_id, weight, learning_parameters, is_demand, current_resources
    )
    print(
        f"E-Learning Platform - Remaining resources: {new_resources:.2f}, Assigned resource usage: {cost:.2f}"
    )
except ValueError as e:
    print(f"Error: {e}")
