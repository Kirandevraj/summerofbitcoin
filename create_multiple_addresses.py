import subprocess
import time
import json
import sys
import csv

def main(start, end):

	# create_wallet = subprocess.check_output(["bitcoin-cli","-named","createwallet",'wallet_name=regtest_wallet_1',"descriptors=true"])
	# wallet = subprocess.check_output(["bitcoin-cli", "loadwallet", "regtest_wallet"])
	# mining_addr = subprocess.check_output(["bitcoin-cli","getnewaddress"])
	# mining_addr = str(mining_addr.decode("utf-8").replace("\n", ""))
	# print(mining_addr)
	# mine_coins = subprocess.check_output(["bitcoin-cli","generatetoaddress","150", mining_addr])
	# print(mine_coins)
	f = open('csv_files/duration_test1.csv', 'a')
	writer = csv.writer(f)
	# header = ["Number of Addresses in DB", "send duration", "listaddresses duration"]
	# writer.writerow(header)

	address_types = ["legacy", "p2sh-segwit", "bech32"]
	
	for i in range(start, end):
		if i % 10 == 0:
			print(i, end)
		addr = subprocess.check_output(["bitcoin-cli","-named","getnewaddress","address_type=" + address_types[i%3]])
		outputs = json.dumps({str(addr.decode("utf-8").replace("\n", "")):0.1})
		args = ["bitcoin-cli","-named", "send","outputs=" + outputs, "fee_rate=2"]

		timeStarted = time.time()
		call_output = subprocess.check_output(args)
		timeEnded = time.time()
		timetaken = timeEnded - timeStarted
		
		args = ["bitcoin-cli","listtransactions"]
		timeStarted_list = time.time()
		call_output = subprocess.check_output(args)
		timeEnded_list = time.time()
		timetaken_list = timeEnded_list - timeStarted_list

		writer.writerow([i,timetaken, timetaken_list])
		f.flush()
		mine_coins = subprocess.check_output(["bitcoin-cli","generatetoaddress","1", str(addr.decode("utf-8").replace("\n", ""))])

	return
	
if __name__ == '__main__':
	main(44724,75000)

	# Notes:
	# Mined at the beginning and at around 200
	# Got 'transaction too large error' at count 2820, hence mined a few blocks to 3480 and
	# changed transaction amount from 0.00001 to 0.1 BTC
