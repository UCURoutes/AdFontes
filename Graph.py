import POI

class Graphclass:

    def __init__(self,dct_POI,start,end,key=1,key_POI=1):
        self.key_POI = key_POI
        self.start = start
        self.key =key
        self.end = end
        self.dct_POI = dct_POI
        self.dct_POI_edge = self.__dct_graph_EDGE(self.key)




    def __dct_graph_EDGE(self,key):
        dct = {}
        for i in self.dct_POI:
            lst = []
            for j in self.dct_POI:
                if i != j:
                    lst.append([i,self.get_cost_of_edge(i,j)])
                    dct[i] = lst
        dct[self.start] = [[i,self.get_cost_of_edge(i,self.end)]for i in self.dct_POI]
        dct[self.end] = [[i,self.get_cost_of_edge(i,self.end)]for i in self.dct_POI]
        return dct

    def get_cost_of_the_way(self,lst_of_POI):
        """
        :param lst_of_POI: list of way 
        :return: cost of these way
        """

        s = 0
        for i in range(len(lst_of_POI)):
            if i+1 <= len(lst_of_POI)-1:
                s += self.get_cost_of_edge(lst_of_POI[i],lst_of_POI[i+1]) + self.cost_of_point(lst_of_POI[i]) * self.key_POI
        return s


    def get_cost_of_edge(self,poi1,poi2):
        return POI.Edge(poi1,poi2,self.key).cost

    def sort_edge_by_cost(self,poi):
        def f(i):
            return i[1]
        lst = [i for i in self.dct_POI_edge[poi]]
        lst.sort(key=f)
        return lst

    def min_cost_edge(self,point,key1=0):
        def f(i):
            return i[1]
        lst = [i for i in self.dct_POI_edge[point]]
        lst.sort(key=f)
        if lst != []:
            return ([point,lst[key1][0]],lst[key1][1])

    def min_cost(self,poi):
        return self.min_cost_edge(poi)[1]


    def next_min_cost_point(self,poi):
        return self.min_cost_edge(poi)[0][1]


    def cost_of_point(self,poi):
        lst = [i for i in self.dct_POI[poi]]
        for i in range(len(lst)):
            if lst[i] == None:
                lst[i] = 0
        if lst == [0.0]:return lst[0] * self.key_POI
        elif lst == [None]:return 0
        elif [i for i in lst if i!= 0] == []: return 0
        else:return [i for i in lst if i!= 0][0]



