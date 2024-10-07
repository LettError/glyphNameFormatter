#unicode 12
lowercase = "00DF	0053 0053		Ll		LATIN SMALL LETTER SHARP S"
uppercase = "1E9E		00DF	Lu		LATIN CAPITAL LETTER SHARP S"

lines = [lowercase, uppercase]
for line in lines:
	uniNumber, uniUppercase, uniLowercase, uniCategory, mathFlag, uniName, = line.split("\t")
	print(f"uniNumber:{uniNumber}, uniUppercase:{uniUppercase}, uniLowercase:{uniLowercase}, uniName:{uniName}")
