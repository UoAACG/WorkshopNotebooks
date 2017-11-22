import pyPLUTO as pp
import numpy as np
import os
import sys
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt


t0=1000000000.0
second_to_yrs=3.17e-8
cwd=os.getcwd()
wdir=cwd+'/'
outdir=cwd[cwd.rfind('/')+1:]
print wdir,outdir
nlinf = pp.nlast_info(w_dir=wdir)
D=pp.pload(0,w_dir=wdir)
PRS=D.prs
RHO=D.rho
X=D.x1
Y=D.x2
Vx=D.vx1
Vy=D.vx2 if 'vx2' in D.vars else 0.
Bx=D.bx1 if 'bx1' in D.vars else 0.
By=D.bx2 if 'bx2' in D.vars else 0.
x_HI=D.X_HI if 'X_HI' in D.vars else 0.
x_HII=D.X_HII if 'X_HII' in D.vars else 0 
x_H2=D.X_H2 if 'X_H2' in D.vars else 0 
T=D.SimTime
print nlinf
for t in range(1,nlinf['nlast']+1):
	D=pp.pload(t,w_dir=wdir)
	PRS=np.dstack((PRS,D.prs))
	RHO=np.dstack((RHO,D.rho))
	Vx=np.dstack((Vx,D.vx1))
	Vy=np.dstack((Vy,D.vx2))
	Bx=np.dstack((Bx,D.bx1)) if 'bx1' in D.vars else 0.
	By=np.dstack((By,D.bx2)) if 'bx2' in D.vars else 0.
	x_HI=np.dstack((x_HI,D.X_HI)) if 'X_HI' in D.vars else 0.
	x_HII=np.dstack((x_HII,D.X_HII)) if 'X_HII' in D.vars else 0.
	x_H2=np.dstack((x_H2,D.X_H2)) if 'X_H2' in D.vars else 0.
	T=np.append(T,D.SimTime)
	
np.savez_compressed(outdir,RHO=RHO,PRS=PRS,Vx=Vx,Vy=Vy,Bx=Bx,By=By,X=X,Y=Y,x_HI=x_HI,x_HII=x_HII,x_H2=x_H2,T=T*t0*second_to_yrs)

Temper = PRS*10891304347826.088/RHO
print RHO.min(),RHO.max()
print PRS.min(),PRS.max()
print Temper.min(),Temper.max()
#################################################################
#Temp0=10891304347826.088
#VAR=np.log10(PRS*Temp0/RHO) #Temperature
#VAR=np.log10(np.copy(RHO)) #RHO
#VAR=2.0*x_H2+x_HI+x_HII #SUM
#VAR=x_HI+x_HII 
#VAR=2.0*x_H2
#VAR=np.log10(RHO)
def quad(VAR,Save_Figure,cl='',rows=2,cols=2,nn=0,tdk='kyrs'):

	TT=np.linspace(0,T.shape[0]-1,rows*cols,dtype=int)
	fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=True, sharey=True,
		            figsize=(cols*5,rows*5))
	i=0
	td=1e3 if tdk=='kyrs' else 1e6 if tdk=='Myrs' else 1.
	for ax in axes.flat:
		ext=[X.min(),X.max(),Y.min(),Y.max()]
		ax.get_yaxis().get_major_formatter().set_useOffset(False)
		ax.add_artist(plt.Circle((0, 0), 1.0, color='r',fill=False,linestyle='--'))
		label = '{:.1f} {}'.format(T[TT[i]]/td,tdk)
		ax.set_title(label,fontsize=20)
		ax.grid(False)
		pc = ax.imshow(VAR[:,:,TT[i]].T,cmap='viridis',origin='lower',aspect='equal',
			       extent=ext,vmin=VAR.min(),vmax=VAR.max())
		if nn>0:
		    k=nn #distance from boundaries for first/last arrows
		    q=pc.axes.quiver(X[k:-k:nn],Y[k:-k:nn],
				    Vx[:,:,TT[i]][k:-k:nn,k:-k:nn].T,
				    Vy[:,:,TT[i]][k:-k:nn,k:-k:nn].T,
				     scale=1e-4,alpha=0.5,width=0.002)
		    pc.axes.quiverkey(q,0.02,1.02,3.36e-6,r'$1\si{km.s^{-1}}$',labelpos='E',
			   fontproperties={'weight': 'bold'})
		i=i+1
	plt.tight_layout()
	cbar_ax = fig.add_axes([0., 1.015, 1., 0.025*(np.float(cols)/rows)])#*(np.float(cols)/rows)
	cb=fig.colorbar(pc, cax=cbar_ax,orientation="horizontal",label=cl)
	cb.ax.tick_params(labelsize=17)
	cb.ax.xaxis.offsetText.set(size=20)
	cb.ax.xaxis.set_ticks_position('top')
	cb.ax.xaxis.set_label_position('top')
	fig.savefig(Save_Figure,bbox_inches='tight')

quad(np.log10(RHO),'RHO',rows=4,tdk='yrs')
quad(np.log10(PRS),'PRS')
quad(2.0*x_H2+x_HI+x_HII ,'sum')
quad(2.0*x_H2,'H2')
quad(x_HI,'HI')
quad(x_HII,'HII')
quad(np.log10(Temper),'Temperature')
