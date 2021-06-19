import numpy as np
import pickle

from sklearn.linear_model import LinearRegression

# using boston house-prices dataset
from sklearn.datasets import load_boston 

from flask import Flask, request
app = Flask(__name__) #creating Flask-object

# model learning
X, y = load_boston(return_X_y=True)
X = X[:, 0].reshape(-1, 1) 
regressor = LinearRegression()
regressor.fit(X,y)

# serialisation
with open('my_file.pkl', 'wb') as output: 
    pickle.dump(regressor, output) #saving of binary model
    
#  function of prediction model
def model_predict(value):
    '''Return result of prediction of the argument value'''
    #deserialisation
    with open('my_file.pkl', 'rb') as pkl_file: 
            regressor_from_file = pickle.load(pkl_file) #loading of binary model
       
    value_to_predict = np.array([value]).reshape(-1, 1)
    return regressor_from_file.predict(value_to_predict)

#  request procession function 
@app.route('/predict')
def predict_func():
    '''Returned result of prediction from the model.'''
    value = request.args.get('value')
#     checking for integer value
    try:
        prediction = model_predict(float(value))
        return f'the result of prediction is {prediction}!'
    except ValueError:
        return f'Not an integer! Enter integer value.'
    

# running of application on server
# network interface address - localhost, and port - 5000
if __name__ == '__main__':
    app.run('localhost', 5000)    