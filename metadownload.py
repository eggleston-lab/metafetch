import os
import time

portals = {"LakEricontroER36_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/LakEricontroER36/download/_JAMO/5a8bfc8164d0b326cdd24cc2/12221.1.245265.ACTCGCT-TCGCATA.fastq.gz", "CB_VirMetaG_3_FD1":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG_2/download/_JAMO/59516afa7ded5e4e5bbdb64e/11724.6.216386.CTTGTA.fastq.gz", "CB_VirMetaG_3_FD2":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG_2/download/_JAMO/594a64fe7ded5e4e5bbd34d1/11706.6.215727.TAGGCAT-TATCCTC.fastq.gz", "CB_VirMetaG_3_FD3":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG_2/download/_JAMO/567c03de0d878518a8a3a497/10057.5.146705.GTGAAA.fastq.gz", "CB_VirMetaG_FD1":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG/download/_JAMO/59516af37ded5e4e5bbdb64b/11724.6.216386.GCCAAT.fastq.gz", "CB_VirMetaG_FD2":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG/download/_JAMO/594a64f47ded5e4e5bbd34cd/11706.6.215727.TCCTGAG-TATCCTC.fastq.gz", "CB_VirMetaG_FD3":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/CB_VirMetaG/download/_JAMO/567c03dc0d878518a8a3a493/10057.5.146705.GTAGAG.fastq.gz"} #add references to portals here after vewing xml file


username = input("Username: ")
password = input("Password: ")

for key, value in portals.items():
	"""start timing"""
	initial = time.perf_counter()

	"login to JGI"""
	login = "curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=" + username + "' --data-urlencode 'password=" + password + "' -c cookies > /dev/null"
	os.system(login)

	"""retrieves fasta file"""
	command = "curl 'https://genome.jgi.doe.gov" + value + "' -b cookies > " + key + ".fastq.gz"
	print(key)
	print(command)
	os.system(command)

	"""Unzip"""
	g-unzip = "gunzip " + key + ".fastq.gz"
	print(g-unzip)
	os.command(g-unzip)

	"""Calculate elapsed time"""
	final = time.perf_counter()
	elapsed = (final - initial)/60
	print(elapsed)
	print("")
