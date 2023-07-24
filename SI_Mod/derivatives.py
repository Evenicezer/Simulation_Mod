import numpy as np
from typing import Protocol

def derivative(X, t, contacts,transmission_prob, total_population,reducing_transmission,
               exposed_period, asymptomatic_period, infectious_period, isolated_period,
               prob_asymptomatic, prob_isolated_asy, prob_dead):
    '''
    An ODE-SEAIFRD model with possibly reduced risk from asymptomatic infected individuals.

    @param X Array of values for S, E, A, I, F, R, and D.
    @param t Time point.

    @param transmission_prob Transmission probability.
    @param reducing_transmission that reduce the transmission of asymptomatic ~ 0.859
    @param total_population Total number of individuals.
    @param exposed_period Mean exposed period.
    @param asymptomatic_period Mean asymptomatic infectious period.
    @param infectious_period Mean infectious period.
    @param isolated_period Mean quarantined period.
    @param prob_asymptomatic Probability of being asymptomatic once exposed.
    @param prob_isolated Probability of being isolated once infected.
    @param prob_dead Probability of dying
    @return Returns derivative of S, E, A, I, F, R, and D at t.
    '''
    S, E, A, I, F, R, D = X
    derivS = - contacts*transmission_prob * S * (I + reducing_transmission*A) / total_population
    derivE = contacts*transmission_prob * S * (I + reducing_transmission*A) / total_population -  E/exposed_period
    derivA = prob_asymptomatic * E / exposed_period - A / asymptomatic_period
    derivI = (1 - prob_asymptomatic)  * E / exposed_period - I / infectious_period
    derivF = (1 - prob_dead)* I / infectious_period - F / isolated_period + prob_isolated_asy*A/asymptomatic_period
    derivR =   (1-prob_isolated_asy)*A / asymptomatic_period + F/isolated_period
    derivD =   prob_dead *I / infectious_period
    return np.array([derivS, derivE, derivA, derivI, derivF, derivR, derivD])


""" some modification
    derivS = - contacts*transmission_prob * S * (I + reducing_transmission*A) / total_population
    derivE = contacts*transmission_prob * S * (I + reducing_transmission*A) / total_population -  E/exposed_period
    derivA = prob_asymptomatic * E / exposed_period - A / asymptomatic_period
    derivI = (1 - prob_asymptomatic)  * E / exposed_period - I / infectious_period
    derivF = (1 - prob_dead)* I / infectious_period - F / isolated_period + prob_isolated_asy*A/asymptomatic_period
    derivR =   (1-prob_isolated_asy)*A / asymptomatic_period + F/isolated_period
    derivD =   prob_dead *I / infectious_period
    return np.array([derivS, derivE, derivA, derivI, derivF, derivR, derivD])
    """