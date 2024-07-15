# adaptive_scorer

**Adaptive Scorer (Version 1.0)**

AdaptiveScorer is a library for scoring and matching entities based on specified properties. It can be used in various applications, such as e-learning platforms, real estate platforms, and more. The library allows for the creation of complete property dictionaries, computation of matching scores, and calculation of resource usage.


## Installation
```bash
pip install git+https://github.com/eugen-hoppe/adaptive_scorer.git
```


## Methods

### `compute_resource_allocation`

The `compute_resource_allocation` method in the `AdaptiveScorer` class calculates the allocation of resources based on provided parameters and available resource capacity. This method can be used in various scenarios to manage the consumption or allocation of limited resources.

```python
def compute_resource_allocation(
    self,
    property_id: str,
    usage_amount: float,
    allocation_parameters: Dict[str, Tuple[float, float]],
    is_demand: bool,
    available_resources: float,
    scale_factor: float = 1.0,
) -> Tuple[float, float]:
```

#### Parameters

- **`property_id` (str)**: The ID of the resource or feature being allocated or consumed.
- **`usage_amount` (float)**: The amount of the resource or rating being used.
- **`allocation_parameters` (Dict[str, Tuple[float, float]])**: A dictionary containing parameters that affect the allocation. The values are tuples containing two factors: one for demand and one for supply.
- **`is_demand` (bool)**: A boolean indicating whether it is a demand (True) or a supply (False).
- **`available_resources` (float)**: The available amount of resources or capacity that can be allocated.
- **`scale_factor` (float)**: An optional scaling factor to adjust the resource usage amount. Default value is 1.0.

#### Return Value

- **Tuple[float, float]**: A tuple containing the remaining resources and the adjusted resource usage.

#### Functionality

**Determine the Allocation Factor**: The method reads the appropriate allocation factor (either for demand or supply) from the `allocation_parameters` dictionary based on the `property_id` and the value of `is_demand`.

**Adjust the Usage**: The `usage_amount` is multiplied by the `scale_factor` to calculate the adjusted usage.

**Calculate the Cost**: The adjusted usage is divided by the allocation factor to calculate the cost of the resource usage.

**Check Available Resources**: The method checks if the calculated cost exceeds the available resources. If so, it raises a `ValueError`.

**Calculate New Available Resources**: The method calculates the new available resources by subtracting the cost from the original available resources.

**Return**: The method returns a tuple containing the new available resources and the cost.

#### Example Code

Here is an example of using the `compute_resource_allocation` method:

```python
from src.adaptive_scorer import AdaptiveScorer

# Example parameters
allocation_parameters = {
    "price": (1.0, 0.8),
    "duration": (1.0, 0.7),
    "difficulty": (1.0, 0.6),
    "rating": (1.0, 0.9)
}

total_rating_capacity = 50.0
user_preference = {
    "price": 0.5,
    "duration": 0.6,
    "difficulty": 0.7,
    "rating": 0.8
}

scorer = AdaptiveScorer()

remaining_capacity = total_rating_capacity
adjusted_ratings = {}

for feature, preference in user_preference.items():
    try:
        remaining_capacity, adjusted_rating = scorer.compute_resource_allocation(
            property_id=feature,
            usage_amount=preference,
            allocation_parameters=allocation_parameters,
            is_demand=True,
            available_resources=remaining_capacity,
            scale_factor=10
        )
        adjusted_ratings[feature] = adjusted_rating
        print(f"{feature}: {adjusted_rating:.2f}, Remaining Capacity: {remaining_capacity:.2f}")
    except ValueError as e:
        print(f"Error in rating {feature}: {e}")
        break
```
