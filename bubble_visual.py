import pandas as pd
import matplotlib.pyplot as plt

# Your data
df = pd.DataFrame({
    'model': ['Susceptible', 'confinement inflow from Susceptible', 'Exposed(Infectious)', 'Exposed(latent)',
              'Presymptomatic infectious', 'Asymptomatic', 'U(Unreported) infectious', 'Subclinical infection (pre&asymptomatic)',
              'I+(infected tested +ve)', 'C+(carrier tested +ve)', 'Symptomat Infection', 'C+(carrier tested +ve)', 'Sever Infection',
              'P(confirmed +ve)', 'Susceptible Vaccinated', 'Exposed Vaccinated', 'Infected Vaccinated', 'V1 (Vaccine 1st dose)',
              'Confined(no more infectious)', 'V2(Vaccine 2nd dose)', 'Vaccination ohne immunity', 'V(Vaccinated)full immunity',
              'Quarantined', 'F(Isolation)either home or hospital', 'L(Lockdown)', 'Hospitalized', 'W(Healthcare workers)', 'C(ICU)',
              'Recovered(no reinfection)', 'Recovered Vaccinated', 'Removed', 'Recovered', 'Deceased'],
    'numbers': [59, 2, 16, 30, 3, 26, 5, 1, 1, 2, 54, 0, 1, 6, 1, 2, 1, 2, 2, 2, 3, 12, 19, 4, 1, 21, 1, 7, 27, 2, 6, 27, 25]
})

# Set the figure size
plt.figure(figsize=(10, 10))

# Scatter plot with bubble sizes
plt.scatter(df.index, [1] * len(df), s=df['numbers'] * 50, alpha=0.5)

# Set the x-axis labels and rotate them for better visibility
plt.xticks(df.index, df['model'], rotation=90)

# Set the title and labels
plt.title('Bubble Visualization of Data')
plt.xlabel('Model')
plt.ylabel('')

# Adjust the spacing to prevent the labels from being cut off
plt.tight_layout()

# Show the plot
plt.show()