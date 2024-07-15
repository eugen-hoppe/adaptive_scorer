from abc import ABC, abstractmethod
from typing import Dict, Tuple


class AdaptiveScorerInterface(ABC):
    @abstractmethod
    def create_complete_dict(
        self, property_catalog: Dict[str, str], entity_dict: Dict[str, float]
    ) -> Dict[str, float]:
        pass

    @abstractmethod
    def compute_score(
        self,
        entity_dict_1: Dict[str, float],
        entity_dict_2: Dict[str, float],
        lower_bound: float = 0.0,
        upper_bound: float = 1.0,
    ) -> float:
        pass

    @abstractmethod
    def compute_resource_allocation(
        self,
        property_id: str,
        usage_amount: float,
        allocation_parameters: Dict[str, Tuple[float, float]],
        is_demand: bool,
        available_resources: float,
        scale_factor: float = 1.0,
    ) -> Tuple[float, float]:
        pass
