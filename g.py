
import numpy as np

# Falling = 1
# Standing = 2
# Moving = 3

# Value function = 3 x T 
T=None
gamma = 0.9

P = np.zeros((3,3,3))


P[0][0][0] = 0.6
P[0][1][0] = 0.4
P[1][2][0] = 1
P[1][2][1] = 0.6
P[1][2][0] = 0.4
P[2][2][1] = 0.8
P[2][0][1] = 0.2
P[2][1][0] = 1

r = np.zeros((3,3,3))

r[0][0][0] = -1
r[0][1][0] = 1
r[1][2][0] = 1
r[1][2][1] = 1
r[1][2][0] = -1
r[2][2][1] = 2
r[2][0][1] = -1
r[2][1][0] = 1


# 0 represents slow, 1 represents fast
PI_b = [[0],[1],[1]]*T
PI_c = [[0],[0],[1]]*T



V_vec  = np.zeros((3,T+1))

for t in reversed(range(T)):
    for i in range(3):
        V = 0
        for j in range(3):
            a = PI_b[i][t]
            n = (r[i,j,a])+gamma*(V_vec[j,t+1])
            m = P[i,j,a]
            V = V + m*n
        V_vec[i][t] = V

V_b = V_vec

V_vec  = np.zeros((3,T+1))


for t in reversed(range(T)):
    for i in range(3):
        V = 0
        for j in range(3):
            a = PI_c[i][t]
            n = (r[i,j,a])+gamma*(V_vec[j,t+1])
            m = P[i,j,a]
            V = V + m*n
        V_vec[i][t] = V

V_c = V_vec

if V_b > V_c:
    print("Policy B is more succesfull")
else:
    print("Policy C is more succesfull")
        
