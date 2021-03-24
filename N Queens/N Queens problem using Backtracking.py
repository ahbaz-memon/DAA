#!/usr/bin/env python
# coding: utf-8

# In[32]:


def display_board(board):
    for row in board:
        for e in row:
            print(e, end = '    ')
        print('\n')


# In[33]:


def is_safe(board, x, y, n):
    #upper column
    for row in range(x - 1, -1, -1):
        if board[row][y] == 1:
            return False
    
    # upper left diagonal
    row  = x - 1
    column = y - 1
    while row >=0 and column >=0:
        if board[row][column] == 1:
            return False
        row -= 1
        column -= 1
    
    # upper right diagonal
    row = x - 1
    column = y + 1
    while row >= 0 and column < n:
        if board[row][column] == 1:
            return False
        row -= 1
        column += 1
    
    return True


# In[34]:


def solveNQ(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solveNQ(board, col + 1, N) == True:
                return True
            board[i][col] = 0
    return False


# In[35]:


def solveNQ_main(board, n):
    if solveNQ(board, 0, n) == False:
        print("Solution does not exist")
        return False
    display_board(board)
    return True


# In[36]:


n = int(input("Enter the number of Queen's for board -> "))


# In[37]:


board = [[0] * n] * n


# In[38]:


display_board(board)


# In[39]:


solveNQ_main(board, n)


# In[ ]:




