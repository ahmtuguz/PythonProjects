import matplotlib.pyplot as plt
import numpy as np

# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.plot(x,y,color="orange",linewidth="3")
# plt.plot(x,y,"o-r")
# plt.axis((0,6,0,20))
# plt.title("Title")
# plt.xlabel("x label")
# plt.ylabel("y label")
# x=np.linspace(0,2,100)
# plt.plot(x,x,label="linear",color="black")
# plt.plot(x,x**2,label="quadratic",color="orange")
# plt.plot(x,x**3,label="cubic",color="purple")
# plt.title("Title")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.legend()
#
# plt.show()

# x=np.linspace(0,2,100)
# fig,axs =plt.subplots(3)
# axs[0].plot(x,x)
# axs[1].plot(x,x**2,color="purple")
# axs[2].plot(x,x**3,color="green")
#
# axs[0].set_title("linear")
# axs[1].set_title("quadratic")
# axs[2].set_title("cubic")
#
# plt.tight_layout()
#
# plt.show()

# x=np.linspace(0,2,100)
# fig,axs =plt.subplots(2,2)
#fig,(axs1,axs2)=plt.subplots(nrows=2,ncols=1,figsize=(8,8))
#fig.savefig("figure1.png")
# plt.suptitle("title")
# axs[0,0].plot(x,x)
# axs[0,1].plot(x,x**2,color="purple")
# axs[1,0].plot(x,x**3,color="green")
# axs[1,1].plot(x,x**4,color="yellow")
#
# axs[0,0].set_title("linear")
# axs[0,1].set_title("quadratic")
# axs[1,0].set_title("cubic")
# axs[1,1].set_title("dada")
#
# plt.tight_layout()
#
# plt.show()

x=np.linspace(0,2,100)
y=x**3
z=x**2

figure=plt.figure()
axes=figure.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x,y,"b")
axes.set_xlabel("x label")
axes.set_ylabel("y label")
axes.set_title("title")

axes2=figure.add_axes([0.15, 0.6, 0.25, 0.25])
axes2.plot(x,z,"r",label="quadratic")
axes2.set_xlabel("x label")
axes2.set_ylabel("y label")
axes2.set_title("title")
plt.legend(loc=4)

plt.show()

