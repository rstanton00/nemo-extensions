#!/usr/bin/python

#only for my work locally!!!
import glob

import os
import urllib
#import nemo
from gi.repository import Nemo, GObject, Gtk, GdkPixbuf
# for id3 support
#import mutagen
from mutagen import File
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MPEGInfo
from mutagen.oggvorbis import OggVorbis
# for exif support
import pyexiv2
# for reading videos. for future improvement, this can also read mp3!
import kaa.metadata
# for reading image dimensions
import Image
# for reading pdf
try:
	from pyPdf import PdfFileReader
except:
	pass

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

directory = "/home/rstanton/Music/adorno_weisler/_Theodor_Adorno_and_Hanns_Eisler_Works_for_String_Quartet"

for sFile in os.listdir(directory):
  print "we are looking at " + sFile
  #sFile = 'file:/' + directory + '/' + sFile
  sFile = directory + '/' + sFile
  print "sFile is now: " + sFile
  fileSize = os.path.getsize(sFile)
  print "file size is: ", fileSize
  if not fileSize < 0:
    result = File(sFile, easy=True)
    print result
    #osFile = file(sFile)
    #print "searching for file type"
    #print type(osFile)
    #if osFile.is_mime_type('audio/mpeg'):
    #  print osFile

# strip file:// to get absolute path
#filename = urllib.unquote(file.get_uri()[7:])
