import pandas as pd
import matplotlib.pyplot as plt

# Your data
df = pd.DataFrame({
    'model': ['Susceptible','confinement inflow from Susceptible','Exposed(Infectious)','Exposed(latent)',
              'Presymptomatic infectious','Asymptomatic','U(Unreported) infectious','Subclinical infection (pre&asymptomatic)',
              'I+(infected tested +ve)','C+(carrier tested +ve)','Symptomat Infection','C+(carrier tested +ve)','Sever Infection',
              'P(confirmed +ve)','Susceptible Vaccinated',  'Exposed Vaccinated','Infected Vaccinated','V1 (Vaccine 1st dose)',
              'Confined(no more infectious)','V2(Vaccine 2nd dose)','Vaccination ohne immunity','V(Vaccinated)full immunity',
              'Quarantined','F(Isolation)either home or hospital','L(Lockdown)','Hospitalized','W(Healthcare workers)','C(ICU)',
              'Recovered(no reinfection)','Recovered Vaccinated','Removed','Recovered','Deceased'],
    'Frequency/Number': [ 59,3,16,30,3,26,5,1,1,2,54,1,1,6,1,2,1,2,2,2,3,12,19,4,1,21,1,7,27,2,6,27,25 ]
})

# Create a new figure
plt.figure(figsize=(10, 10))

# Create a horizontal bar plot
plt.barh(df['model'], df['Frequency/Number'], color='skyblue')

# Invert y-axis so that the model with the highest number is on top
plt.gca().invert_yaxis()

# Set the title and labels
plt.title('Quantity of Models')
plt.xlabel('Numbers')
plt.ylabel('Models')
plt.savefig('Bar_graph')

# Show the plot
plt.show()