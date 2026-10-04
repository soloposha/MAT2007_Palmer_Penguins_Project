# Palmer Penguins Data Analysis

## Research Question

How does the correlation between flipper length and body mass differ among the three penguin species of the Palmer Archipelago?

## Project Description

This project analyses the Palmer Penguins dataset using Python.

The aim is to investigate the relationship between penguin flipper length and body mass and to determine whether this relationship differs between the three penguin species found in the Palmer Archipelago: Adelie, Chinstrap, and Gentoo.

## Dataset

The dataset contains measurements from 344 penguins.

The variables mainly used in this analysis are:

- `species`
- `flipper_length_mm`
- `body_mass_g`

The three species included in the dataset are:

- Adelie
- Chinstrap
- Gentoo

Dataset source:

https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data

The dataset file used by the program is:

`penguins_size.csv`


## Data Cleaning

The dataset was checked for missing values in flipper length and body mass.

Two penguins had missing measurements and were removed because both measurements are required to calculate the correlation.

Therefore:

- Original number of penguins: 344
- Number used in the analysis: 342

## Analysis

The Python program:

- loads the dataset using pandas
- checks for missing values
- removes rows with missing flipper length or body mass
- calculates average body mass and average flipper length
- calculates Pearson's correlation coefficient
- compares correlations between penguin species
- calculates average measurements for each species
- calculates the standard error of the mean (SEM) as a measure of uncertainty in the mean measurements
- creates scatter plots
- saves summary results as CSV files

## Dependencies

The project requires Python and the following Python libraries:

- pandas
- matplotlib

They can be installed using:

```bash
python -m pip install pandas matplotlib
```

## How to Run the Program

Place `penguin_analysis.py` and `penguins_size.csv` in the same folder.

Open the project folder in Visual Studio Code.

Run the program using:

```bash
python penguin_analysis.py
```

The program will display the results in the terminal and create the graphs and summary files automatically.

## Output Files

The program generates:

- `penguin_scatter.png`
- `penguin_species_scatter.png`
- `penguin_species_summary.csv`
- `penguin_uncertainty_summary.csv`

## Main Results

After data cleaning, 342 penguins were included in the analysis.

The overall correlation between flipper length and body mass was:

`r = 0.871`

The correlations for each species were:

- Adelie: `r = 0.468`
- Chinstrap: `r = 0.642`
- Gentoo: `r = 0.703`

The overall correlation is stronger than the correlations calculated separately for each species.

The scatter plot also shows that the three species form different groups, suggesting that species differences contribute to the strong overall relationship between flipper length and body mass.