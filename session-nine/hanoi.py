def main():
	# Solve the Towers of Hanoi puzzle for five disks
	# from peg A to peg C using extra peg B
	towers(5, "A", "B", "C")

def towers(numdisks, startpeg, extrapeg, endpeg):
	if numdisks == 1:
		print("Move a disk from", startpeg, "to", endpeg)
	else:
		towers(numdisks - 1, startpeg, endpeg, extrapeg)
		print("Move a disk from", startpeg, "to", endpeg)
		towers(numdisks - 1, extrapeg, startpeg, endpeg)		

if __name__ == "__main__":
	main()
