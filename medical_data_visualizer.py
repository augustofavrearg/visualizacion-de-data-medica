import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = df_medico=pd.read_csv("medical_examination.csv")

# Add 'overweight' column
imc=df_medico["weight"]/((df_medico["height"]/100)**2)

df_medico["sobrepeso"]=imc

df_medico.loc[df_medico["sobrepeso"]<=25, "sobrepeso"]=0
df_medico.loc[df_medico["sobrepeso"]>25, "sobrepeso"]=1
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df_medico.loc[df_medico["cholesterol"]==1, "cholesterol"]=0
df_medico.loc[df_medico["cholesterol"]>1, "cholesterol"]=1

df_medico.loc[df_medico["gluc"]==1, "gluc"]=0
df_medico.loc[df_medico["gluc"]>1, "gluc"]=1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    df_cat=df_medico.melt(id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "sobrepeso", "smoke"])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df_medico[(df_medico['ap_lo'] <= df_medico['ap_hi']) &
                      (df_medico['height'] >= df_medico['height'].quantile(0.025)) &
                      (df_medico['height'] <= df_medico['height'].quantile(0.975)) &
                      (df_medico['weight'] >= df_medico['weight'].quantile(0.025)) &
                      (df_medico['weight'] >= df_medico['weight'].quantile(0.975))
                    ]
    # Calculate the correlation matrix
    corr = df_heat.corr()
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)]=True 



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))


    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', linewidths=.3)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig