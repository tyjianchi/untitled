import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

class dataanalysis:
    def __init__(self):
        self.w=None

    def fit(self,X,y):
        print(X.shape)
        X=np.insert(X,0,1,axis=1)
        print(X.shape)
        X_=np.linalg.inv(X.T.dot(X))
        self.w=X_.dot(X.T).dot(y)

    def predict(self,X):
        X=np.insert(X,0,1,axis=1)
        y_pred=X.dot(self.w)
        return y_pred

    def mean_squared_error(self,y_true,y_pred):
        mse=np.mean(np.power(y_true-y_pred,2))
        return mse

    def main(self):
        dts=datasets.load_diabetes()

        X=dts.data[:,np.newaxis,2]
        print(dts.data)
        print(dts.target)
        x_train,x_test=X[:-20],X[-20:]

        y_train,y_test=dts.target[:-20],dts.target[-20:]
        clf=dataanalysis()
        clf.fit(x_train,y_train)
        y_pred=clf.predict(x_test)

        print("mean squared Error:",clf.mean_squared_error(y_test,y_pred))

        # plt.scatter(x_test[:,0],y_test,color='black')
        # plt.plot(x_test[:,0],y_pred,color='blue',linewidth=3)
        # plt.show()

daa=dataanalysis()
daa.main()