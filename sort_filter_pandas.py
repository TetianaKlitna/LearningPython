# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Select the individuals column
individuals = homelessness[["individuals"]]

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] > 10000]

south_mid_atlantic = homelessness[ (homelessness["region"] == "South Atlantic") | (homelessness["region"] == "Mid-Atlantic")]

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
is_in_canu = homelessness["state"].isin(canu)
mojave_homelessness = homelessness[is_in_canu]

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000)&(homelessness["region"] == "Pacific")]