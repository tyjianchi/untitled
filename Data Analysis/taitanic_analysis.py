import pandas as pd
import numpy as np


class titanic_ana:
    def __init__(self):
        self.raito=None

    def get_data(self,file_path):
        file_data=pd.read_csv(file_path)
        # file_data.dropna(subset=["Age"],axis=0,inplace=True)
        # file_data.replace({'Sex':{'male':0,'female':1}},inplace=True)
        pre_x=file_data[["Pclass","SibSp","Parch"]]
        post_y=file_data["Fare"]
        return pre_x,post_y

    def test_data(self,file_path):
        file_data = pd.read_csv(file_path)
        # file_data.dropna(subset=["Age"],axis=0,inplace=True)
        # file_data.replace({'Sex':{'male':0,'female':1}},inplace=True)
        test_x=file_data[["Pclass","SibSp","Parch"]]
        return test_x

    def fit(self,pre_x,post_y):
        pre_x.insert(0,"Seq",1)
        pre_x_=np.linalg.inv(pre_x.T.dot(pre_x))
        self.raito=pre_x_.dot(pre_x.T).dot(post_y)
        return self.raito

    def predict(self,test_x):
        test_x.insert(0, "Seq", 1)
        return test_x.dot(self.raito)


    def test1(self):
        df = pd.DataFrame(np.random.randn(5, 3), index=list('abcde'),
                          columns=['one', 'two', 'three'])  # 随机产生5行3列的数据
        df.iloc[1, :2] = np.nan  # 将指定数据定义为缺失
        df.iloc[2:-1, 2] = np.nan
        print(df)
        df.dropna(subset=["three"],axis=0,inplace=True)
        print(df)
if __name__=='__main__':
    ta=titanic_ana()
    # ta.test1()
    pre_x,post_y=ta.get_data(r'/Users/Elven/PycharmProjects/untitled/Data Analysis/train.csv')
    ta.fit(pre_x,post_y)
    test_x=ta.test_data(r'/Users/Elven/PycharmProjects/untitled/Data Analysis/test.csv')
    test_y=ta.predict(test_x)
    test_y.to_csv(r'/Users/Elven/PycharmProjects/untitled/Data Analysis/result.csv')
    print(test_y)
