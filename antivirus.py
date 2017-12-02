# Python Script for Yara.
# EFREI Promo 2019,
# BOUQUET Julien <julien.bouquet@efrei.net>
# LAMBERTZ Marc <marc.lambertz@efrei.net>
# MARTIN Alexandre <alexandre.martin@efrei.net>

import sys
import os
import shutil
import urllib
import zipfile
import yara
import config
import antivilib

# Check user input
if len(sys.argv) <= 1:
    raise Exception("Usage : python antivirus.py ./way/to/path")

# ASCII ART :)
print("""
 ______  __          ___      ___
|  ____|/ _|        (_) \    / (_)
| |__  | |_ _ __ ___ _ \ \  / / _ _ __ _   _ ___
|  __| |  _| '__/ _ \ | \ \/ / | | '__| | | / __|
| |____| | | | |  __/ |  \  /  | | |  | |_| \__ \\
|______|_| |_|  \___|_|   \/   |_|_|   \__,_|___/
""")
print("Efrei's Antivirus, welcome !\n")
print("Bouquet, Lambertz, Martin\n\n")

# Clean old resources
if(os.path.isdir("viralBase")):
	shutil.rmtree("viralBase")

# Downloads and extract Yara's rules from Github
print("Downloading Yara's rules, please wait...\n")
urllib.urlretrieve(config.rulesUrl, "viralBase.zip")
print("Extracting rules, please wait...\n")
zip_ref = zipfile.ZipFile("viralBase.zip", 'r')
zip_ref.extractall("viralBase")
zip_ref.close()
os.remove("viralBase.zip")
print("Download and extraction complete !\n\n")

# Correct index files for Windows
if(config.windows):
	print("Upgrade index for Windows, please wait...")
	antivilib.windowsCorrect("viralBase/rules-master/index.yar")
	print("Upgrade complete !\n\n")

# Run yara to scan target folder
print("Check files from the target folder, please wait...")
rule = yara.compile("viralBase/rules-master/index.yar")
for root, dirs, files in os.walk(sys.argv[1]):
    for name in files:
        print("Checking " + os.path.join(root, name))
        matches = rule.match(os.path.join(root, name))
        print(matches)
print("End of files checking")

# End
if(config.windows):
	os.system("pause")
