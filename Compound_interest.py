p,r,t=map(int,input().split())
a=p*pow((1+r/100.0),t)
print(F"{a:.2f}")