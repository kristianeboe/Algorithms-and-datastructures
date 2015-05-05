values = [12,10,20,15]
weights = [2,1,3,3]
number_of_items = 4
capacity = 5

for j in range(capacity):
    m[0,j] = 0
for i in range(1,number_of_items):
    for j in range(capacity):
        if w[i] <= j:
            m[i,j] = max(m[i-1, j], m[i-1, j-w[i] + v[i]])
        else:
            m[i,j] = m[i-1,j]
