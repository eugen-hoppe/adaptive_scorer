# adaptive_scorer

**Adaptive Scorer (Version 1.0)**

AdaptiveScorer is a library for scoring and matching entities based on specified properties. It can be used in various applications, such as e-learning platforms, real estate platforms, and more. The library allows for the creation of complete property dictionaries, computation of matching scores, and calculation of resource usage.


## Installation
```bash
pip install git+https://github.com/eugen-hoppe/adaptive_scorer.git
```


## Purpose of Parameters

- **Bounds (`lower_bound`, `upper_bound`)**: These parameters define the range within which the property weights are adjusted. They ensure that the weights are scaled appropriately to provide accurate and meaningful scores.
- **Learning Parameters (`learning_parameters`)**: These parameters are tuples that influence the calculation of resource usage. They help in determining how the weight of a property affects the consumption of resources.
- **Scale Factor (`scale_factor`)**: This factor is used to adjust the weights during the computation of resource usage. It ensures that the weights are scaled to a meaningful range for the specific application.
- **Resource Usage (`compute_resource_usage`)**: This function calculates the amount of resources required for a given property weight. It helps in managing and optimizing the allocation of resources based on the specified parameters.


## Examples

### E-Learning Platform Example

```bash
python examples/e_learning.py
```

**Description of Example and Significance of the Algorithm**

The `AdaptiveScorer` library enables the e-learning platform to match courses and learning preferences. By comparing specific properties such as Mathematics, Physics, Computer Science, and Literature, the library calculates the alignment between course offerings and individual student preferences. This enhances the learning experience by helping students find the courses that best suit their needs. Additionally, the library can calculate resource usage, such as the time required or the effort needed for a course. Through this flexible and adaptable method, the e-learning platform optimizes matching and improves the efficiency of the learning process.

### Real Estate Platform Example

```bash
python examples/real_estate.py
```

**Description of Example and Significance of the Algorithm**

The `AdaptiveScorer` library allows the real estate platform to match property characteristics with buyer preferences. By comparing specific features such as location, size, price, and condition, the library evaluates the alignment between available properties and the preferences of prospective buyers. This results in better recommendations and an improved user experience, as buyers can find properties that best meet their needs. Additionally, the library can calculate resource usage, such as the time or effort required for a viewing. Through this flexible and adaptable method, the real estate platform optimizes matching and enhances the efficiency of the property transaction process.
