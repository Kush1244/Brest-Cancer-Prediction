import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def read_data():
    df = pd.read_csv("data.csv")
    df.drop("Unnamed: 32", axis=1, inplace=True)
    return df


def SeparateX_Y(dataset):
    y = dataset["diagnosis"].values
    dataset.drop(["id", "diagnosis"], axis=1, inplace=True)
    x = dataset.iloc[:, :].values
    return y, x


def SplitIntoTrainingAndTestSet(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=0)
    return x_train, x_test, y_train, y_test


def LabelEncode(y):
    le = LabelEncoder()
    return le.fit_transform(y)


def FeatureScale(x):
    for i in x:
        print(i)


class DATASET(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.dataset = read_data()
            cls.y, cls.x = SeparateX_Y(cls.dataset)
            cls.y = LabelEncode(cls.y)
            # cls.x = FeatureScale(cls.x)
            cls.X_TRAIN, cls.X_TEST, cls.Y_TRAIN, cls.Y_TEST = SplitIntoTrainingAndTestSet(cls.x, cls.y)
            cls.instance = super(DATASET, cls).__new__(cls)
        return cls.instance
