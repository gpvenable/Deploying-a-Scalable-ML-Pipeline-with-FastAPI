# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: Random Forest Classifier
Library: scikit-learn
Input: Processed census data with encoded categorical and numerical features
Output: Binary classification of whether a person earns >$50k or <=$50k
## Intended Use
Classify people based on their census features
## Training Data
Source: UCI Adult Census Income dataset
Size: ~30k rows
## Evaluation Data
20% test split from the original dataset
## Metrics
Precision: 0.7419
Recall: 0.6384
F1 score: 0.6863

## Ethical Considerations
Data set main contain biases based on many factors
## Caveats and Recommendations
Model performance varies across data slices
Model is trained on static data
