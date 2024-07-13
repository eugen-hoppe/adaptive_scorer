from typing import Dict, Tuple

from .interface import AdaptiveScorerInterface


class AdaptiveScorer(AdaptiveScorerInterface):
    def create_complete_dict(
        self, property_catalog: Dict[str, str], entity_dict: Dict[str, float]
    ) -> Dict[str, float]:
        complete_dict = {property_id: 0.0 for property_id in property_catalog}
        complete_dict.update(entity_dict)
        return complete_dict

    def compute_score(
        self,
        entity_dict_1: Dict[str, float],
        entity_dict_2: Dict[str, float],
        lower_bound: float = 0.0,
        upper_bound: float = 1.0,
    ) -> float:
        total_score = 0.0
        property_count = len(entity_dict_1)

        for property_id in entity_dict_1:
            weight_1 = entity_dict_1[property_id]
            weight_2 = entity_dict_2[property_id]

            adjusted_weight_1 = lower_bound + (weight_1 * (upper_bound - lower_bound))
            adjusted_weight_2 = lower_bound + (weight_2 * (upper_bound - lower_bound))

            score_contribution = 1 - abs(adjusted_weight_1 - adjusted_weight_2) / (
                upper_bound - lower_bound
            )
            total_score += score_contribution

        average_score = total_score / property_count
        return average_score * 100

    def compute_resource_usage(
        self,
        property_id: str,
        weight: float,
        learning_parameters: Dict[str, Tuple[float, float]],
        is_demand: bool,
        current_resources: float,
        scale_factor: float = 1.0,
    ) -> Tuple[float, float]:
        learning_param = learning_parameters.get(property_id, (1.0, 1.0))[
            1 if is_demand else 0
        ]

        adjusted_weight = weight * scale_factor

        cost = adjusted_weight / learning_param

        if cost > current_resources:
            raise ValueError("Insufficient resources for this weight.")

        new_resources = current_resources - cost
        return new_resources, cost
