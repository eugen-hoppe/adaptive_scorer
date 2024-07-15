# adaptive_scorer

**Adaptive Scorer (Version 1.0)**

AdaptiveScorer is a library for scoring and matching entities based on specified properties. It can be used in various applications, such as e-learning platforms, real estate platforms, and more. The library allows for the creation of complete property dictionaries, computation of matching scores, and calculation of resource usage.


## Installation
```bash
pip install git+https://github.com/eugen-hoppe/adaptive_scorer.git
```


## Methods

### `create_complete_dict`

#### `create_complete_dict` Parameters

```python
def create_complete_dict(
    self, property_catalog: Dict[str, str], entity_dict: Dict[str, float]
) -> Dict[str, float]:
```

1. **`property_catalog: Dict[str, str]`**
   - **Description**: A dictionary containing the available properties that are used in the system. The key is the property identifier, and the value is a description or another indicator of the property.
   - **Example**: 
     ```python
     {
         "price": "Price of the course or property",
         "duration": "Duration of the course",
         "difficulty": "Difficulty level of the course",
         "rating": "User rating of the course"
     }
     ```

2. **`entity_dict: Dict[str, float]`**
   - **Description**: A dictionary containing the current values for the properties of the given entity (e.g., course or property). The key is the property identifier, and the value is the numerical value of the property.
   - **Example**: 
     ```python
     {
         "price": 1.0,
         "duration": 0.7,
         "difficulty": 0.6,
         "rating": 0.8
     }
     ```

#### Return Value

The function returns a dictionary (`Dict[str, float]`) that includes all properties from the `property_catalog` with the corresponding values from the `entity_dict`. If a property is not present in the `entity_dict`, it is assigned a default value of `0.0`.

**Example Return Value**:
```python
{
    "price": 1.0,
    "duration": 0.7,
    "difficulty": 0.6,
    "rating": 0.8
}
```

#### Functionality

The `create_complete_dict` function creates a complete dictionary for the given entity by ensuring that all properties from the `property_catalog` are present. It initializes all properties with a default value of `0.0` and then updates the values for the properties specified in the `entity_dict`.

#### Example

Suppose we have the following parameters:

```python
property_catalog = {
    "price": "Price of the course or property",
    "duration": "Duration of the course",
    "difficulty": "Difficulty level of the course",
    "rating": "User rating of the course"
}
entity_dict = {
    "price": 1.0,
    "duration": 0.7
}
```

The calculation might look like this:

```python
complete_dict = scorer.create_complete_dict(property_catalog, entity_dict)
```

The resulting `complete_dict` will include all properties from the `property_catalog`, with the values from the `entity_dict` and any missing properties initialized to `0.0`:

```python
{
    "price": 1.0,
    "duration": 0.7,
    "difficulty": 0.0,
    "rating": 0.0
}
```


### `compute_score` 

#### `compute_score` Parameters

```python
def compute_score(
    self,
    entity_dict_1: Dict[str, float],
    entity_dict_2: Dict[str, float],
    lower_bound: float = 0.0,
    upper_bound: float = 1.0,
) -> float:
```

1. **`entity_dict_1: Dict[str, float]`**
   - **Description**: A dictionary representing the first entity's properties and their corresponding values. This dictionary is typically used to represent the user's preferences or an ideal set of values.
   - **Example**: 
     ```python
     {
         "price": 0.9,
         "duration": 0.8,
         "difficulty": 0.8,
         "rating": 0.6
     }
     ```

2. **`entity_dict_2: Dict[str, float]`**
   - **Description**: A dictionary representing the second entity's properties and their corresponding values. This dictionary is typically used to represent the actual values of a course, property, or other item being scored.
   - **Example**: 
     ```python
     {
         "price": 1.0,
         "duration": 0.7,
         "difficulty": 0.6,
         "rating": 0.8
     }
     ```

