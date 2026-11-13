import json as J,os as O,sys as Y,urllib.request as R,base64 as B
Y.setrecursionlimit(10000)
U=O.environ.get("MAKEFUN_ENV_URL")or Y.exit("no env")
T=[x-128 for x in B.b85decode(b"fPjF2fPjF2g^G%7Y>JA7g?n~@fOdO@fPjFMlz@PMg@uZlnTmylii(t;o|KA;va+(Wva+(WfPjF2fPjF2PFP}MVq#cMSZsiRfPidRVugy2kBWt2Vt|j7l#hU7Vug>Cl#hjCVt|T|kBWd|SZsiRfPidRPFP}MVq#cMY<6~bc6N4bc7=d|fPjT|c8ZFMii(PMc7TeCii&`Cc7=tCiiL%Cc7TP7iiLo7c7T9@fPjE@Y<6~bc6N4bfPjF7g@Ay7dw_s|fPjE|dw_s|fPjE|dw_s|fPjE|dw_s|fPjE|dw_s|fPjE|g^G%bii(PbfPjF2fPjF2Y<6~gdv<ngc7TO|fPjE@c7=t7g@u52fPjUCg@u57dw_+7g@u57c7TP2g@u52c7T9@fPjE@Y<6~gdv<ngl%9%!fQp`!l$3ygfPj>gc5G~HY;0_HY+_<qSYl#qVpv#CPFPrCVpv#CPFPrCVpv#CPFPrCVpv#CPFPrCPGVwWVq#)WVq$=RfPi9RVs@0Co|JZCVs@UWsGfFWVs@UWsGfFWVs@0Co|JZCVr+JRfOc$RPFP}WY+_hW")]
V=(100,320,330,500,900,0)
KN=(31,33,14,18,-31,-33,-14,-18)
KG=(1,16,-1,-16,15,17,-15,-17)
DG=KG[4:]
RT=KG[:4]
SQ=tuple(s for s in range(128)if not s&0x88)
MA=100000
b=bytearray(128)
sd=1
ca=0
ep=-1
hf=0
WK=4
BK=116
nd=0
TT={}
KI=[[0,0]for _ in range(128)]
HI=[0]*1664
PH=[]
def uc(m):
 s="abcdefgh"[m&7]+str(((m&127)>>4)+1)+"abcdefgh"[(m>>7)&7]+str((((m>>7)&127)>>4)+1)
 p=(m>>14)&7
 return s+("","","n","b","r","q")[p]if p else s
def pf(f):
 global sd,ca,ep,hf,WK,BK
 q=f.split()
 b[:]=[0]*128
 r=7
 f2=0
 mp=" PNBRQKpnbrqk".index
 for c in q[0]:
  if c=="/":
   r-=1
   f2=0
  elif c.isdigit():
   f2+=int(c)
  else:
   b[r*16+f2]=mp(c)
   if mp(c)==6:
    WK=r*16+f2
   elif mp(c)==12:
    BK=r*16+f2
   f2+=1
 sd=1-2*(q[1]!="w")
 ca=0
 for i in range(4):
  if "KQkq"[i] in q[2]:
   ca|=1<<i
 ep=-1 if q[3]=="-"else(int(q[3][1])-1)*16+ord(q[3][0])-97
 hf=int(q[4])
def at(s,w):
 for d in(-15,-17)if w else(15,17):
  t=s+d
  if not t&0x88 and b[t]==(1 if w else 7):
   return True
 for d in KN:
  t=s+d
  if not t&0x88 and b[t]==(2 if w else 8):
   return True
 for d in KG:
  t=s+d
  if not t&0x88 and b[t]==(6 if w else 12):
   return True
 for d in DG:
  t=s+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==(3 if w else 9)or p==(5 if w else 11):
     return True
    break
   t+=d
 for d in RT:
  t=s+d
  while not t&0x88:
   p=b[t]
   if p:
    if p==(4 if w else 10)or p==(5 if w else 11):
     return True
    break
   t+=d
 return False
