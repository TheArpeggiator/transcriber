frets = [['E4','F4','F#4','G4','G#4','A4','A#4','B4'],
		['B3','C4','C#4','D4','D#4','E4','F4','F#4'],
		['G3','G#3','A3','A#3','B3','C4','C#4','D4'],
		['D3','D#3','E3','F3','F#3','G3','G#3','A3'],
		['A2','A#2','B2','C3','C#3','D3','D#3','E3'],
		['E2','F2','F#2','G2','G#2','A2','A#2','B2']]

def find_pos(note):
	pos = 999
	base = 999
	for i in range(5):
		for j in range(7):
			if note == frets[i][j]:
				if(j<pos):
					pos = j
					base = i
	return base+1, pos
	#print note