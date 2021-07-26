import subprocess
import time
import json
import sys
import csv

def main():
	args = ["bitcoin-cli","listaddressgroupings"]
	call_output = subprocess.check_output(args)
	call_output = json.loads(call_output)
	print(call_output)
	print(len(call_output))

if __name__ == "__main__":
	main()