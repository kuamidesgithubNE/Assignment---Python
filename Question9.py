def compute_hcf(x,y):
     while(y):
        x,y = y, x % y
     return x
hcf = compute_hcf(54, 24)

print("The H.C.F is " , hcf)
