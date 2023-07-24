import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from derivatives import derivative

if __name__ == "__main__":
    total_population = 5000  # Total number of individuals
    E0 = 20  # Initial number of exposed individuals
    A0 = 0   # Initial number of asymptomatic infectious individuals
    I0 = 10  # Initial number of infected symptomatic individuals
    F0 = 0   # Initial number of individuals in isolation
    R0 = 0   # Initial number of recovered individuals
    D0 = 0   # Initial number of death cases
    S0 = total_population - E0 - A0 - I0 - F0 - R0 - D0  # Susceptible individuals



    contacts = 10           # number of contacts in standard case
    transmission_prob = 0.716  # transmission probability
    exposed_period = 3       # Mean exposed period
    asymptomatic_period = 5  # Mean asymptomatic infectious period
    infectious_period = 7    # Mean infectious period
    isolated_period = 10 # Mean isolation
    reducing_transmission= 0.859
    prob_asymptomatic = 0.2  # probability of being asymptomatic once exposed
    prob_isolated_asy = 0.2  # probability of being
    prob_dead = 0.1          # probability of dying

    tmax = 90  # maximum simulation day

    fslarge = 20
    fssmall = 16

    t = np.linspace(0, tmax, (tmax+1)*10)
    fig, ax = plt.subplots(figsize=[12, 7])

    solution_seaifrd = integrate.odeint(derivative, [S0, E0, A0, I0, F0, R0, D0], t,
                                       args=(contacts, transmission_prob,  total_population,reducing_transmission,
                                             exposed_period, asymptomatic_period, infectious_period,
                                             isolated_period, prob_asymptomatic, prob_isolated_asy,
                                             prob_dead))

    total_infections = total_population - solution_seaifrd[-1, 0]



    ax.plot(t, solution_seaifrd[:, 0], label='Susceptible', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 1], label='Exposed', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 2], label='Asymptomatic Infectious', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 3], label='Infected Symptomatic', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 4], label='Isolation', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 5], label='Recovered', linewidth=3)
    ax.plot(t, solution_seaifrd[:, 6], label='Death', linewidth=3)


    ax.set_xlabel('Days', fontsize=fslarge)
    ax.set_ylabel('Number of individuals', fontsize=fslarge)
    ax.set_title('Simulation of an ODE-SEAIFRD model', fontsize=fslarge)
    ax.legend(fontsize=fssmall, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()
    plt.show()