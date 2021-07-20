import subprocess
import time
import json
import sys
import csv

def main(count):
	f = open('csv_files/duration.csv', 'w')
	writer = csv.writer(f)
	header = ["Number of Addresses in DB", "send duration", "listaddresses duration"]
	writer.writerow(header)

	address_types = ["legacy", "p2sh-segwit", "bech32"]
	
	for i in range(count):
		addr = subprocess.check_output(["bitcoin-cli","-named","getnewaddress","address_type=" + address_types[i%3]])
		args = ["bitcoin-cli","-named", "send","outputs=" + json.dumps({addr:0.00001}), "fee_rate=2"]

		timeStarted = time.time()
		subprocess.call(args)
		timetaken = time.time() - timeStarted
		
		args = ["bitcoin-cli","listtransactions"]
		timeStarted_list = time.time()
		subprocess.call(args)
		timetaken_list = time.time() - timeStarted_list
		
		writer.writerow([i,timetaken, timeStarted_list])

	return
	
if __name__ == '__main__':
	main(200)
