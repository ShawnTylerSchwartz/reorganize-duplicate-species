#
# reorganize_duplicates.py
# reorganize fish images into different directories based on binomial species taxonomical classification
#
# by Shawn Tyler Schwartz, 2019
# <shawnschwartz@ucla.edu>
# https://shawntylerschwartz.com
#

# import modules
import os, shutil, collections

inputdir = "fish-to-reorganize"
outputdir = "_reorganized-output"
underscore = "_"
oriwdir = os.getcwd()

# write output directory if not already present
if not os.path.isdir(outputdir):
	os.mkdir(outputdir)

# create empty lists
family_list = list()
species_list = list()
combined_list = list()

# define movefishcopy() function
def movefishcopy(curimg, newlocation):
	os.chdir(oriwdir)
	os.chdir(inputdir)
	shutil.copy(curimg, newlocation)
	print(curimg, " Successfully Copied to ", newlocation)
	os.chdir(oriwdir)
	os.chdir(outputdir)

# get fish images from directory
for fish in os.listdir(inputdir):
	if fish.endswith(".png"):
		# expected file naming scheme for proper sorting: Family_Genus_species_id.png
		splitFish = fish.split('_', maxsplit=3)
		Family = splitFish[0]
		genus = splitFish[1]
		species = splitFish[2]
		fishID = splitFish[3]

		# rejoin genus and species together by underscore
		fam_binomial_species_taxonomy = Family + underscore + genus + underscore + species

		family_list.append(Family)
		species_list.append(fam_binomial_species_taxonomy)

		# take all instances of appended list elements and store only unique instances to new array
		species_duplicates = [item for item, count in collections.Counter(species_list).items() if count > 1]
		unique_fams = [item for item, count in collections.Counter(family_list).items() if count >= 1]

# console output for visualization
print("Unique Families Found: ", unique_fams)
print("Unique Duplicate Species Found: ", species_duplicates)

# execute file copying procedure and write necessary output directories for duplicates
os.chdir(outputdir)
for dups in species_duplicates:
	if not os.path.isdir(dups):
		os.mkdir(dups)
		os.chdir(oriwdir)
		for fish in os.listdir(inputdir):
			if fish.endswith(".png"):
				tmp_split = fish.split('_', maxsplit=3)
				tmp_name = tmp_split[0] + underscore + tmp_split[1] + underscore + tmp_split[2]
			if (fish.endswith(".png")) and (dups == tmp_name):
				movefishcopy(fish, os.path.join(oriwdir, outputdir, dups))
				
	else:
		os.chdir(oriwdir)
		for fish in os.listdir(inputdir):
			if fish.endswith(".png"):
				tmp_split = fish.split('_', maxsplit=3)
				tmp_name = tmp_split[0] + underscore + tmp_split[1] + underscore + tmp_split[2]
			if (fish.endswith(".png")) and (dups == tmp_name):
				movefishcopy(fish, os.path.join(oriwdir, outputdir, dups))
os.chdir(oriwdir)