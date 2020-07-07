#!/usr/bin/env python
# coding: utf-8

# # Web App

# In[67]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[68]:


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


# In[69]:


@app.route('/')

def home():
    return render_template('index.html')


# In[70]:


@app.route('/predict',methods=['POST'])

def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Insurance Claim should be {}'.format(output))


# In[73]:


env FLASK_ENV=development FLASK_APP=App.ipynb flask run


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False) # Note this step

# if __name__ == "__main__":
#     app.run(debug=True)


# In[66]:


get_ipython().system('jupyter nbconvert --to script App.ipynb')

