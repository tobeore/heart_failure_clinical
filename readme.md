# Heart Failure Clinical Records Classification

## Overview

This project involves building and evaluating machine learning models to predict heart failure events based on clinical records. The dataset used includes various health-related features of patients, and the goal is to classify whether a patient is likely to experience a heart failure event (`DEATH_EVENT`).

## Project Structure

- `EDA.py`: Contains functions for exploratory data analysis (EDA).
- `heart_failure_clinical_records_dataset.csv`: Dataset used for classification.
- `classification.py`: Contains code for preprocessing, training models, and evaluating results.

## Libraries Used

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `imblearn`

## Dataset

The dataset `heart_failure_clinical_records_dataset.csv` contains the following columns:

- `age`: Age of the patient
- `anaemia`: Whether the patient has anaemia
- `creatinine_phosphokinase`: Level of creatinine phosphokinase in the blood
- `diabetes`: Whether the patient has diabetes
- `ejection_fraction`: Percentage of blood pumped out of the heart
- `high_blood_pressure`: Whether the patient has high blood pressure
- `platelets`: Platelets count in the blood
- `serum_creatinine`: Serum creatinine level in the blood
- `serum_sodium`: Serum sodium level in the blood
- `sex`: Gender of the patient (1 = male, 0 = female)
- `smoking`: Whether the patient is a smoker
- `time`: Follow-up period in days
- `DEATH_EVENT`: Target variable indicating heart failure (1 = event, 0 = no event)


