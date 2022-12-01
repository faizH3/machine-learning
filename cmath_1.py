class Chmath:
    def __init__(self):
        self.name = "math"
        # self.means = self.mean

    def mean(self, mean):
        # list
        self.mMean = 0
        self.nmean = mean

        # sum
        for x in self.nmean:
            self.mMean = self.mMean + x            
        
        self.means = self.mMean / len(self.nmean)
        return self.means
        
