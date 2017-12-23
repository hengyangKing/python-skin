#coding = utf-8
def main():
	print("please input data :\n")
	while True:
		try:
			count = int(input())
		except Exception as ret:
			print("input error parameters")
		else:
			if count > 0:
				break
			else:
				print("Please enter the number of paragraphs greater than 0")

	index = count
	ends = []
	limited = []
	while (index != 0):
		try:
			start, end, speed = (int(x) for x in input().split(' '))
		except Exception as ret:
			print("Input error parameters")
		else:
			if start < 0 or end < 0 or speed < 0 or end < start or end > 100 :
				print("Input error parameters")

			elif (len(ends)>0) :
				if(start != ends[-1]):
					print("Input error parameters discontinuities")
				else:
					ends.append(end)
					limited.append(speed)
					index = index -1
			else:
				ends.append(end)
				limited.append(speed)
				index = index -1

	if(len(ends) == count):
		end = 0
		start = 0

		while True:
			try:
				start , end = (int(x) for x in input().split(' '))
			except Exception as ret:
				print("input error parameters")
			else:
				if start <= end:
					break

		if start == end:
			print("time is 0")
		else:
			# 因为是连续的
			# 所以只记录一个阶段截止的值 于 s[i]
			# limit[i]存放从s[i - 1]到s[i]的速度限制
			# 拿数组下标做逻辑应该是时间复杂度和空间复杂度都比较低的一种
			time = 0
			i = 0
			while i<len(ends):
				if start <= ends[i]:
					if (end >= ends[i]):
						time += (ends[i]-start)/limited[i]
						start = ends[i]
					else:
						time += (ends[i]-end)/limited[i]
						break
				i = i + 1
			print("time is %.2f hour"%time)

if __name__ == '__main__':
	main()
