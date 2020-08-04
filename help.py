import os

sub_folder = './docs/'

files = [f for f in os.listdir(sub_folder) if os.path.isfile(sub_folder + f)]

print(files)

sidebar_file = open(sub_folder + '_sidebar.md', 'w')

for file in files:
	if ".md" in file and '_' not in file:
		with open(os.path.join(sub_folder, file), 'r') as f:
			first_line = f.readline()
			name = first_line.replace('# ', '').replace('\n', '')
			file = file.replace(" ", "%20")
			sidebar_file.write(f'* [{name}]({file})\n')

sidebar_file.close()
