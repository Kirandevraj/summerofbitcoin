import matplotlib.pyplot as plt
import numpy as np
import csv

with open('duration_test1.csv', newline='') as f:
    reader = csv.reader(f)
    # data = list(reader)
    header = next(reader)
    rows = [[float(row[0]), float(row[1]), float(row[2])] for row in reader if row]

# plt.title("Time taken for send transaction")
# plt.plot(np.arange(0, len(rows)), np.asarray(rows)[:,1])
# plt.xlabel("Number of addresses present in the wallet")
# plt.ylabel("Time taken for send transaction in seconds")
# plt.savefig("send.png")
# plt.clf()

# plt.title("Time taken for list transaction")
# plt.plot(np.arange(0, len(rows)), np.asarray(rows)[:,2])
# plt.xlabel("Number of addresses present in the wallet")
# plt.ylabel("Time taken for listtransaction")
# plt.savefig("list.png")

print(np.mean(np.asarray(rows)[:,1][-10000:]))