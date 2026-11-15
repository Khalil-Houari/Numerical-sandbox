import numpy as np
import matplotlib.pyplot as plt 


def lorenz_att(state, parameters) :
    x, y, z = state
    sigma, beta, rho = parameters
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    
    state_vec = np.array([dx, dy, dz])
    return state_vec

def rk4_step(state, dt, parameters) :

    state0 = state 
    k1 = lorenz_att(state0, parameters)

    state1 = state0 + 0.5 * dt * k1
    k2 = lorenz_att(state1, parameters)

    state2 = state0 + 0.5 * dt * k2
    k3 = lorenz_att(state2, parameters)

    state3 = state0 + dt * k3
    k4 = lorenz_att(state3, parameters)

    return state0 + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)


def simulate(state, parameters, dt, step_number) :
    trajectory = np.zeros((step_number, 4))
    for i in range(step_number) : 
        trajectory[i, :3] = rk4_step(state, dt, parameters)
        state = trajectory[i, :3]
        trajectory[i, 3] = (i+1) * dt
    return trajectory


def ploter2(t1, t2,s1, s2, p1, p2) :
    plt.style.use('dark_background')
    fig =plt.figure(figsize=(10,10))

    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    color_map1 = plt.get_cmap('cool')
    color_map2 = plt.get_cmap('hot')

    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))

    ax.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    ax.set_title('Lorenz Attractor')
    

    ax.plot(t1[:,0], t1[:,1], t1[:,2], color=color_map1(0.5), lw=0.5, 
            label= f"Trajectory 1:\n starting coordinates: \n    x={s1[0]:.3f}\n    y={s1[1]:.3f}\n    z={s1[2]:.3f}\n parameters:\n    sigma={p1[0]:.3f}\n    beta={p1[1]:.3f}\n    rho={p1[2]:.3f}" )
    ax.plot(t2[:,0], t2[:,1], t2[:,2], color=color_map2(0.5), lw=0.5, 
            label= f"\n Trajectory 2:\n starting coordinates: \n    x={s2[0]:.3f}\n    y={s2[1]:.3f}\n    z={s2[2]:.3f}\n parameters:\n    sigma={p2[0]:.3f}\n    beta={p2[1]:.3f}\n    rho={p2[2]:.3f}" )
    ax.legend(prop={'size': 10}, loc='upper left',bbox_to_anchor=(1.05, 1), frameon=False, facecolor='black', edgecolor='white', fontsize=8)
    

def step_number(dt) : #the clamp of time will be 100 seconds, so the number of steps will be 100/dt
    return int(100/dt)


def ploter1(t1, s1, p1, dt, color) :
    plt.style.use('dark_background')
    fig =plt.figure(figsize=(10,10))

    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    color_map1 = plt.get_cmap(color)

    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color((1, 1, 1, 0))

    ax.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    ax.set_title('Lorenz Attractor')
    

    ax.plot(t1[:,0], t1[:,1], t1[:,2], color=color_map1(0.5), lw=0.5, 
            label= f"Trajectory :\n step size: {dt}\n starting coordinates: \n    x={s1[0]:.3f}\n    y={s1[1]:.3f}\n    z={s1[2]:.3f}\n parameters:\n    sigma={p1[0]:.3f}\n    beta={p1[1]:.3f}\n    rho={p1[2]:.3f}" )
    ax.legend(prop={'size': 10}, loc='upper left',bbox_to_anchor=(1.05, 1), frameon=False, facecolor='black', edgecolor='white', fontsize=8)
    

def ploter_2D(tr, p, dt) :
    plt.style.use('dark_background')
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 16), sharex=True)
    fig.subplots_adjust(hspace=0.4, bottom=0.07, top=0.9, left=0.1, right=0.9)

    ax1.set_xlabel('t axis', fontsize=8, labelpad=5)
    ax1.set_ylabel('X axis', fontsize=8, labelpad=5)
    ax1.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    ax2.set_xlabel('t axis', fontsize=8, labelpad=5)
    ax2.set_ylabel('Y axis', fontsize=8, labelpad=5)
    ax2.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    ax3.set_xlabel('t axis', fontsize=8, labelpad=5)
    ax3.set_ylabel('Z axis', fontsize=8, labelpad=5)
    ax3.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    fig.text(0.5, 0.01, f"time step: {dt}\nparameters:  sigma={p[0]:.3f},  beta={p[1]:.3f},  rho={p[2]:.3f}", ha="center", va="bottom", fontsize=10, color='white')
    
    ax1.plot(tr[:,3], tr[:,0], color='cyan', lw=0.5, label= "X(t)" )
    ax2.plot(tr[:,3], tr[:,1], color='green', lw=0.5, label= "Y(t)" )
    ax3.plot(tr[:,3], tr[:,2], color='red', lw=0.5, label= "Z(t)" )

    ax1.legend(prop={'size': 10}, loc='upper left',bbox_to_anchor=(1.05, 1), frameon=False, facecolor='black', edgecolor='white', fontsize=8)
    ax2.legend(prop={'size': 10}, loc='upper left',bbox_to_anchor=(1.05, 1), frameon=False, facecolor='black', edgecolor='white', fontsize=8)
    ax3.legend(prop={'size': 10}, loc='upper left',bbox_to_anchor=(1.05, 1), frameon=False, facecolor='black', edgecolor='white', fontsize=8)



if __name__ == "__main__" :
    #parameters = np.array([sigma, beta, rho])


    step1 = 0.0001
    parameters1 = np.array([10, 8/3, 28],dtype=float) 
    state1 = np.array([1,1,1],dtype=float) 
    trajectory1 = simulate(state1, parameters1, step1, step_number(step1))


    step2 = 0.1
    parameters2 = np.array([10, 8/3, 28],dtype=float)
    state2 = np.array([1,1,1],dtype=float) 
    trajectory2 = simulate(state2, parameters2, step2, step_number(step2))


    step3 = step1
    parameters3 = np.array([10, 8/3, 215],dtype=float)
    state3 = np.array([1,1,1],dtype=float)
    trajectory3 = simulate(state3, parameters3, step3, step_number(step3))

    ploter1(trajectory3,state3,parameters3, step3, "hot")
    #ploter_2D(trajectory3, parameters3, step3)

    #ploter1(trajectory2,state2,parameters2, step2, "inferno")
    #ploter_2D(trajectory2, parameters2, step2)

    ploter1(trajectory1, state1, parameters1, step1, "viridis")
    #ploter_2D(trajectory1, parameters1, step1)
    

    ploter2(trajectory1, trajectory3, state1, state3, parameters1, parameters3)

    plt.show()