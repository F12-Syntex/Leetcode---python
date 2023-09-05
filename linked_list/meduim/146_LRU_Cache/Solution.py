class DoublyListNode(object):
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyListNode(0, 0)
        self.tail = DoublyListNode(0, 0)        

    #remove the node from the dll
    def remove(self, node):

        if node.key not in self.cache:
            return 

        #in order for us to remove a node we need to set the nodes prev to it's next and set it's next to it's prev
        nxtNode = node.next
        prevNode = node.prev

        if node.prev:
            node.prev.next = nxtNode

        if node.next:
            node.next.prev = prevNode   

        node.next = None
        node.prev = None

    #add the node to the end of the list
    def append(self, node):

        #get the old tail
        prevTail = self.tail.prev

        #if the prev tail does not exist, that means we are appending a value for the first time
        if not prevTail:
            self.tail.prev = self.head.next = node
            return
        
        #set the prev tail's next to the current node
        prevTail.next = node

        #set the prev of the new tail to the prev tail, then set it's next to the parent tail
        node.prev = prevTail
        node.next = self.tail

        #set the parent tails prev to the new tail
        self.tail.prev = node

        return -1

    #get the value from the key if it exists
    #update the retreived value, and make it the most recent
    def get(self, key):
        if key in self.cache:            
            node = self.cache[key]
            #make the value at key the most recently used
            self.remove(node)
            self.append(node)

            return node.val
        return -1
    

    #add the value to the map and make it the most recent
    #evict the least used value, which will be located at self.head.right
    def put(self, key, value):

        if key in self.cache:
            self.remove(self.cache[key])

        #add the key at the end, first add it to the map then append it to the ll    
        node = DoublyListNode(key, value)
        self.cache[key] = node
        self.append(node)

        #remove the least used value if we're over capacity
        if len(self.cache) > self.capacity:
            lsf = self.head.next
            self.remove(lsf)
            del self.cache[lsf.key]

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, "hi")
obj.put(2, "hey")

#2, 1
param_1 = obj.get(2)

#2, 3
obj.put(3,"hiyo")
param_1 = obj.get(2)

#2, 4
obj.put(4, "wow")
