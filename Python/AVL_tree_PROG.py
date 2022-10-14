#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self,data,parent):
        
        self.data = data
        self.rightchild = None
        self.leftchild = None
        self.parent = parent
        self.height = 0
class AVLTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data,None)
            
        else:
            self.insert_node(data,self.root)
            
    def insert_node(self,data,node):
        
        if data < node.data:
            if node.leftchild is not None:
                self.insert_node(data,node.leftchild)
                
            else:
                node.leftchild = Node(data,node)
                node.height = max(self.calheight(node.leftchild),self.calheight(node.rightchild))+1
        else:
            if node.rightchild is not None:
                
                self.insert_node(data,node.rightchild)
            else:
                node.rightchild = Node(data,node.rightchild)
                node.height = max(self.calheight(node.leftchild),self.calheight(node.rightchild))+1
    
        self.violation_helper(node)
    
    def remove(self,data):
        if self.root:
            self.remove_node(data,self.root)
            
    def remove_node(self,data,node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data,node.leftchild)
        elif data > node.data:
            self.remove_node(data,node.rightchild)
        else:
            if node.leftchild is None and node.rightchild is None:
                parent = node.parent
                if parent and parent.rightchild == node:
                    parent.rightchild = None
                if parent and parent.leftchild == node:
                    parnet.leftchild = None
                    
                if parent is None:
                    self.root = None
                del node
                
                self.violation_helper(node)
            
            elif node.leftchild is None and node.rightchild is not None:
                
                parent = node.parent
                if parent:
                    if parent.rightchild == node:
                        parent.rightchild = node.rightchild
                    if parent.leftchild == node:
                        parent.leftchild = node.rightchild
                else:
                    self.root = node.rightchild
                node.rightchild.parent = parent
                del node
                
                self.violation_helper(node)
            elif node.rightchild is None and node.leftchild is not None:
                parent = node.parent
                if parent:
                    if parent.rightchild == node:
                        parent.rightchild = node.leftchild
                    if parent.leftchild == node:
                        parent.leftchild = node.leftchild
                else:
                    self.root = node.leftchild
                    
                node.leftchild.parent = parent
                del node
                
                self.violation_helper(node)
            else: 
                predecessor = self.getpredecessor(node.leftchild)
                
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data,predecessor)
                
    def getpredecessor(self,node):
        if node.rightchild:
            return self.getpredecessor(node.rightchild)
        return node
    
    
    
    
    
    
    
    
    def traverse(self):
        if self.root is not None:
            self.traverse_lrR(self.root)
    def traverse_lrR(self,node):
        
        if node.leftchild is not None:
            self.traverse_lrR(node.leftchild)
            
        print(node.data)
        if node.rightchild is not None:
            self.traverse_lrR(node.rightchild)
    def violation_helper(self,node):
        ballance = self.calculate_balance(node)
        #we know the tree is left heavy
        if ballance > 1:
            # left right heavy situation left rotation on parent 
            #left - right 
            if self.calculate_balance(node.leftchild) < 0:
                self.rotate_left(node.leftchild)
            #right rotation on grandparent
            self.rotate_right(node)
        if ballance < -1:
            #right left heavy 
            if self.calculate_balance(node.rightchild) > 0:
                self.rotate_right(node.rightchild)
            #left rotation 
            self.rotate_left(node.rightchild)
            
                
            
    def calheight(self,node):
        if node is None:
            return -1
        else:
            return node.height
            
    def calculate_balance(self,node):
        if node is None:
            return 0
        return self.calculate_balance(node.leftchild) - self.calculate_balance(node.rightchild)
            
            
   
                
            
            
            
obj = AVLTree()
obj.insert(1)
obj.insert(5)
obj.insert(0)
obj.insert(3)
obj.insert(6)
obj.insert(2)
obj.insert(7)
obj.insert(4)
obj.traverse()
            
            
            
            
        

