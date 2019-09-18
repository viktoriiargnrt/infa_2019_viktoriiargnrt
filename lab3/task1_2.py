from graph import*
penColor('purple')
rectangle(0,0,500,400)
brushColor(204,255,255)
rectangle(0,0,500,200)
brushColor(0,0,102)
rectangle(0,200,500,300)
penColor(255,204,0)
brushColor(255,204,0)
circle(400,100,50)
rectangle(0,300,500,400)
n=13
r=500/(n*2)
x=r
for i in range (n):
	circle(x,310,r)
	x+=2*r
penColor(102,51,0)
penSize(5)
line(50,330,50,390)
run()
