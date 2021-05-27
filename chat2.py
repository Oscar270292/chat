
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	awc = 0
	asc = 0
	apc = 0
	vwc = 0
	vsc = 0
	vpc = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for m in s[2:]:
				if s[2] == '貼圖':
					asc +=1
				elif s[2] == '圖片':
					apc += 1
				else:
					awc += len(m)
		elif name == 'Viki':
			for m in s[2:]:
				if s[2] == '貼圖':
					vsc +=1
				elif s[2] == '圖片':
					vpc += 1
				else:
					vwc += len(m)
	print('allen說了', awc, '個字')
	print('allen傳了', asc, '張貼圖')
	print('allen傳了', apc, '張圖片')
	print('viki說了', vwc, '個字')
	print('viki傳了', vsc, '張貼圖')
	print('viki傳了', vpc, '張圖片')
	

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()