import subprocess
import json

def main():
	# I have created a desciptor wallet.
	# 	{
	#   "walletname": "test_desc",
	#   "walletversion": 169900,
	#   "format": "sqlite",
	#   "balance": 0.00992790,
	#   "unconfirmed_balance": 0.00000000,
	#   "immature_balance": 0.00000000,
	#   "txcount": 4,
	#   "keypoolsize": 3000,
	#   "keypoolsize_hd_internal": 3000,
	#   "paytxfee": 0.00000000,
	#   "private_keys_enabled": true,
	#   "avoid_reuse": false,
	#   "scanning": false,
	#   "descriptors": true
	# }

	# Generate Address:
	# for i in range(100):
	# 	subprocess.Popen(["../bitcoin/src/bitcoin-cli","getnewaddress"])

	#Get All the generated Addresses:
	all_addrs = subprocess.check_output(["../bitcoin/src/bitcoin-cli","listreceivedbyaddress","0","true"])
	print(str(all_addrs))
	print("All")
	all_addrs = json.loads(all_addrs)
	just_addrs = [str(addr["address"]) for addr in all_addrs]
	# print(just_addrs)
	print(len(just_addrs))
	for item in just_addrs:
		# print(item)
		addr = {item:0.00001}
		addr = json.dumps(addr)
		args = ["../bitcoin/src/bitcoin-cli","-named", "send","outputs=" + addr, "fee_rate=1"]
		p = subprocess.check_output(args)
	return
	
if __name__ == '__main__':
	main()
