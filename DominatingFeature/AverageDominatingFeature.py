""" Finds The Average Value of Each Features for classification"""
""" CheckAverage Gives us the feature where we have clear distinction between 
    average feature that corresponds to 1 or 0
    e.g -> Suppose the average value of all features that give y == 0 is 17 and 
    and the average value of all features that give y == 1 is 13
    Now we check the how many of features that give 1 have average greater than 17.
    Let's say we get 3-4 feature. 
"""


class CheckAverage:
    def __init__(self, features_name, x, y, error_margin=0.5):
        self.features_name = features_name
        self.X = x
        self.Y = y
        self.errorMargin = error_margin
        self.AvgFeaturesValuesForEachCase = list()
        self.FindAvg()

    def FindAvg(self):
        for i in range(len(self.features_name)):
            good = 0
            bad = 0
            for j in range(len(self.features_name)):
                if self.Y[j] == 1:
                    good += self.X[j][i]
                else:
                    bad += self.X[j][i]
            self.AvgFeaturesValuesForEachCase.append([good, bad])

    def GetEachFeaturesCount(self):
        return self.AvgFeaturesValuesForEachCase

    def ReturnFeature(self):
        """ Returns the feature having average distinguishable """
        pass
