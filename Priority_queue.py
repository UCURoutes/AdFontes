def f(dct):
    k = list(dct.keys())[0]
    return k
class PriorityQueue:
    def __init__(self):
        self.__elements = []

    @staticmethod
    def f(dct):
        k = list(dct.keys())[0]
        return k

    def add_element(self, element,priority):
        dct = {priority:element}
        self.__elements.append(dct)

    def sort_max_to_min(self):
        self.sort_min_to_max()
        self.__elements.reverse()

    def sort_min_to_max(self):
        self.__elements.sort(key=f)

    def get_elements(self):
        return self.__elements

    def pop(self):
        self.sort_max_to_min()
        k = self.__elements[0]
        self.__elements.remove(k)
        return k

    def __str__(self):
        return str(self.__elements)
#a = PriorityQueue()
#a.add_element("a",3)
#a.add_element("b",2)
#a.add_element("c",1)
#a.sort_max_to_min()
#print(a.get_elements())
#a.sort_min_to_max()
#print(a.get_elements())
#print(a.pop())
#print(a.get_elements())