# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This project uses a Random Forest classifier to predict individuals that earn more than $50,000 per year.
The model is trained on data from the U.S. Census. Categorical features were processed using OneHotEncoder, and labels were binarized with LabelBinarizer.

## Intended Use

The model is intended for educational purposes and to demonstrate the complete workflow of a machine learning pipeline, including data preprocessing, model training, evaluation, and deployment with FastAPI.
This is not intended for making real-world employment, financial, or income-related decisions.

## Training Data

The model was trained from a subset of publically available data from U.S. Census Bureau. 
The dataset includes demographic and employment features such as age, workclass, education, marital status, occupation, relationship, race, sex, and native country.
The training set was split from the full dataset using an 75/25 train-test split.

## Evaluation Data

The test set was used to evaluate the model's performance and is a 25% subset of the full census dataset.
The model performance was also evaluated on slices of the data corresponding to unique values of categorical features.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model is evaluated with the standard classification metrics:
- Precision: 0.7436
- Recall: 0.6237
- F1 Score: 0.6784 

Overall, the model was 74% correct in predicting individuals that earn more than %50,000.
Of the individuals that did earn more than $50,000, the model correctly identified 62% of them.
The F1 Score shows a decent balance between the precision and recall.

Additionally, he performance on the categorical slices are saved in slice_output.txt. An example of the slice metrics include:
- education: Bachelors
    Precision: 0.7748 | Recall: 0.7073 | F1: 0.7395
- marital-status: Divorced
    Precision: 0.7321 | Recall: 0.3796 | F1: 0.5000

These metrics shows the model's performance across different subgroups.

## Ethical Considerations

The model uses demographic features like race and sex, which could possibly introduce bias.

## Caveats and Recommendations
The model is for demonstration purposes only.
The small subgroups in the categorical slices may have unstable metrics due to having few samples.
There may be potential bias in the dataset due to demographic features in the dataset.
Based on the metrics, there is still room for improvement for the model.