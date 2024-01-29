from tkinter import *
from random import *
class S:
    def __init__(s,m,c=600,e=30):s.m=m;s.c=c;s.e=e;s.p=10;s.a=Canvas(s.m,width=c,height=c);s.a.pack();s.n=[(300,300),(270,300),(240,300)];s.k=set(s.n);s.i="Right";s.x="Right";s.f=s.r();s.m.bind("<Key>",s.h);s.u()
    def r(s):
        if hasattr(s,"f"):s.a.delete("f")
        y=set((x,y)for x in range(0,s.c,s.e)for y in range(0,s.c,s.e))-s.k;d=choice(list(y));f=(d[0],d[1]);s.a.create_rectangle(f[0],f[1],f[0]+s.p,f[1]+s.p,fill="red",tags="f");return f
    def h(s,v):
        K=v.keysym;D={"Up":"Down","Down":"Up","Left":"Right","Right":"Left"}
        if K in D and s.i!=D[K]:s.x=K
    def M(s):
        H=s.n[0];D={"Up":(0,-s.p),"Down":(0,s.p),"Left":(-s.p,0),"Right":(s.p,0)};w=(H[0]+D[s.i][0],H[1]+D[s.i][1])
        if not(0<=w[0]<s.c)or not(0<=w[1]<s.c)or w in s.k:s.m.destroy();return
        s.n.insert(0,w);s.k.add(w)
        if w==s.f:s.f=s.r()
        else:T=s.n.pop();s.k.remove(T);s.a.delete("s")
        for g in s.n:s.l(g,fill="green",tags="s")
    def l(s,C,fill,tags):x,y=C;s.a.create_rectangle(x,y,x+s.p,y+s.p,fill=fill,tags=tags)
    def u(s):s.i=s.x;s.M();s.m.after(100,s.u)
O=Tk();G=S(O);O.mainloop()