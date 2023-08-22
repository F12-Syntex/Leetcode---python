class TimeMap(object):

    def __init__(self):
        self.store = {}
        

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([value, timestamp])


    def get(self, key, timestamp):
        res = ""

        if key not in self.store:
            return res
        
        values = self.store[key]

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
    
    def print(self):
        print(self.store)
        


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set(1, 1, 1)
param_2 = obj.get(1,1)
print(param_2)