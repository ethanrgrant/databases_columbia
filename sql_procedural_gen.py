import random

with open("new_ents.txt", "w") as outfile:
	outstring = "INSERT INTO individuals VALUES\n"
	uid = 1007
	ed_level = ["high school", "college", "masters"]
	income = list(range(80000,120000))
	neighborhood = list(range(11, 20))
	for x in range(1, 30):
		outstring += "(" + str(uid) + ",\'" + str(random.choice(ed_level)) + "\',"+ str(random.choice(income)) + "," + str(random.choice(neighborhood)) + "),\n"
		uid+= 1
	outstring = outstring[:-2]
	outstring += ";"
	outfile.write(outstring)
