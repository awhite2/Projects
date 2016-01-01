This directory contains two kinds of word lists.

* Those files beginning with the name "words" are
  human-readable alphabetically sorted English word 
  lists in which one word appears in each line of the file.
  
  The file "words.txt" is the same as the Linux word list
  that can be found in the file /usr/share/dicts/linux.words
  on many Linux systems. This fairly extensive list contains
  454245 words, but there are still many words that it is missing.
  
  The files named "words5.txt", "words6.txt", etc. are subsets
  of "words.txt" containing words of up to 5, 6, etc. characters
  that do not begin with a capital letter. 
  
  	+ words5.txt contains 5525 words
  	+ words6.txt contains 10488 words
	+ words7.txt contains 16618 words
	+ words8.txt contains 22641 words
	
* Those files begining with the name "dict" are versions of the 
  "words" files that are intended to be read only by 
  the computer. These files encode the word lists in a manner that
  makes it very easy for a program to construct a tree that can
  efficiently test whether a given string is in the word list or not. 
  The "dict" files are automatically produced from the "words" files. 

  N.B. The "dict" files *must* end in ".bin" to be
  transferred correctly (in binary, raw mode) by Mac Fetch. 