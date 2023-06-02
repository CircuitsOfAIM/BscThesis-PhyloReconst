import pandas as pd
import pickle   
import numpy as np
import sklearn.ensemble

if __name__=="__main__":
    # insert your input data path
    test_data = pd.read_csv('vazi-sp015-input.csv')
    
    data = test_data.reset_index(drop=True)
    x_test = np.array(data)

    rdmodel = pickle.load(open('finalized_model.sav','rb'))

    prediction = rdmodel.predict(x_test)

    np.savetxt('output_vaez.csv', prediction, delimiter=',')
