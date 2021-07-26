import subprocess
import time
import json
import sys
import csv

def main():
	args = ["bitcoin-cli","listaddressgroupings"]
	timeStarted_list = time.time()
	call_output = subprocess.check_output(args)
	timeEnded_list = time.time()
	timetaken_list = timeEnded_list - timeStarted_list
	call_output = json.loads(call_output)
	print(call_output)
	print(len(call_output))

if __name__ == "__main__":
	main()