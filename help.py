import os

sub_folder = './docs/'

files = [f for f in os.listdir(sub_folder) if os.path.isfile(sub_folder + f)]

print(files)

sidebar_file = open(sub_folder + '_sidebar.md', 'w')

for file in files:
	if ".md" in file and '_' not in file:
		name = file.split(".md")
		file = file.replace(" ", "%20")
		sidebar_file.write(f'* [{name[0]}]({file})\n')

sidebar_file.close()
