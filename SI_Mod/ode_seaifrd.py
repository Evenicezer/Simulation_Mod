












































































import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


def derivative(X, t):
    '''
    An ODE-SEIHRD model with possibly reduced risk from infected individuals.

    @param X Array of values for S, E, I, H, R, and D.
    @param t Time point.
    @return Returns derivative of S, E, I, H, R, and D at t.
    '''
    S, E, I, H, R, D = X
    derivS = - contacts * transmission_prob * S * relrisk_infected * I / total_population
    derivE = contacts * transmission_prob * S * relrisk_infected * I / total_population - E / exposed_period
    derivI = E / exposed_period - I / infectious_period
    derivH = prob_hospitalized * I / infectious_period - H / hospitalized_period
    derivR = (1 - prob_hospitalized) * I / infectious_period + (1 - prob_dead) * H / hospitalized_period
    derivD = prob_dead * H / hospitalized_period
    return np.array([derivS, derivE, derivI, derivH, derivR, derivD])



if __name__ == "__main__":




    total_population = 5000  # Total number of individuals
    E0 = 10 # Initial number of exposed individuals
    I0 = 5  # Initial number of infected individuals
    H0 = 0
    R0 = 0 # Initial number of recovered individuals
    D0 = 0
    S0 = total_population - E0 - I0 - H0 - R0 - D0 # Susceptible individuals

    contacts = 10 # number of contacts in standard case
    transmission_prob = 0.05 # transmission probability
    exposed_period = 3  # Mean exposed period
    infectious_period = 7  # Mean infectious period
    hospitalized_period = 10  # Mean hospitalized period
    relrisk_infected = 0.75 # relative risk or non-isolation of infected
    prob_hospitalized = 0.2 # probability of being hospitalized once infected
    prob_dead = 0.1 # probability of dying once hospitalized

    tmax = 90  # maximum simulation day

    fslarge = 20
    fssmall = 16   

    exercise = '10a'

    if exercise == '10a':    

        t = np.linspace(0, tmax, (tmax+1)*10)
        fig, ax = plt.subplots(figsize=[12, 7])        

        solution_seir = integrate.odeint(derivative, [S0, E0, I0, H0, R0, D0], t)
        total_infections = total_population - solution_seir[-1,0]
        ifr = solution_seir[-1,5] / total_infections
        print('The infection fatality rate is ' +  str(np.round(100*ifr,2)) + ' %')
        print('The case fatality rate is ' +  str(np.round(100*ifr/(1-relrisk_infected),2)) + ' %')   



        # ax.plot(t, solution_seir[:,0], label='Susceptibles', linewidth=3)
        ax.plot(t, solution_seir[:, 1], label='Exposed', linewidth=3)
        ax.plot(t, solution_seir[:, 2], label='Infected', linewidth=3)
        ax.plot(t, solution_seir[:, 3], label='Hospitalized', linewidth=3)
        # ax.plot(t, solution_seir[:,4], label='Recovered', linewidth=3)
        ax.plot(t, solution_seir[:, 5], label='Dead', linewidth=3)
        ax.plot(t, 100 * np.ones(len(t)), '--',
                label='Hospital bed capacity', linewidth=3)

        ax.set_xlabel('Days', fontsize=fslarge)
        ax.set_ylabel('Number of individuals', fontsize=fslarge)
        ax.set_title('Simulation of an ODE-SEIHRD model', fontsize=fslarge)
        ax.legend(fontsize=fssmall, loc='center left', bbox_to_anchor=(1, 0.5))

        plt.tight_layout()
        plt.show()

    elif exercise == '10b':

        tmax_npi = 20  # simulation day before NPI    

        t1 = np.linspace(0, tmax_npi, (tmax_npi+1)*10)
        t2 = np.linspace(tmax_npi, tmax, (tmax-tmax_npi+1)*10)
        t = np.concatenate((t1, t2))        

        solution_seir_1 = integrate.odeint(derivative, [S0, E0, I0, H0, R0, D0], t1)

        for contacts_reduced in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
            contacts = contacts_reduced
            [S0new, E0new, I0new, H0new, R0new, D0new] = solution_seir_1[-1,:] # set new initial values
            solution_seir_2 = integrate.odeint(derivative, [S0new, E0new, I0new, H0new, R0new, D0new], t2)

            # "glue" partial solutions together
            solution_seir =  np.concatenate((solution_seir_1, solution_seir_2))

            max_hospitalizations = max(solution_seir[:,3])

            if max_hospitalizations < 100:
                print('Necessary contact restriction from day 20 on for hospital bed capacity is ' +
                        str((10 - contacts_reduced) * 10) + "%.")
                        
                break
