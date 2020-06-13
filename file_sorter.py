import os
import shutil
os.chdir('C:\\Users\\Sarthak\\Desktop\\S')
									#	FILE SORTER BY SARTHAK MISHRA

os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Word Files(.docx)')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Powerpoint Files(.ppt)')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Java Codes')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Python Codes')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\HTML Codes')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\C, C++, php Codes')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Text Files(.txt)')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Images')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Videos')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\pdf')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Compressed Files')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Applications')
os.mkdir('C:\\Users\\Sarthak\\Desktop\\S\\Excel Files')

# For word files
for filename in os.listdir():
	if filename.endswith('.docx'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Word Files(.docx)')

# For powerpoint presentations
	if filename.endswith('.pptx'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Powerpoint Files(.ppt)')

# For Java Codes
	if filename.endswith('.java'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Java Codes')

# For Python Codes
	if filename.endswith('.py'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Python Codes')

# For HTML Codes
	if filename.endswith('.htm' or '.html'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\HTML Codes')

# For php,c,c++ Codes
	if filename.endswith('.php' or '.c'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\C, C++, php Codes')

# For C++ Codes
	if filename.endswith('.cpp'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\C, C++, php Codes')

# For Text Files
	if filename.endswith('.txt'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Text Files(.txt)')

# For images
	if filename.endswith('.png' or '.jpg' or '.jpeg'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Images')

# For Videos
	if filename.endswith('.mp4' or '.mkv' or '.3gp'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Videos')

# For pdf
	if filename.endswith('.pdf'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\pdf')

# For Compressed Files
	if filename.endswith('.zip' or '.rar'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Compressed Files')

# For applications
	if filename.endswith('.exe'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Applications')

# For Excel Files
	if filename.endswith('.xlsx'):
		shutil.move(filename,'C:\\Users\\Sarthak\\Desktop\\S\\Excel Files')