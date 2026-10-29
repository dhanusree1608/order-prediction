# Online Order Prediction

A machine learning project that predicts whether a customer will **order** a product or **not**, using a Logistic Regression model.

## Data
`online_order_prediction_data.xlsx` has 200 rows and these columns:

| Column | Meaning |
|---|---|
| Review rating | Product review score (1 to 5) |
| Quality rating | Product quality score (1 to 5) |
| Price (₹) | Product price |
| Ordered or not | Result: ordered / not ordered |

> Note: only the first 10 rows are real sample values. The remaining rows are randomly generated for practice, so results are for learning only.

## Model
- Algorithm: Logistic Regression (with feature scaling)
- Train/test split: 80% / 20%
- Test accuracy: about 80%

## How to run
1. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
2. Open the notebook `order_prediction_model.ipynb` in Jupyter and run all cells.
3. The trained model is saved as `order_model.joblib`.

## Use the saved model
```python
import joblib, pandas as pd

model = joblib.load('order_model.joblib')
row = pd.DataFrame([[4.5, 5, 400]], columns=['Review rating', 'Quality rating', 'Price (₹)'])
print(model.predict_proba(row)[0, 1])   # chance of ordering
```

## Run the web app (optional)
```
streamlit run app.py
```
