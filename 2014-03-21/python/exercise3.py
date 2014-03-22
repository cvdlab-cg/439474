from pyplasm import *

x_firststep=QUOTE([33])
Y_firststep=QUOTE([68])
firststep=PROD([x_firststep,Y_firststep])

x_secondstep=QUOTE([-1.5,30])
Y_secondstep=QUOTE([-1.5,65])
secondstep=PROD([x_secondstep,Y_secondstep])

x_thirdstep=QUOTE([-3,27])
Y_thirdstep=QUOTE([-3,62])
thirdstep=PROD([x_thirdstep,Y_thirdstep])

step=STRUCT([firststep,secondstep,thirdstep])

def circle(r):
	def circle0(p):
		alpha = p[0]
		return [r*COS(alpha), r*SIN(alpha)]
	return circle0

culomnbase = T([1,2])([4,4])(MAP(circle(1))(INTERVALS(2*PI)(20)))

#queste righe successive servono per fare una colonna
culomnpic=T([1,2,3])([4,4,10])(MAP(circle(0.7))(INTERVALS(2*PI)(20)))
culomngra=T([1,2,3])([4,4,10.5])(MAP(circle(1))(INTERVALS(2*PI)(360)))
c1=JOIN([culomnpic,culomnbase])
c2=JOIN([culomnpic,culomngra])
x_cubo=PROD([Q(2),Q(2)])
cubo=T([1,2,3])([3,3,10.5])(PROD([x_cubo,Q(0.4)]))

colonna=STRUCT([c1,c2,cubo])

trasl = [T([1,2])([5,0]),culomnbase]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),culomnbase]
colonnato2 = STRUCT(NN(12)(trasl2))

culomnbase2=T([1,2])([25,0])(culomnbase)
trasl3 = [T([1,2])([0,5]),culomnbase2]
colonnato3 = STRUCT(NN(12)(trasl3))

culomnbase3=T([1,2])([0,60])(culomnbase)
trasl4 = [T([1,2])([5,0]),culomnbase3]
colonnato4 = STRUCT(NN(5)(trasl4))
col5=T([1,2])([10,7.5])(culomnbase)
col6=T([1,2])([15,7.5])(culomnbase)
col7=T([1,2])([10,52.5])(culomnbase)
col8=T([1,2])([15,52.5])(culomnbase)

y_r1=QUOTE([-10.5,47])
x_r1=QUOTE([-10,1])
xy=PROD([x_r1,y_r1])
xy2=T(1)(12)(xy)

y_r2=QUOTE([-18.5,1])
x_r2=QUOTE([-11,11])
xy3=PROD([x_r2,y_r2])

y_r3=QUOTE([-47,4])
x_r3=QUOTE([-11,4,-3,4])
xy4=PROD([x_r3,y_r3])

tetto=STRUCT([xy2,xy3,xy4,xy])

colcentr=STRUCT([col5,col6,col7,col8])

ctot1=STRUCT([step,tetto,colcentr])
	
ctot=STRUCT([colonnato,colonnato2,culomnbase,step,colonnato3,colonnato4,colcentr,tetto])	

firststep=PROD([firststep,Q(1)])
secondstep=PROD([secondstep,Q(2)])
thirdstep=PROD([thirdstep,Q(3)])
step=STRUCT([firststep,secondstep,thirdstep])

trasl =[T([1,2])([5,0]), colonna]
colonnato = STRUCT(NN(5)(trasl))

trasl2 = [T([1,2])([0,5]),colonna]
colonnato2 = STRUCT(NN(12)(trasl2))

colonna2=T([1,2])([25,0])(colonna)
trasl3 = [T([1,2])([0,5]),colonna2]
colonnato3 = STRUCT(NN(12)(trasl3))

colonna3=T([1,2])([0,60])(colonna)
trasl4 = [T([1,2])([5,0]),colonna3]
colonnato4 = STRUCT(NN(5)(trasl4))
col5=T([1,2])([10,7.5])(colonna)
col6=T([1,2])([15,7.5])(colonna)
col7=T([1,2])([10,52.5])(colonna)
col8=T([1,2])([15,52.5])(colonna)
colonnati=STRUCT([colonnato,colonnato2,colonna,step,colonnato3,colonnato4,col5,col6,col7,col8])

tetto=PROD([tetto,Q(10.9)])