def gn(cp=False):
 ms=[]
 w=sd==1
 for s in SQ:
  p=b[s]
  if not p or(p<=6)!=w:
   continue
  t=(p-1)%6
  if t==0:
   d=16 if w else-16
   t1=s+d
   if not b[t1]:
    r=t1>>4
    if r==(7 if w else 0):
     for pr in(2,3,4,5):
      ms.append(s|(t1<<7)|(pr<<14))
    elif not cp:
     ms.append(s|(t1<<7))
     if(s>>4)==(1 if w else 6):
      t2=s+2*d
      if not b[t2]:
       ms.append(s|(t2<<7)|(2<<17))
   for dd in(d-1,d+1):
    t1=s+dd
    if t1&0x88:
     continue
    q=b[t1]
    if q and(q<=6)!=w:
     r=t1>>4
     if r==(7 if w else 0):
      for pr in(2,3,4,5):
       ms.append(s|(t1<<7)|(pr<<14))
     else:
      ms.append(s|(t1<<7))
    elif t1==ep:
     ms.append(s|(t1<<7)|(1<<17))
  elif t==1:
   for d in KN:
    t1=s+d
    if t1&0x88:
     continue
    q=b[t1]
    if q:
     if(q<=6)!=w:
      ms.append(s|(t1<<7))
    elif not cp:
     ms.append(s|(t1<<7))
  elif t in(2,3,4):
   ds=DG if t==2 else RT if t==3 else KG
   for d in ds:
    t1=s+d
    while not t1&0x88:
     q=b[t1]
     if q:
      if(q<=6)!=w:
       ms.append(s|(t1<<7))
      break
     if not cp:
      ms.append(s|(t1<<7))
     t1+=d
  else:
   for d in KG:
    t1=s+d
    if t1&0x88:
     continue
    q=b[t1]
    if q:
     if(q<=6)!=w:
      ms.append(s|(t1<<7))
    elif not cp:
     ms.append(s|(t1<<7))
   if not cp:
    k=ks(w)
    if s==k:
     if w:
      if ca&1 and not b[5]and not b[6]and b[7]==4 and not at(4,0)and not at(5,0)and not at(6,0):
       ms.append(s|(6<<7)|(4<<17))
      if ca&2 and not b[3]and not b[2]and not b[1]and b[0]==4 and not at(4,0)and not at(3,0)and not at(2,0):
       ms.append(s|(2<<7)|(8<<17))
     else:
      if ca&4 and not b[117]and not b[118]and b[119]==10 and not at(116,1)and not at(117,1)and not at(118,1):
       ms.append(s|(118<<7)|(4<<17))
      if ca&8 and not b[115]and not b[114]and not b[113]and b[112]==10 and not at(116,1)and not at(115,1)and not at(114,1):
       ms.append(s|(114<<7)|(8<<17))
 return ms
def ks(w):
 return WK if w else BK
def mk(m):
 global sd,ca,ep,hf,WK,BK
 s=m&127
 t=(m>>7)&127
 p=(m>>14)&7
 f=(m>>17)&15
 pc=b[s]
 cp=b[t]
 oep=ep
 ohf=hf
 b[t]=pc
 b[s]=0
 if pc==6:
  WK=t
 elif pc==12:
  BK=t
 if p:
  b[t]=p+1 if sd==1 else p+7
 if f==1:
  b[t+(-16 if sd==1 else 16)]=0
 elif f==2:
  ep=s+((16 if sd==1 else-16))
 else:
  ep=-1
 if f==4:
  b[t-1]=b[t+1]
  b[t+1]=0
 elif f==8:
  b[t+1]=b[t-2]
  b[t-2]=0
 oc=ca
 ca&=~((1 if s==7 else 0)|(2 if s==0 else 0)|(4 if s==119 else 0)|(8 if s==112 else 0)|(1 if t==7 else 0)|(2 if t==0 else 0)|(4 if t==119 else 0)|(8 if t==112 else 0)|(3 if s==4 else 0)|(12 if s==116 else 0))
 hf=0 if cp or(pc%6)==1 else hf+1
 sd=-sd
 return(pc,cp,oc,oep,f,ohf)
def un(m,u):
 global sd,ca,ep,hf,WK,BK
 pc,cp,oc,oep,f,ohf=u
 s=m&127
 t=(m>>7)&127
 p=(m>>14)&7
 sd=-sd
 ca=oc
 hf=ohf
 b[s]=pc
 b[t]=cp
 if pc==6:
  WK=s
 elif pc==12:
  BK=s
 if f==1:
  b[t+(-16 if sd==1 else 16)]=7 if sd==1 else 1
 elif f==4:
  b[t+1]=b[t-1]
  b[t-1]=0
 elif f==8:
  b[t-2]=b[t+1]
  b[t+1]=0
 ep=oep
def ev():
 s=0
 ph=0
 wb=0
 bb=0
 kmg=0
 keg=0
 for q in SQ:
  p=b[q]
  if not p:
   continue
  t=(p-1)%6
  w=p<=6
  i=(q&7)+((q>>4)<<3)
  j=(q&7)+((7-(q>>4))<<3)
  if t==5:
   kmg+= T[320+i] if w else -T[320+j]
   keg+= T[384+i] if w else -T[384+j]
   continue
  v=V[t]+T[t*64+i if w else t*64+j]
  s+= v if w else -v
  if t:
   ph+= (1 if t in(1,2)else 2 if t==3 else 4)
   if t==2:
    if w:
     wb+=1
    else:
     bb+=1
 if ph>24:
  ph=24
 s+=(kmg*ph+keg*(24-ph))//24
 if wb>1:
  s+=30
 if bb>1:
  s-=30
 return s if sd==1 else -s
def key():
 return(bytes(b),sd,ca,ep)
