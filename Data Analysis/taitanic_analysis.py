import pandas as pd
import numpy as np


class titanic_ana:
    def get_data(self,file_path):
        file_data=pd.read_csv(file_path)
        flag_age=~pd.isnull(file_data["Age"])
        file_age_ture=file_data[flag_age]
        pre_x=file_age_ture[["Pclass","Sex","Age","SibSp","Parch"]]
        post_y=file_age_ture["Fare"]
        return pre_x,post_y

    def fit(self,pre_x,post_y):
        pre_x_=np.linalg.inv(pre_x.T.dot(pre_x))
        ratio=pre_x_.dot(pre_x.T).dot(post_y)
        return ratio

if __name__=='__main__':
    ta=titanic_ana()
    re_x,post_y=ta.get_data(r'/Users/Elven/PycharmProjects/untitled/Data Analysis/train.csv')
    ratio=ta.fit(re_x,post_y)
    print(ratio)