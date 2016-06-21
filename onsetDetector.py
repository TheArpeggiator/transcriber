#! /usr/bin/env python

import sys
from aubio import source, onset

#create sample space for onsets
onsets = []

def get_onset(name):
	win_s = 512                 # fft size
	hop_s = win_s / 2           # hop size

	filename = name

	samplerate = 0

	s = source(filename, samplerate, hop_s)
	samplerate = s.samplerate

	o = onset("default", win_s, hop_s, samplerate)

	# total number of frames read
	total_frames = 0
	while True:
	    samples, read = s()
	    if o(samples):
	        #print "%f" % o.get_last_s()
	        onsets.append(round(o.get_last_s(),4))
	    total_frames += read
	    if read < hop_s: break

	return onsets