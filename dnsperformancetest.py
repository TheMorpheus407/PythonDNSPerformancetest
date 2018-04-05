import dns.resolver
import time

dnsserver = ['1.1.1.1','4.2.2.1','8.8.8.8','9.9.9.9','80.80.80.80','208.67.222.123','199.85.126.20','185.228.168.168','77.88.8.7','176.103.130.132','156.154.70.3','8.26.56.26']

domains = ['google.com', 'amazon.com', 'facebook.com', 'the-morpheus.de']

toplist = []

for i in dnsserver:
	avg = 0
	for j in domains:
		try:
			resolv = dns.resolver.Resolver()
			resolv.nameservers = [i]
			resolv.timeout = 1
			start = time.time()
			result = resolv.query(j)
			end = time.time()
			avg = avg + (end-start)
		except Exception as e:
			avg = avg + 100000
	avg = avg / len(domains)
	toplist.append([i, avg])

toplist = sorted(toplist, key=lambda x: x[1])

for elem in toplist:
	print("{0:>17} :: {1}".format(elem[0], elem[1]))
