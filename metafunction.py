
import os
import time

portals ={"LakEriepJuly2011":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/LakEriepJuly2011/download/_JAMO/51d5253b067c014cd6ef0e82/6308.7.42424.fastq.gz",
	"NOAtaG_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_7/download/_JAMO/55767a430d878529e7caf410/9146.3.123723.TGACCA.fastq.gz",
	"NOAtaG_7_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG/download/_JAMO/55767a3e0d878529e7caf406/9146.2.123720.CGATGT.fastq.gz",} #add references to portals here after vewing xml file



def login(userID, passwd):
	loginstr = "curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=" + userID + "' --data-urlencode 'password=" + passwd + "' -c cookies > /dev/null"
	return loginstr

userID = input("Username: ")
passwd = input("Password: ")
		


for key, value in portals.items():
	#logs the user for each retrieval
	initial = time.perf_counter()
	loginstr = login(userID, passwd)
	"""retrieves fasta file"""
	command = "curl 'https://genome.jgi.doe.gov" + value + "' -b cookies > " + key + ".fastq.gz"
	print(key)
	print(command)
	os.system(command)
	extract = "gunzip " + key + ".fastq.gz"
	print(extract)
	os.system(extract)
	final = time.perf_counter()
	elapsed = (final - initial) / 60
	print("Elapsed Time (minutes)")
	print(elapsed)
	
		
