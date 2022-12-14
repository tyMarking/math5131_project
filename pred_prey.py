import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# A = 100
A = 140
ALPHA = 10000
# BETA = 70
BETA = 50
X = 3e-10

SpeciesN = "Satelites"
Speciesn = "Debris Fragments"

def farinella_cordelli(state,t):
    N, n = state
    return A-(X*n*N), (BETA*A) + (ALPHA*X*n*N)


def main():
    #what was used in the paper
    state0 = [2e3,5e4]

    #modern version
    state0 = [3e3,700000]
    t = np.arange(0.0, 300.0, 0.0001)
    states = odeint(farinella_cordelli, state0, t)
    # print(states)

    max_sat_t = np.argmax(states[:,0])
    print(states[max_sat_t])

    # states[:,0] = states[:,0]/1.4e4
    # states[:,1] = states[:,1]/5e8
    

    plt.plot(states[:,0],states[:,1])
    plt.xlabel(SpeciesN + " (1.4e4)")
    plt.ylabel(Speciesn + " (5e8)")
    plt.title(f'{Speciesn} vs. {SpeciesN} (Time Suppressed)')
    plt.grid(True, linewidth=0.5)
    plt.show()
    
    plt.plot(states[:,0])
    plt.plot(states[:,1])
    plt.legend([SpeciesN, Speciesn])
    plt.xlabel('Time (100 years)')
    plt.ylabel('Population Size\n(1.4e4 satelites, 5e8 fragments)')
    plt.title(f'{Speciesn} vs. {SpeciesN}')
    plt.grid(True, linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    main()