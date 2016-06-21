import numpy

#create sample space for midi to frequency matching
notes = numpy.zeros(shape=(12,11)) 

#base notes values created in char array
m_notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
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
				return i,j

def match_note(note):
	n,octave = find_note(note)
	octave-=1

	return m_notes[n],octave