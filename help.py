import os

path = './docs/'

sub_folders = [f for f in os.listdir(path) if os.path.isdir(path + f)]

sidebar_file = open(os.path.join(path, '_sidebar.md'), 'w')
for sub_folder in sub_folders:
	sidebar_file.write(f'* **{sub_folder}**\n')
	abs_folder = os.path.join(path, sub_folder)
	files = [f for f in os.listdir(abs_folder) if os.path.isfile(os.path.join(abs_folder, f))]
	files.sort()
	print(files)

	for file in files:
		if ".md" in file and '_' not in file:
			with open(os.path.join(abs_folder, file), 'r') as f:
				first_line = f.readline()
				name = first_line.replace('# ', '').replace('\n', '')
				file = file.replace(" ", "%20")
				file_link = os.path.join(sub_folder, file)
				sidebar_file.write(f'	* [{name}]({file_link})\n')

sidebar_file.close()