def qs(a,be,ply):
 global nd
 nd+=1
 if nd>MA:
  raise TimeoutError
 if ply>64:
  return ev()
 w=sd==1
 inch=at(ks(w),not w)
 st=ev()
 if not inch:
  if st>=be:
   return be
  if st>a:
   a=st
 else:
  a=-99999
 ms=gn(False) if inch else gn(True)
 ms.sort(key=lambda m:-(V[(b[(m>>7)&127]-1)%6]*10-V[(b[m&127]-1)%6] if b[(m>>7)&127] else 0))
 fd=False
 for m in ms:
  if not inch and not b[(m>>7)&127] and not((m>>14)&7):
   continue
  u=mk(m)
  if at(ks(w),not w):
   un(m,u)
   continue
  fd=True
  sc=-qs(-be,-a,ply+1)
  un(m,u)
  if sc>=be:
   return be
  if sc>a:
   a=sc
 if inch and not fd:
  return -99990+ply
 return a
BM=0
def sr(a,be,d,ply):
 global nd,BM,sd,ep
 if d<=0:
  return qs(a,be,ply)
 nd+=1
 if nd>MA:
  raise TimeoutError
 k=key()
 e=TT.get(k)
 if e and e[0]>=d:
  if ply==0 and e[3]:
   BM=e[3]
  if e[1]==0:
   return e[2]
  if e[1]==1 and e[2]>=be:
   return be
  if e[1]==2 and e[2]<=a:
   return a
 w=sd==1
 inch=at(ks(w),not w)
 if inch:
  d+=1
 elif d>=3:
  s0=sd
  e0=ep
  sd=-sd
  ep=-1
  sc=-sr(-be,-be+1,d-3,ply+1)
  sd=s0
  ep=e0
  if sc>=be:
   return be
 ms=gn()
 if not ms:
  return -99990+ply if inch else 0
 tt=e[3] if e else 0
 def ord(m):
  c=b[(m>>7)&127]
  if m==tt:
   return -1000000
  if c:
   return -(900000+V[(c-1)%6]*10-V[(b[m&127]-1)%6])
  if m==KI[ply][0] or m==KI[ply][1]:
   return -800000
  return -HI[(b[m&127]*128)+((m>>7)&127)]
 ms.sort(key=ord)
 best=-99999
 bm=0
 fl=2
 n=0
 for m in ms:
  c=b[(m>>7)&127]
  u=mk(m)
  if at(ks(w),not w):
   un(m,u)
   continue
  rk=key()
  rep=rk in PH or rk in RP
  if rep:
   sc=0
   un(m,u)
   if sc>=be:
    return be
   if sc>best:
    best=sc
    bm=m
   continue
  RP.append(rk)
  if n==0:
   sc=-sr(-be,-a,d-1,ply+1)
  else:
   rd=d-2 if d>=3 and n>=4 and not c and not((m>>14)&7) else d-1
   sc=-sr(-a-1,-a,rd,ply+1)
   if sc>a and sc<be:
    sc=-sr(-be,-a,d-1,ply+1)
  RP.pop()
  un(m,u)
  if sc>=be:
   if not c:
    KI[ply][1]=KI[ply][0]
    KI[ply][0]=m
    HI[(b[m&127]*128)+((m>>7)&127)]+=d*d
   TT[k]=(d,1,be,m)
   if ply==0:
    BM=m
   return be
  if sc>best:
   best=sc
   bm=m
   if ply==0:
    BM=m
   if sc>a:
    a=sc
    fl=0
  n+=1
 if best<=-99999:
  return -99990+ply if inch else 0
 TT[k]=(d,fl,best,bm)
 return best
RP=[]
def rt():
 global nd
 bm=0
 nd=0
 RP.clear()
 for d in range(1,64):
  try:
   sc=sr(-99999,99999,d,0)
  except TimeoutError:
   break
  if sc>-99990:
   bm=BM
 return bm
def post(p,bo):
 q=R.Request(U+p,data=J.dumps(bo).encode(),headers={"content-type":"application/json"})
 try:
  with R.urlopen(q)as r:
   return J.load(r)
 except Exception as e:
  Y.exit(str(e))
cg=0
while True:
 g=post("/game",{})
 if g["status"]=="done":
  break
 if g["game"]!=cg:
  cg=g["game"]
  TT.clear()
  PH.clear()
  RP.clear()
 while g["status"]=="your_move":
  pf(g["fen"])
  PH.append(key())
  m=rt()
  u=uc(m) if m else ""
  if not m or u not in g["legal_moves"]:
   lg=g["legal_moves"]
   m=0
   # fallback: first legal move, convert UCI to internal encoding
   u=lg[0]
   f="abcdefgh".index(u[0])+("12345678".index(u[1]))*16
   t="abcdefgh".index(u[2])+("12345678".index(u[3]))*16
   pr={"n":2,"b":3,"r":4,"q":5}.get(u[4],0) if len(u)==5 else 0
   m=f|(t<<7)|(pr<<14)
   # detect ep/double/castle flags for the fallback move
   pc=b[f]
   if(pc%6)==1 and abs(t-f)==32:
    m|=2<<17
   elif(pc%6)==1 and t==ep:
    m|=1<<17
   elif(pc%6)==6 and abs(t-f)==2:
    m|= (4<<17) if t>f else (8<<17)
  g=post("/move",{"game":g["game"],"move":uc(m)})
 print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=Y.stderr)
print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=Y.stderr)
