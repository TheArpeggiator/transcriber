#import required python scripts for execution
import sys, Notes, math, onsetDetector, frets, draw
from aubio import source, pitch, freqtomidi

#set sample space
Notes.sample_space()

if len(sys.argv) < 2:
    print "Usage: %s <filename> [samplerate]" % sys.argv[0]
    sys.exit(1)

filename = sys.argv[1]

#get onsets of notes
onsets = onsetDetector.get_onset(filename)

#set sample rate for analysis
downsample = 1
samplerate = 44100 / downsample
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])

win_s = 4096 / downsample # fft size
hop_s = 512  / downsample # hop size

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

pitch_o = pitch("yin", win_s, hop_s, samplerate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)

pitches = []
confidences = []
timestamp = []
base = []
pos = []
t = 0

# total number of frames read
total_frames = 0
ons = 1

#endless loop to find notes and match to position on guitar fretboard
while True:
    samples, read = s()
    pitch = pitch_o(samples)[0]
    pitch = int(round(pitch))
    confidence = pitch_o.get_confidence()
    t = total_frames / float(samplerate)
    
    """
    THIS IS TESTER CODE, LEAVE AS IT/EDIT IF YOU ARE SMART ENOUGH!!!!!!!

    if confidence > 0.85 and pitch > 0:
    	note,octave = Notes.match_note(pitch)
        if ((ons < len(onsets)) and (float(t) > float(onsets[ons]))):
            #print "%.4f %d %s%d %.4f" % (t, pitch, note, octave, confidence)
            print "%f" % onsets[ons] 
            ons+=1
            
            b, p = frets.find_pos(note + str(octave))
            if(b<1000):
                print "%d %d %f" % (b, p, t)
                timestamp.append(round(t,4))
                base.append(b)
                pos.append(p)
            ons+=1
    """

    if (ons<(len(onsets)) and float(t) > float(onsets[ons]) and confidence > 0.6):
        note,octave = Notes.match_note(pitch)
        print "%.4f %d %s%d %.4f" % (t, pitch, note, octave, confidence)
        b, p = frets.find_pos(note + str(octave))
        if(b<1000):
            #print "%d %d %f" % (b, p, t)
            timestamp.append(round(t,4))
            base.append(b)
            pos.append(p)
        ons+=1
    
    pitches.append(pitch)
    confidences.append(confidence)
    total_frames += read
    
    if read < hop_s: break

#show tabs
draw.plot_tabs(base,pos,timestamp,t,filename)