import numpy

notes = numpy.zeros(shape=(12,11))
count = 0

def sample_space():
	global count
	for i in range(11):
		for j in range(12):
			notes[j][i] = count
			count = count + 1
			if count == 128:
				break
		if count == 128:
			break

def find_note(note):
	for i in range(12):
		for j in range(11):
			if note == notes[i][j]:
				return (i,j)