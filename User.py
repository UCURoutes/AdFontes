import Graph
#import URL
import POI
import Priority_queue

#dct = PlacesInfo.dct

#lst = [POI.POIclass(i,dct[i]) for i in dct]
#g = Graphclass(lst,begin,end)



class Userclass:
    def __init__(self,budget,feature,dct_of_graph_POI,begin,end,key_edge=1,key_POINT=1):
        self.key_POINT = key_POINT
        self.key =key_edge
        self.budget = budget
        self.start = begin
        self.end = end
        self.feature = feature
        self.graph = Graph.Graphclass(dct_of_graph_POI, self.start,self.end,self.key,self.key_POINT)
        self.queue = Priority_queue.PriorityQueue()
    def db_function(self,h, lst_of_way, alfa=1 / 2):
        def f(p):
            lst = []
            for i in self.graph.dct_POI[p]:

                if i != None:
                    lst.append(i)
                else:
                    lst.append(0)
            if h > len(lst)-1:
                return 0
            return lst[h]


        lst_of_way.sort(key=f)
        lst_of_way = lst_of_way[::-1]
        sum1 = 0
        counter = 0
        for i in lst_of_way:
            counter += 1
            sum1 += f(i) * (counter ** (-alfa) + 0)
        return sum1

    def Gain(self,way_list):
        '''
        :param vector_of_index: tuple of futures.
        :return: result of Gain formula.
        '''
        number = 0
        ##########################
        # It will be code one day#
        ##########################

        for i in way_list:
            if i == self.start or i == self.end:
                number = 0
            else:
                for h in range(len(self.graph.dct_POI[i])):
                    if self.graph.dct_POI[i][h] != None:
                        number += self.graph.dct_POI[i][h] * self.db_function(h, way_list)
                    else:
                        number += 0 * self.db_function(h, way_list)
        return number

    def db_function_for_index_vector(self,h,alfa=1/2):
        if h == 0 or h == 0.0:return 0
        sum1 = h * ((self.feature.index(h)+1) ** (-alfa) + 0)
        return sum1

    def Gain_for_index_vector(self):
        number = 0
        for h in range(len(self.feature)):
                if self.feature[h] != None:
                    number += self.feature[h] * self.db_function_for_index_vector(self.feature[h])
                else:
                    number += 0 * self.db_function_for_index_vector(self.feature[h])
        return number
    def find_path(self,path_list,cost_of_path):

        def f(p):
            lst = []
            for i in self.graph.dct_POI[p]:

                if i != None:
                    lst.append(i)
                else:
                    lst.append(0)

            return [i for i in lst if i != 0][0]


        G = self.Gain(path_list)
        lst = self.graph.sort_edge_by_cost(path_list[-2])
        for i in lst:
            point = self.graph.next_min_cost_point(i[0])
            if i[1] == None:
                i[1] = 0
            if i[1] + self.graph.get_cost_of_edge(self.end,point)+self.graph.cost_of_point(point) <= self.budget-cost_of_path:
                path_list = path_list[:-2]+[path_list[-2]]+[i[0]]+[path_list[-1]]
                cost_of_path = self.graph.get_cost_of_the_way(path_list)
                new_G = self.Gain(path_list)
                if new_G > G:
                    G = new_G
                    self.queue.add_element(path_list,G)

    def PACER(self):
        list_PACER= []
        G = self.Gain_for_index_vector()
        self.find_path([self.start,self.end],self.graph.get_cost_of_edge(self.start,self.end))
        self.queue.sort_max_to_min()
        for i in self.queue.get_elements():
            lst = [i[j] for j in i if j >= G]
            list_PACER.append(lst)
        return list_PACER

