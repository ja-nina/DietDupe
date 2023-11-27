# Evaluation Measures

- accuracy-based
- expert evaluation
    - A human expert oversees the model. The model outputs top-5 candidates for
    a given ingredient. The expert labels each of the candidates as accepted (1)
    or denied (0). The model receives feedback as a weighted sum of the labels,
    where the weights are 1, ½, ⅓, ... (MRR)
