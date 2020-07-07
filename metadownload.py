
import os

portals ={"LakEriepJuly2011":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/LakEriepJuly2011/download/_JAMO/51d5253b067c014cd6ef0e82/6308.7.42424.fastq.gz",
	"NOAtaG_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG_7/download/_JAMO/55767a430d878529e7caf410/9146.3.123723.TGACCA.fastq.gz",
	"NOAtaG_7_FD":"/portal/ext-api/downloads/get_tape_file?blocking=true&url=/NOAtaG/download/_JAMO/55767a3e0d878529e7caf406/9146.2.123720.CGATGT.fastq.gz",} #add references to portals here after vewing xml file




for key, value in portals.items():
	os.system("curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=mbrockley@middlebury.edu' --data-urlencode 'password=FILL IN' -c cookies > /dev/null")
	"""retrieves fasta file"""
	command = "curl 'https://genome.jgi.doe.gov" + value + "' -b cookies > " + key + ".fastq.gz"
	print(key)
	print(command)
	os.system(command)
	print("")
		
