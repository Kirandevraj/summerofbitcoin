import subprocess
from subprocess import Popen, PIPE
import time
import json

def main():
	pid = subprocess.check_output(['pidof','bitcoind']).strip("\n")
	print("Process id of bitcoind: ", pid)
	addr = subprocess.check_output(["bitcoin-cli","-named","getnewaddress","address_type=legacy"])
	outputs = json.dumps({str(addr.decode("utf-8").replace("\n", "")):0.1})
	p = Popen(["sudo", "perf","record","-g","--call-graph","dwarf","-F","101","-p",pid,"--","sleep","5"])
	start = time.time()
	args = ["bitcoin-cli","-named", "send","outputs=" + outputs, "fee_rate=2"]
	print(args)
	output = subprocess.check_output(args)
	end = time.time()
	p.wait()
	print("Time taken for send operation to end", end - start)
	perf_end =  time.time()
	print("Time taken for perf operation to end", perf_end - end)
	
	cmd = "sudo perf script | stackcollapse-perf.pl --all | flamegraph.pl --color java > bitcoin.svg"
	ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	output = ps.communicate()[0]
	print(output)
	return

if __name__ == "__main__":
	main()