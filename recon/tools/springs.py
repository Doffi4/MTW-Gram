# Sample CASpringAnimation / damped-spring curves used by Telegram macOS, for porting to Qt anim::.
import math
def ca_spring(m,k,c,v0=0.0,dt=1e-4,T=1.5):
    x,v,t=0.0,v0,0.0; out=[]
    while t<=T:
        out.append((t,x)); a=(-k*(x-1)-c*v)/m; v+=a*dt; x+=v*dt; t+=dt
    return out
def settle(samples,eps=0.001):
    last=0
    for t,x in samples:
        if abs(1-x)>eps: last=t
    return last
def bez(p1x,p1y,p2x,p2y,t):
    def bx(s): return 3*(1-s)**2*s*p1x+3*(1-s)*s*s*p2x+s**3
    def by(s): return 3*(1-s)**2*s*p1y+3*(1-s)*s*s*p2y+s**3
    lo,hi=0.0,1.0
    for _ in range(50):
        mid=(lo+hi)/2
        if bx(mid)<t: lo=mid
        else: hi=mid
    return by((lo+hi)/2)
def at(s,t):
    for tt,x in s:
        if tt>=t: return x
    return s[-1][1]
specs={
 'spring (.spring curve) m3 k1000 c500':(3,1000,500),
 'springBounce m5 k900 c88':(5,900,88),
 'textSendVertical m1 k272 c33':(1,272,33),
 'sendButtonField m1 k555.027 c47.118':(1,555.027,47.118),
 'switch response0.47 ζ0.7':(1,(2*math.pi/0.47)**2,2*0.7*2*math.pi/0.47),
}
print('| spring | ω0 | ζ | settle(0.1%) s | x@25% of 0.5s | x@50% | x@75% | x@100% (0.5s) |')
print('|---|---|---|---|---|---|---|---|')
for n,(m,k,c) in specs.items():
    s=ca_spring(m,k,c); w=math.sqrt(k/m); z=c/(2*math.sqrt(k*m))
    print(f'| {n} | {w:.2f} | {z:.3f} | {settle(s):.3f} | {at(s,0.125):.3f} | {at(s,0.25):.3f} | {at(s,0.375):.3f} | {at(s,0.5):.3f} |')
print()
s=ca_spring(3,1000,500)
print('Сравнение `.spring` (CASpring m3/k1000/c500, проигрывается за 0.5 s и масштабируется speed=0.5/duration) с bezier(0.23,1,0.32,1):\n')
print('| t/T | CASpring | bezier(0.23,1,0.32,1) | easeOut(0,0,0.58,1) | easeInOut(0.42,0,0.58,1) |\n|---|---|---|---|---|')
for i in range(0,11):
    f=i/10
    print(f'| {f:.1f} | {at(s,0.5*f):.3f} | {bez(0.23,1,0.32,1,f):.3f} | {bez(0,0,0.58,1,f):.3f} | {bez(0.42,0,0.58,1,f):.3f} |')