3. **`lower_bound: float = 0.0`**
   - **Description**: The lower bound of the scale for adjusting the weights of the properties. This is the minimum value that a property weight can take after adjustment.
   - **Example**: `0.0` (default value)

4. **`upper_bound: float = 1.0`**
   - **Description**: The upper bound of the scale for adjusting the weights of the properties. This is the maximum value that a property weight can take after adjustment.
   - **Example**: `1.0` (default value)

#### Return Value

The function returns a float representing the computed score as a percentage. The score indicates how closely the properties of the second entity match the properties of the first entity based on their respective weights.

**Example Return Value**:
```python
85.0  # This indicates an 85% match between the two entities.
```

#### Functionality

The `compute_score` function calculates the similarity score between two entities based on their properties. It adjusts the weights of the properties within the specified bounds and computes the score as the average similarity across all properties.

#### Example

Suppose we have the following parameters:

```python
entity_dict_1 = {
    "price": 0.9,
    "duration": 0.8,
    "difficulty": 0.8,
    "rating": 0.6
}
entity_dict_2 = {
    "price": 1.0,
    "duration": 0.7,
    "difficulty": 0.6,
    "rating": 0.8
}
lower_bound = 0.0
upper_bound = 1.0
```


The function will adjust the weights of the properties within the specified bounds and compute the score based on the similarity between the two entities. The result might be a score indicating how well the properties of `entity_dict_2` match those of `entity_dict_1`.



### `compute_resource_allocation`


#### `compute_resource_allocation`-Parameters

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

1. **`property_id: str`**
   - **Description**: The identifier of the feature for which the resource allocation is being calculated.
   - **Example**: `"price"`, `"duration"`, `"difficulty"`

2. **`usage_amount: float`**
   - **Description**: The amount of resource usage for the specified feature.
   - **Example**: `0.9` for a high preference or usage amount.

3. **`allocation_parameters: Dict[str, Tuple[float, float]]`**
   - **Description**: A dictionary containing the allocation parameters for each feature. The key is the feature identifier, and the value is a tuple of two floats representing the allocation parameters (e.g., demand and supply parameters).
   - **Example**: 
     ```python
     {
         "price": (1.0, 0.7),
         "duration": (1.0, 0.6),
         "difficulty": (1.0, 0.9),
         "rating": (1.0, 0.9)
     }
     ```

4. **`is_demand: bool`**
   - **Description**: A boolean value indicating whether the calculation is for demand (`True`) or supply (`False`). This determines which value of the tuple in `allocation_parameters` is used.
   - **Example**: `True` for demand, `False` for supply.

5. **`available_resources: float`**
   - **Description**: The available resources that can be used for allocation.
   - **Example**: `20.0` for a total capacity of 20 units.

6. **`scale_factor: float = 1.0`**
   - **Description**: A scaling factor to adjust the usage amounts. The default value is `1.0`, meaning no scaling. A higher value increases the usage amounts accordingly.
   - **Example**: `5` for scaling from 1 to 5 stars.

#### Return Value

The function returns a tuple of two floats:

1. **`new_available_resources: float`**
   - **Description**: The remaining resources after allocation.
   - **Example**: `18.5` after the calculation.

2. **`cost: float`**
   - **Description**: The cost of resource usage for the specified feature.
   - **Example**: `1.5` for the usage cost.

#### Functionality

The `compute_resource_allocation` function calculates the resource distribution based on the provided parameters. It uses the allocation parameters and usage amounts to compute the cost and adjust the remaining resources. If the cost exceeds the available resources, a `ValueError` exception is raised.

#### Example

Suppose we have the following parameters:

```python
property_id = "price"
usage_amount = 0.9
allocation_parameters = {
    "price": (1.0, 0.7),
    "duration": (1.0, 0.6),
    "difficulty": (1.0, 0.9),
    "rating": (1.0, 0.9)
}
is_demand = True
available_resources = 20.0
scale_factor = 5
```
