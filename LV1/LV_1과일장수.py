def solution(k, m, score):
    result = 0
    score = sorted(score,reverse = True)
    
    if len(score)<m:
        return 0
    
    for i in range(0,len(score)//m,1):
            
        result+=score[i*m+m-1]*m
        
    return result    

#%%
#
'''
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''

# %%
a = ['but'
,'i'
,'wont'
,'hesitate'
,'no'
,'more'
,'no'
,'more'
,'it'
,'cannot'
,'wait'
,'im'
,'yours']
max_length = 0
for i in a:
    if max_length < len(i):
        max_length = len(i)
x = []
y = []
for i in range(1,max_length+1):
    for j in a:
        if len(j) ==i:
            x.append(j)
    sorted(x,reverse=False)
    y += x
    x =[]
# %%
# %%
y
# %%
