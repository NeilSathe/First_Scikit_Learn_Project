**Grade Predictor Based on Study Hours**

A simple python project that uses machine learning to predict the users grade as a percentage based on study time.

Important : This README file was written long after this project was created. 

**Overview**

The program created uses scikit-learn's linear regression model in combination with a csv file of data (unable to be uploaded) to create a machine learnign model that takes the users input of study time and use it to predict their grade on an assesment.
This allows the users to determine the relation between their study hours and grades, letting them decide on how they can study more effeciently.

**Tools**

The tools used to create this project are :

- Python 3.11 (Language)
- Pandas (File Handling or I/O)
- Scikit-learn (Machine Learning Component)
- Microsoft Excel (File Handling)


**How To Run**

1. Clone the repo  
2. Install dependencies:
   pip install scikit-learn pandas
3. Run:
   python linear_regression.py

**Reflection**

This was one of my extremely early machine learning projects where I was focusing on learning simple concepts like Linear Regression and data handelling with pandas. 
Although the code is not structured well, it shows my early understanding of basic python structures like 2d arrays, dataframes and file i/o. The training data csv is unable to be uploaded.
One improvement I would make if I re-programmed this today is that i would convert the inputs from a 2D array into an actual pandas dataframe which would resolve the warning that X was trained with feature lables.
Additionally, I would wrap the program within a definition and handle inputs outside.
