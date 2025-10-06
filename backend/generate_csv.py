import csv


with open("skills.txt","r") as f:
    lines = f.readlines()

skills_data = []
for line in lines:
    if line.strip():  # skip empty lines
        skill, category = line.strip().split(",", 1)  # split only on first comma
        skills_data.append([skill.strip(), category.strip()])

with open('skills.csv','w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['skill','category'])
    writer.writerows(skills_data)
