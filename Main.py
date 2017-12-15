import URL
import User
import POI
import PlacesInfo
import Loading
import json
import Graph
class Main:
    def __init__(self):

        self.key_edge = self.__get_key_EDGE()
        self.key_POI = self.__get_POI()
        self.begin = URL.begin
        self.end = URL.end
        self.budget = self.__get_budget()
        self.key = self.__get_key()
        self.feature = []
        self.data_dct = self.make_request(self.key)
        self.user = User.Userclass(self.budget,self.feature,self.data_dct,self.begin,self.end,self.key_edge,self.key_POI)


    def make_request(self,key):
        dct = {}
        for i in range(key):
            dct1 = PlacesInfo.get_data_from_URL(self.begin)
            self.feature.append(self.__get_feature())
            for j in dct1:
                if j != None:
                    if i > 0 :
                        dct[j] = [0 for n in range(i)]+[dct1[j]]+[0 for n in range(key - 1 - i)]
                    else:
                        dct[j] = [dct1[j]] + [0 for n in range(key - 1)]
        dct[self.begin] = [0 for n in range(key - 1)]
        dct[self.end] = [0 for n in range(key - 1)]

        return dct

    def __get_budget(self):
        try:
            k = input("Enter your budget :")
            k = float(k)
        except ValueError:
            k = self.__get_budget()
        return k

    def __get_feature(self):
        try:
            k = input("Enter your feature :")
            k = float(k)
        except ValueError:
            k = self.__get_feature
        return k

    def __get_key(self):
        try:
            k = input("Enter the number of types : ", )
            k = int(k)
        except ValueError:
            k = self.__get_key()
        return k

    def __get_key_EDGE(self):
        try:
            k = input("Enter key of edge cost : ", )
            k = int(k)
        except ValueError:
            k = self.__get_key()
        return k

    def __get_POI(self):
        try:
            k = input("Enter key of POI cost : ", )
            k = int(k)
        except ValueError:
            k = self.__get_key()
        return k

    def __get_top(self):
        try:
            k = input("Enter number of top: ", )
            k = int(k)
        except ValueError:
            k = self.__get_key()
        return k


    def action(self):
        for i in self.user.PACER():
            print(i)


a = Main()
print("data == ",a.data_dct)
print("######################################################################################################################################################\n"+"######################################################################################################################################################\n")
a.action()