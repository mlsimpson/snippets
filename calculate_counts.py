import pprint

counts = ["900,google.com",
		"100,yahoo.com",
		"5,sports.yahoo.com",
		"1,mobile.sports.yahoo.com",
		"10,com.com",
		"80,wikipedia.org",
		"80,en.wikipedia.org",
		"1,wikipedia.uk"
		]

def calculateCounts(counts):

	counts_per_domain = {}

	# for row in counts:
	#     number = row.split(',')[0]
	#     domain = row.split(',')[1].split('.')
	#     counts_per_domain.append([number, domain])

	for row in counts:
		count = row.split(',')[0]
		domain_parts = row.split(',')[1].split('.')
		# print(count, domain_parts)
		domain_parts_len = len(domain_parts)
		for i in range(domain_parts_len):
			url = ".".join(domain_parts[i:])
			# print(url)
			counts_per_domain.setdefault(url, 0)
			counts_per_domain[url] += int(count)
			# print(counts_per_domain[url], url)
	pprint.pprint(sorted(counts_per_domain.items(), key=lambda x: x[1], reverse=True))


# though you can use the standard python dict with .setdefault(<key>,
# <default>) to get the same thing without importing anything

# Thanks, Sean and voidlilly

from collections import defaultdict

results = defaultdict(int)
for x in counts:
	count, url = x.split(",")
	count = int(count)
	parts = url.split(".")
	for x, part in list(enumerate(parts)):
		subdomain = ".".join(parts[x:])
		results[subdomain] += count

# print(results)

calculateCounts(counts)