p1 = MAP(circle(1.175))(INTERVALS(PI)(32))
p1=PROD([Q(1),p1])
p1=T(2)(1.175)(p1)
c=CUBOID([1,1.175,0])
s=JOIN([c,p1])
s=T(3)(4.275)(s)
c1=CUBOID([1,2.35,4.275])
ss=T([1,2])([10,17.5])(STRUCT([s,c1]))
ss=T(3)(3)(STRUCT(NN(6)([T(2)(4),ss])))
ss2=T(1)(12)(ss)

tetto=DIFF([tetto,ss,ss2])

#cornicione
x_matt1=QUOTE([26.5])
y_matt1=QUOTE([1.5])
matt1=PROD([x_matt1,y_matt1])
matt1=PROD([matt1,Q(1.2)])
x_matt2=QUOTE([1.5])
y_matt2=QUOTE([61.5])
matt2=PROD([x_matt2,y_matt2])
matt2=PROD([matt2,Q(1.2)])
cornice=STRUCT([matt1,matt1])
matt3=T([1,2])([0,60])(matt1)
matt4=T([1,2])([25,0])(matt2)
cornicione=STRUCT([matt1,matt2,matt3,matt4])
cornicione=T([1,2,3])([3.25,3.25,10.9])(cornicione)

x_bord1=QUOTE([26.75])
y_bord1=QUOTE([1.75])
bord1=PROD([x_bord1,y_bord1])
bord1=PROD([bord1,Q(0.3)])
x_bord2=QUOTE([1.75])
y_bord2=QUOTE([61.75])
bord2=PROD([x_bord2,y_bord2])
bord2=PROD([bord2,Q(0.3)])
bordino=STRUCT([bord1,bord1])
bord3=T([1,2])([0,60])(bord1)
bord4=T([1,2])([25,0])(bord2)
bordoncino=STRUCT([bord1,bord2,bord3,bord4])
bordoncino=T([1,2,3])([3.125,3.125,12.2])(bordoncino)

x_cfront1=QUOTE([26.5])
y_cfront1=QUOTE([1.5])
cfront1=PROD([x_cfront1,y_cfront1])
cfront1=PROD([cfront1,Q(1.5)])
cfront1=T([1,2,3])([3.25,3.25,12.5])(cfront1)
cfront2=T(2)(60)(cfront1)
front=STRUCT([cfront1,cfront2])

x_bord3=QUOTE([26.75])
y_bord3=QUOTE([1.75])
bord3=PROD([x_bord3,y_bord3])
bord3=PROD([bord3,Q(0.3)])
bordoncino2=T([1,2,3])([3.125,3.125,13.7])(bord3)
bordoncino3=T(2)(60)(bordoncino2)

#triangolo

base=CUBOID([27,2.5,0.5])
l1=CUBOID([13.5/COS(PI/9),2.5,0.5])
l2=R([1,3])(7*PI/18+PI/2)(l1)
l1=R([1,3])(PI/9)(l1)
l1=T(1)(0.5*COS(7*PI/18))(l1)
l2=T([1,3])([27,0.5])(l2)
triangolo=JOIN([base,l1,l2])
triangolo=T([1,2,3])([3.125,2.75,14])(triangolo)

t2=S([1,2,3])([0.9,0.4,0.9])(triangolo)
t2=T([1,2,3])([1.6,1.6,1.6])(t2)

t=DIFF([triangolo,t2])
t2=T(2)(62)(t2)
triangolo2=T(2)(60)(triangolo)
triangolo2=DIFF([triangolo2,t2])

primocubo=CUBOID([13,1,1.8])
secondocubo=T([1,3])([1.2,1.8])(CUBOID([10.6,1,1.6]))
terzocubo=T([1,3])([2.05,3.4])(CUBOID([8.9,1,0.7]))
quartocubo=T([1,3])([4.8,4.1])(CUBOID([3.4,1,1.2]))
buco=T([1,3])([5.9,1.8])(CUBOID([1.2,1,1.6]))
secondocubo=DIFF([secondocubo,buco])

x=PROD([Q(2),Q(2)])
cc=T([1,2,3])([9.5,10.5,10.5])(PROD([x,Q(0.4)]))
cc2=T(1)(12)(cc)
cc3=T(2)(45)(cc)
cc4=T(2)(45)(cc2)
cap=STRUCT([cc,cc2,cc3,cc4])
cubi=STRUCT([primocubo,secondocubo,terzocubo,quartocubo])
cubi=T([1,2,3])([10,11,10.9])(cubi)
cubi2=T(2)(45)(cubi)

VIEW(STRUCT([cap,colonnati,tetto,cornicione,bordoncino,front,bordoncino2,bordoncino3,t,triangolo2,cubi,cubi2]))