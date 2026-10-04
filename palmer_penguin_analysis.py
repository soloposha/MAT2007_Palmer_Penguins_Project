import os
import pandas as pd
import matplotlib.pyplot as plt

# Finding the folder where analysis.py is saved
project_folder = os.path.dirname(os.path.abspath(__file__))

# Loading the dataset from that folder
csv_path = os.path.join(project_folder, "penguins_size.csv")

df = pd.read_csv(csv_path)

print("Dataset loaded successfully!")

# Checking for missing measurements
missing_values = df[
    ["flipper_length_mm", "body_mass_g"]
].isna().sum()

print("Missing values:")
print(missing_values)

if missing_values.sum() > 0:
    print("Missing measurements found. These rows will be removed.")
else:
    print("No missing measurements found.")

# Removing the penguins missing any of the measurments as to not disrupt the program
clean_df = df.dropna(
    subset=["flipper_length_mm", "body_mass_g"]
)
# Will display initial amound of pinguins and the total used for the investigation
print("\nPenguins before cleaning:", len(df))
print("Penguins after cleaning:", len(clean_df))

# Calculating the average measurements and then displaying them
average_mass = clean_df["body_mass_g"].mean()
average_flipper = clean_df["flipper_length_mm"].mean()

print("\nAverage body mass:", round(average_mass, 2), "g")
print("Average flipper length:", round(average_flipper, 2), "mm")

# Calculating the correlation between the length of flipper and body weight for individual pinguins
# Defining corelation function
def calculate_correlation(group):
    r = group["flipper_length_mm"].corr(
        group["body_mass_g"]
    )
    return r

correlation = calculate_correlation(clean_df)

print("\nCorrelation:", round(correlation, 3))

# Creating a scatter plot for the correlation (All pinguins of all specias included)

plt.figure(figsize=(8, 6))

plt.scatter(
    clean_df["flipper_length_mm"],
    clean_df["body_mass_g"],
    alpha=0.6
)

# Adding axis labels and a title to the plot
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.title("Flipper Length vs Body Mass in Palmer Penguins")

# Adding grid lines to the plot
plt.grid(True, alpha=0.3)

# Saves the scater plot that i will use for the analysis and the report
plt.tight_layout()
plt.savefig(
    os.path.join(project_folder, "penguin_scatter.png"),
    dpi=300
)

# Makes the graph pop up in a new window
plt.show()

# Now i am going to look at the correlation specific to the species and compare between themselves

print("\nCorrelation by species:")

plt.figure(figsize=(8, 6))

for species, group in clean_df.groupby("species"):

    # Calculating the correlation for each species specifically
    r = calculate_correlation(group)

    print(species, ":", round(r, 3))

    # Ploting each species separately
    plt.scatter(
        group["flipper_length_mm"],
        group["body_mass_g"],
        label=species,
        alpha=0.7
    )

plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.title("Flipper Length vs Body Mass by Penguin Species")
plt.legend(title="Penguin species")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    os.path.join(project_folder, "penguin_species_scatter.png"),
    dpi=300
)
plt.show()
# here it is essential to close each graph with an x and not just minimise it becausue if not my computer refuses to continue


#Calculating average measurements by species

summary = clean_df.groupby("species").agg(
    penguins=("body_mass_g", "size"),
    average_mass_g=("body_mass_g", "mean"),
    average_flipper_mm=("flipper_length_mm", "mean")
)

print("\nSummary by species:")
print(summary.round(2))

# Saving the results as a new CSV file
summary.to_csv(
    os.path.join(project_folder, "penguin_species_summary.csv")
)

# Calculating uncertainty for all penguins together and for each individual species.

groups = [("All penguins", clean_df)]

# Adding each species as a separate group
groups += list(clean_df.groupby("species"))

# Creating an empty list to store the results
results = []

for name, group in groups:

    # Counting the number of penguins
    n = len(group)

    # Calculating the average body mass and flipper length
    mean_mass = group["body_mass_g"].mean()
    mean_flipper = group["flipper_length_mm"].mean()

    # Calculating the standard error of each mean
    sem_mass = group["body_mass_g"].sem()
    sem_flipper = group["flipper_length_mm"].sem()

    # Calculating Pearson's correlation coefficient
    r = calculate_correlation(group)

    # Storing the results
    results.append({
        "Species": name,
        "N": n,
        "Mean mass (g)": mean_mass,
        "SEM mass (g)": sem_mass,
        "Mean flipper (mm)": mean_flipper,
        "SEM flipper (mm)": sem_flipper,
        "Correlation": r
    })

# Converting the results into a table
uncertainty_df = pd.DataFrame(results)

# Displaying the table
print("\nSTATISTICAL UNCERTAINTY:")
print(uncertainty_df.round(3).to_string(index=False))

# Saving the results into a CSV file
uncertainty_df.to_csv(
    os.path.join(project_folder, "penguin_uncertainty_summary.csv"),
    index=False
)

# Confirming that the analysis has finished running
print("Analysis completed successfully!")