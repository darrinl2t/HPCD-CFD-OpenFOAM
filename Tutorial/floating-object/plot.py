import pandas as pd
import matplotlib.pyplot as plt

mm = 1/25.4
timeDir = 'postProcessing/sixDoF_History/0'
outName = 'sixDoF_History.png'
inp = timeDir + '/sixDoFRigidBodyState.dat'

dfCFD = pd.read_csv(inp, delimiter = ' ', header = None, skip_blank_lines = False,skiprows=3)
dfCFD.columns =['Time','centreOfRotationX','centreOfRotationY','centreOfRotationZ','centreOfMassX','centreOfMassY','centreOfMassZ', 'rotationX','rotationY','rotationZ','velocityX','velocityY','velocityZ','omegaX','omegaY','omegaZ']


t = dfCFD['Time'].values
surge = dfCFD['centreOfMassX'].values
sway = dfCFD['centreOfMassY'].values
heave = dfCFD['centreOfMassZ'].values
roll = dfCFD['rotationX'].values
pitch = dfCFD['rotationY'].values
yaw = dfCFD['rotationZ'].values

fig, axs = plt.subplots(3, 2,figsize=(250*mm,200*mm))
axs[0, 0].plot(t, surge,'black')
axs[0, 0].set(ylabel='Surge (m)')
axs[0, 0].set_ylim(-0.15,0.15)
axs[1, 0].plot(t, sway, 'tab:purple')
axs[1, 0].set(ylabel='Sway (m)')
axs[1, 0].set_ylim(-0.1,0.1)
axs[2, 0].plot(t, heave, 'tab:green')
axs[2, 0].set(ylabel='Heave (m)')
axs[2, 0].set_ylim(-0.1,0.1)


axs[0, 1].plot(t, roll, 'tab:olive')
axs[0, 1].set(ylabel='Roll (degrees)')
axs[0, 1].yaxis.tick_right()
axs[0, 1].yaxis.set_label_position("right")
axs[0, 1].set_ylim(-1,1)
axs[1, 1].plot(t, pitch, 'tab:red')
axs[1, 1].set(ylabel='Pitch (degrees)')
axs[1, 1].yaxis.tick_right()
axs[1, 1].yaxis.set_label_position("right")
axs[1, 1].set_ylim(-20,20)
axs[2, 1].plot(t, yaw, 'tab:orange')
axs[2, 1].set(ylabel='Yaw (degrees)')
axs[2, 1].yaxis.tick_right()
axs[2, 1].yaxis.set_label_position("right")
axs[2, 1].set_ylim(-1,1)

for ax in axs.flat:
    ax.set(xlabel='Time (s)')
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.savefig(outName, bbox_inches='tight', dpi=800)

