from heapq import*
from collections import*
from sys import*
input = lambda:stdin.readline().strip()
INF=1e9
class hash:
    def __init__(self):
        self.idx=0
        self.dic={}
        self.keyList=[]
    def stoi(self, string):
        try:
            return self.dic[string]
        except:
            self.dic[string] = self.idx
            self.keyList.append(string)
            self.idx+=1
            return self.dic[string]
    def itos(self, index):
        return self.keyList[index]
class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = self.right = None
class HuffmanTree:
    def __init__(self):
        self.rootList=deque()
    def merge(self, x, y):
        xfreq, xkey = x
        yfreq, ykey = y
        
        if xkey!=INF: xNode = Node(xfreq, xkey)
        
        else: xNode = self.find(xfreq, xkey)
        if ykey!=INF: yNode = Node(yfreq, ykey)
        else: yNode = self.find(yfreq, ykey)
       
        parent = Node(xfreq+yfreq, INF)
        parent.left = xNode
        parent.right = yNode
        
        self.rootList.append(parent)
        self.root = self.rootList[0]
    def find(self, freq, key):  
       
        while self.rootList:
            root = self.rootList.popleft()
            node = self._find(root, freq, key)
            if node is None:
                self.rootList.append(self.rootList.popleft())
            else:
                return node
    def _find(self, node, data, key):
        if node is None or (data == node.data and key == node.key): return node
        if data < node.data: return self._find(node.left, data, key)
        if data > node.data: return self._find(node.right, data, key)
    def findKey(self, data, key):
        return self._findKey(self.root, data, key, '')
    def _findKey(self, node, data, key, res):
        if node is None or data == node.data: return res
        if data < node.data: return self._findKey(node.left, data, key, res+'0')
        if data > node.data: return self._findKey(node.right, data, key, res+'1')

    def levelorder(self):
        self._levelorder(self.root)
    def _levelorder(self, node):
        q=deque()
        q.append(node)
        while q:
            node = q.popleft()
            if node is None: continue
            print(node.data, node.key)
            q.append(node.left)
            q.append(node.right)
   
    def makeHTTable(self):
        self.intable={}
        self.detable={}
        self._makeHTTable(self.root, '')
    def _makeHTTable(self, node, res):
        if node is None: return
        if node.key != INF:
            self.intable[hs.keyList[node.key]] = res
            self.detable[res] = hs.keyList[node.key]
            return
        self._makeHTTable(node.left, res+'0')
        self._makeHTTable(node.right, res+'1')
    
    def decoding(self, string):
        return self._decoding(self.root, string, 0)
    def _decoding(self, node, string, pos):
        if node.key != INF: return node.key
        if pos == len(string): return INF
        if string[pos] == '0': return self._decoding(node.left, string, pos+1)
        if string[pos] == '1': return self._decoding(node.right, string, pos+1)

a=input()
hs=hash()
for i in range(len(a)):
    hs.stoi(a[i])
maxLen = hs.idx
cnt = [[0, i]for i in range(maxLen)]    
for i in range(len(a)):                 
    cnt[hs.dic[a[i]]][0] += 1
pq = []
for i in range(maxLen):
    heappush(pq, cnt[i])
ht = HuffmanTree()
if len(pq)==1:     
    heappush(pq,[INF, INF])
while len(pq)>1:  
    x = heappop(pq)
    y = heappop(pq)
    ht.merge(x, y)
    heappush(pq, [x[0]+y[0], INF])

ht.makeHTTable()

res=''
for i in range(len(a)):
    res+=ht.intable[a[i]]
    print('인코딩:',res)

ans=''
temp=''
for i in range(len(res)):
    temp += res[i]
    try:
        ans += ht.detable[temp]
        temp=''
    except:
        pass
print('디코딩:',ans)