from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/result", methods=['POST'])
def result():
    try:
        age = int(request.form['age'])
        sex = int(request.form['sex'])  # 1 = Male, 0 = Female
        EDUC = int(request.form['EDUC'])
        SES = int(request.form['SES'])
        MMSE = float(request.form['MMSE'])
        eTIV = float(request.form['eTIV'])
        nWBV = float(request.form['nWBV'])
        ASF = float(request.form['ASF'])
        
        df = pd.read_csv('oasis_longitudinal.csv')
        df["SES"].fillna(df["SES"].median(), inplace=True)
        df["MMSE"].fillna(df["MMSE"].mean(), inplace=True)
        df['Group'] = df['Group'].replace(['Converted'], ['Demented'])
        df['Group'] = df['Group'].map({"Demented": 1, "Nondemented": 0})
        df['M/F'] = df['M/F'].replace({'F': 0, 'M': 1})
        print("Prediction received:", [age, sex, EDUC, SES, MMSE, eTIV, nWBV, ASF])

        X = df[["M/F", "Age", "EDUC", "SES", "MMSE", "eTIV", "nWBV", "ASF"]].values
        y = df[["Group"]].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = RandomForestClassifier(n_estimators=200, max_depth=8, max_features='sqrt', criterion='gini')
        model.fit(X_train, y_train.ravel())
        print("Prediction received:", [age, sex, EDUC, SES, MMSE, eTIV, nWBV, ASF])

        prediction = model.predict([[sex, age, EDUC, SES, MMSE, eTIV, nWBV, ASF]])
        print("Model output:", prediction[0])
        if prediction[0] == 1:
            return render_template('alzimers.htm')
        else:
            return render_template('noalzimers.html')

    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
