
import os

portals ={"NOAtaG_6_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_4/download/_JAMO/55767a400d878529e7caf407/9146.2.123720.TTAGGC.fastq.gz",
	 "NOAtaG_3_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_2/download/_JAMO/5705dddf7ded5e2cf1e8f40b/10348.7.157979.GGACTCC-CTCTCTA.fastq.gz"} #add references to portals here after vewing xml file




for key, value in portals.items():
	os.system("curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=mbrockley@middlebury.edu' --data-urlencode 'password=FILL IN' -c cookies > /dev/null")
	"""retrieves fasta file"""
	command = "curl 'https://genome.jgi.doe.gov" + value + "' -b cookies > " + key + ".fastq.gz"
	print(key)
	print(command)
	os.system(command)
	print("")
		
