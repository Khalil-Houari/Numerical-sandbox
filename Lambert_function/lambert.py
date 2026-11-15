import numpy as np 
import matplotlib.pyplot as plt


def f():
    x = np.linspace(-1, 5, 1000)
    return np.array([x, np.exp(x)*x])

def lambert(f) :
    return np.array([f[1], f[0]])

def ploter(f,name, color) :
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')

    color_map = plt.get_cmap(color)

    ax.grid(True, color='white', linestyle='--', linewidth=0.5, alpha=0.3)

    ax.set_title(name)

    ax.plot(f[0], f[1], color=color_map(0.5), label=name)
    ax.legend()



if __name__ == "__main__":
    f = f()
    ploter(lambert(f), 'Lambert Function', 'viridis')
    ploter(f, 'xe^x Function', 'plasma')
    plt.show()