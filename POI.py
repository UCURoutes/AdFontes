class POIclass:
    def __init__(self,coordinates,feature,cost=0):

        self.coordinates = coordinates
        self.feature = feature
        self.cost = cost

    def __eq__(self, other):
        if type(self) == type(other) and self.feature == other.feature and self.coordinates == other.coordinates and self.cost == other.cost:
            return True
        else:
            return False


#################################################
#################################################
#################################################

class Edge:
    def __init__(self,poi1,poi2,key=1):
        self.poi1 = poi1
        self.poi2 = poi2
        self.cost = self.count_cost()*key
    def count_cost(self):
        return ((self.poi1[0] - self.poi2[0])**2 + (self.poi1[1] - self.poi2[1])**2)**(1/2)

