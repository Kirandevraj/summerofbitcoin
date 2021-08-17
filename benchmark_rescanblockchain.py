import subprocess
import time
import json
import sys
import csv

def main(start, end):

	# create_wallet = subprocess.check_output(["bitcoin-cli","-named","createwallet",'wallet_name=db_rescan_test',"descriptors=true"])

	f = open('csv_files/duration_dbscan_main.csv', 'a')
	writer = csv.writer(f)
	header = ["Number of Addresses in DB", "rescan_db_duration"]
	writer.writerow(header)

	address_types = ["legacy", "p2sh-segwit", "bech32"]
	
	for i in range(start, end):
		if i % 10 == 0:
			print(i, end)
		addr = subprocess.check_output(["bitcoin-cli","-named","getnewaddress","address_type=" + address_types[i%3]])
		args = ["bitcoin-cli","rescanblockchain","500000", "501000"]

		timeStarted = time.time()
		call_output = subprocess.check_output(args)
		timeEnded = time.time()
		timetaken = timeEnded - timeStarted
		
		writer.writerow([i,timetaken])
		f.flush()
	return
	
if __name__ == '__main__':
	main(0,100000)
