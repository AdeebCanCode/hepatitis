# Hepatitis C Prediction Model

## Overview
This repository contains a Hepatitis C diagnostic model based on machine learning, developed to improve diagnostic efficiency and accuracy through the analysis of common blood parameters. The model uses logistic regression to accurately predict Hepatitis C, with the potential to streamline the diagnostic process for healthcare professionals and reduce the need for resource-intensive laboratory procedures. This README provides an in-depth look into the project’s purpose, methodologies, and results.

---



---

## Project Purpose
The primary objective of this project is to develop a machine learning model capable of predicting the likelihood of Hepatitis C using basic blood test parameters. By accurately identifying cases of Hepatitis C, this model aims to:
- Enhance early detection, leading to timely intervention and management.
- Reduce diagnostic time and cost by minimizing the need for extensive testing.
- Integrate into a web application for seamless use by healthcare professionals in real-time scenarios.

---

## Background and Motivation
Hepatitis C remains a significant public health issue globally, often progressing to severe liver conditions such as cirrhosis and liver cancer if left undiagnosed and untreated. Traditional diagnostic methods involve two stages: an antibody test followed by RNA confirmation, requiring extensive lab resources and expertise. Leveraging blood test parameters commonly available from routine examinations, this machine learning approach provides an alternative that is not only time- and cost-efficient but also scalable.

---

## Data Collection and Processing
### Dataset
The dataset comprises 616 patient records, each with 12 key blood parameters known to correlate with liver health. These include:
- **Alanine Aminotransferase (ALT)**
- **Albumin (ALB)**
- **Alkaline Phosphatase (ALP)**
- **Aspartate Aminotransferase (AST)**
- **Total Bilirubin (TBIL)**
- **Total Protein (PROT)**
- **Cholesterol (CHOL)**
- **Serum Cholinesterase (CHE)**
- **Gamma-Glutamyl Transferase (GGT)**
- **Creatinine (CREA)**

### Data Preprocessing
Data preprocessing involved:
1. **Handling Missing Values**: Imputing or removing incomplete records to ensure model reliability.
2. **Normalization**: Standardizing blood parameter values to allow the model to learn effectively without bias towards feature magnitudes.
3. **Splitting the Dataset**: Dividing the dataset into 70% training, 20% testing, and 10% validation to ensure robust performance evaluation.

### Feature Selection
Through exploratory data analysis, it was determined that AST, GGT, and TBIL showed strong positive correlations with Hepatitis C diagnosis. This feature selection enhanced the model’s predictive focus and minimized overfitting.

---

## Machine Learning Model Selection
Three models were evaluated for this project:
1. **Logistic Regression**: A widely used algorithm for binary classification due to its interpretability and computational efficiency. Achieved optimal results in this project.
2. **Random Forest**: An ensemble learning method that leverages multiple decision trees. While effective, it was computationally heavier than logistic regression.
3. **K-Nearest Neighbors (KNN)**: Though simple, KNN required extensive memory and processing, leading to less favorable performance.

After comparison, logistic regression was selected for its high accuracy and straightforward interpretability, achieving a predictive accuracy of **94.5%**.

---

## Model Evaluation and Performance
### Evaluation Metrics
The model’s performance was assessed using:
- **Accuracy**: Achieved a high level of accuracy, with logistic regression proving the most effective among tested models.
- **Precision, Recall, and F1-Score**: Provided insights into the model’s ability to correctly classify positive cases without generating excessive false positives or false negatives.
- **Confusion Matrix**: Visualized the model’s classification performance, specifically its ability to reduce false negatives (critical in medical diagnostics).

### Results Summary
The logistic regression model demonstrated superior accuracy (94.5%) with precision, recall, and F1 scores indicating a strong performance. The confusion matrix highlighted a minimal number of false negatives, emphasizing the model’s reliability in correctly identifying Hepatitis C cases.

---

## Methodology and Implementation Details
1. **Data Exploration**: Initial EDA was performed to identify significant patterns, including correlation analysis, data distribution plots, and feature interaction graphs.
2. **Feature Engineering**: Created polynomial features from core blood parameters to capture non-linear relationships, which were tested but eventually excluded to simplify the model without sacrificing accuracy.
3. **Logistic Regression Model**: Trained with regularization to prevent overfitting. Hyperparameter tuning (e.g., regularization strength) was performed using cross-validation to maximize generalizability.
4. **Deployment Preparation**: The model is wrapped in a RESTful API built with FastAPI, enabling seamless integration into healthcare systems for real-time predictions.

---

## Results and Insights
- **Accuracy and Precision**: The model achieved high accuracy, with precision scores indicating reliable predictions across all cases, including those with minor deviations in blood parameters.
- **Confusion Matrix Analysis**: Showed low false negatives and high true positives, essential in a medical setting to avoid misdiagnosing potentially serious cases.
- **Practical Application**: With real-time integration, the model can serve as an immediate diagnostic aid, particularly useful in resource-limited settings where full laboratory testing is not always feasible.

---

## Future Work and Improvements
1. **Larger Dataset with Diverse Patient Demographics**: Adding more data, especially from different demographic backgrounds, could improve model accuracy across diverse populations.
2. **Advanced Features**: Including other clinical variables, such as BMI and family medical history, may increase predictive power.
3. **Model Ensembling**: Incorporating ensemble methods, such as Gradient Boosting, could further enhance accuracy and robustness.
4. **Continuous Learning**: Deploying a self-improving system that updates the model periodically based on new diagnostic data would enhance its effectiveness over time.

---


This project provides a solid foundation for scalable, accessible, and efficient Hepatitis C diagnostics through machine learning, with the goal of improving patient outcomes and reducing the strain on healthcare resources.
