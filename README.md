guitar notes transcriber
=============

Basic implementation of the aubio library to try and map notes played on the guitar to the top half of the guitar fretboard. The use of the base frequency identifier and the onset detector has been from the python extension of the aubio library. Any code on top of that has been to augment the use of the library to estimate where the notes are positioned on the guitar fretboard.

**Disclaimer**
This project is still under works, a LOT of things don't work as they are supposed to, there is no distinguished UI (Blame it on the lack of personnel AND TIME!), but everything works as it should in the terminal.

Implementation and Design Basics
--------------------------------

The code has been written in Python and I have tried to comment as much as I can to explain what happens where!
Please make sure that you have the aubio python extension installed along with Matplotlib and Numpy.

sudo pip install aubio

p.s. make sure you have pip installed as well (duh!)

run code as -
python pitchDetector.py audio_file_path


Credits
------------------------

Core work on the frequency note conversion to MIDI and using the Onset Detector to map these recognised notes have been done by myself and my colleague Sujith Sajeev.

Additional credit to Sayeram Eswar for initial help in conceiving this project idea and helping with the final plotting of the notes using Matplotlib.

Without the help of Paul Brossier's aubio library this project would not have been possible. Thanks Paul!


Contact Info and Email Address
-----------------------------

Sujith Sajeev - sujithishtar3@gmail.com
Sayeram Eswar - sayeram.eswar1@gmail.com

Rahul Agnihotri (myself) - raul.agni12@gmail.com

Copyright and License Information
---------------------------------

this is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
