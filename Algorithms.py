"""
This file contains all of the search algrothms that you will have to impliment.

Please only change the parts of the file you are asked to.  Look for the lines
that say

"*** TTU CS3368 YOUR CODE HERE ***"

look for "*** TTU CS3368 READ THIS ***" if there is any 

The parts you fill in start about 3/4 of the way down.  Follow the project
description for details.

Good luck and happy searching!
"""

import util

from util import *
from collections import deque

class DFS(object):
    def depthFirstSearch(self, problem):
        """
        Search the deepest nodes in the search tree first
        [2nd Edition: p 75, 3rd Edition: p 87]

        Your search algorithm needs to return a list of actions that reaches
        the goal.  Make sure to implement a graph search algorithm
        [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** TTU CS3368 READ THIS ***"
        """
        Remember that you will best strategy is to use a stack. you can import stack from util
        Remember to keep track of visited states
        here is a plan:
        (1) import stack
        (2) intiate you variable
        (3) get the start state/node
        (4) push start node and empty path to stack
        (5) initiate a visted node variable
        (6) while there is something on you stack
            6.1 get the state and path
            6.2 if goal return goal
            6.3 else if you did not visit the state
                6.3.1 pass though all seccessors
                you can get a successor using problem.getSuccessors("yournode")
                    push the sucessor to you statck
            6.4 add the node to visited nodes
                
        prints can always help you alot     
        """
        "*** TTU CS3368 YOU CODE GO HERE ***"
        
        
        stack = Stack()                                                                     #Initialize stack from Stack() function                   
        startState = problem.getStartState()                                              
        stack.push((startState, [], Stack()))                                               #Push starting state in stack                                     

        while not stack.isEmpty():                                                          #Pop nodes until stack is empty     
            popped = stack.pop()                                                       
            state = popped[0]
            path = popped[1]
            visited = popped[2]
            
            if problem.isGoalState(state):                                                  #If the current node is the goal node return the path                        
                return path

            if state not in visited.list:                                                           
                visited.push(state)                                                       
                for successor in problem.getSuccessors(state):                             #Get successors of current state and push into stack 
                    stack.push((successor[0], path + [successor[1]], visited))             

        return None                                                                        #If no path was found to goal, return none                                        
        util.raiseNotDefined()
        
class BFS(object):
    def breadthFirstSearch(self, problem):
        "*** TTU CS3368 READ CODE HERE ***"
        "Idea is Same as DFS But with Queue, which you Queue import from util"
        queue = Queue()                                                                    #Initialize queue from Queue() function
        startState = problem.getStartState()                                               #Get start state
        queue.push((startState, [], Queue()))                                                        

        while not queue.isEmpty():                                                         #Keey poping nodes from queue
            popped = queue.pop()                                                          
            state = popped[0]                                                              
            path = popped[1]
            visited = popped[2]
            
            if problem.isGoalState(state):                                                
                return path

            if state not in visited.list:                                                   #Conditional to check if current state has been visited        
                visited.push(state)                                                         #If node hasn't been visited, add visit to stack
                for successor in problem.getSuccessors(state):                              
                    queue.push((successor[0], path + [successor[1]], visited))                
        
        util.raiseNotDefined()

class UCS(object):
    def uniformCostSearch(self, problem):
        "*** TTU CS3368 READ CODE HERE ***"
        "This is a Priority Queue so how to push your things to a priority queue?"
        "How to keep track of costs in the priotity queue? how to choose based on priority?"
        startState = problem.getStartState()
        if problem.isGoalState(startState):                                                  #Conditional check if start state is the goal
            return []
        priorityQueue = PriorityQueue()
        priorityQueue.push((startState, [], 0), 0)                                           #Push arguments in queue
        visited = set()                                                                      #Empty set

        while not priorityQueue.isEmpty():
            currentNode = priorityQueue.pop()
            state = currentNode[0]
            path = currentNode[1]
            cost = currentNode[2]
            if problem.isGoalState(state):
                return path
            if state not in visited:
                visited.add(state)  
                for successor, action, stepCost in problem.getSuccessors(state):
                    afterPath = path + [action]                                             #Update new path and new cost
                    afterCost = cost + stepCost
                    priorityQueue.push((successor, afterPath, afterCost), afterCost)        #Push the arguments into queue
        return None

    
        util.raiseNotDefined()
        
class aSearch (object):
    def nullHeuristic( state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0
    def aStarSearch(self,problem, heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        "*** TTU CS3368 YOUR CODE HERE ***"
        "how to extend USC to A*"

        "Search the node that has the lowest combined cost and heuristic first."
        startState = problem.getStartState()                                         
        if problem.isGoalState(startState):                                          
            return []
        priorityQueue = PriorityQueue()                                          
        priorityQueue.push((startState, [], 0), heuristic(startState, problem))                #Push code into queue
        visited = set()                                                                   
        while not priorityQueue.isEmpty():                                          
            currentNode = priorityQueue.pop()
            state = currentNode[0]
            path = currentNode[1]
            cost = currentNode[2]
            if state in visited:
                continue
            visited.add(state)
            if problem.isGoalState(state):
                return path                                                   
            for nextState, action, stepCost in problem.getSuccessors(state):                   #Loop through the successors
                afterPath = path + [action]                                             
                afterCost = cost + stepCost                                               
                priority = afterCost + heuristic(nextState, problem)                     
                priorityQueue.push((nextState, afterPath, afterCost), priority)                #Push arguements into queue
        return None
        util.raiseNotDefined()
