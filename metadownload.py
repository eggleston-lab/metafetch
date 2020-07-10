
import os

portals = {"NOAtaG_3_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_2/download/_JAMO/5705dddf7ded5e2cf1e8f40b/10348.7.157979.GGACTCC-CTCTCTA.fastq.gz", "NOAtaG_6_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_4/download/_JAMO/55767a400d878529e7caf407/9146.2.123720.TTAGGC.fastq.gz", "LakEricontroER36_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/LakEricontroER36/download/_JAMO/5a8bfc8164d0b326cdd24cc2/12221.1.245265.ACTCGCT-TCGCATA.fastq.gz", "CB_VirMetaG_3_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG_2/download/_JAMO/59516afa7ded5e4e5bbdb64e/11724.6.216386.CTTGTA.fastq.gz"} #add references to portals here after vewing xml file


username = input("Username: ")
password = input("Password: ")

for key, value in portals.items():
	login = "curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=" + username + "' --data-urlencode 'password=" + password + "' -c cookies > /dev/null"
	os.system(login)
	"""retrieves fasta file"""
	command = "curl 'https://genome.jgi.doe.gov" + value + "' -b cookies > " + key + ".fastq.gz"
	print(key)
	print(command)
	os.system(command)
	print("")
		
