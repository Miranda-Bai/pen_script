#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getMorse(image):
  """Get morse out of image

  This assumes the background colour is static and morse code has a different colour.
  Morse code can be in any colour, as long as it is not the same as the top-left pixel.


  >>> getMorse('pwd.png')
  ['----.']

  """

  from PIL import Image
  import re

  im = Image.open(image, 'r')

  chars = []
  background = im.getdata()[0]

  for i, v in enumerate(list(im.getdata())):
    if v == background:
      chars.append(" ")
    else:
      chars.append("*")

    # print "{0: <4}: {1: <15} ({2})".format(i, v, "[-] BG" if v == background else "[+] FG")

  output =  "".join(chars)

  # Clean output by removing whitespace front and back
  # Then make dash out of every combination of 3 dots
  # Convert dots to actual dot
  # Convert whitespace between letters (i.e. >1 bg pixel) to seperator
  # Remove whitespace
  # Return list of letters
  output = re.sub(r'^\s*', '', output)
  output = re.sub(r'\s*$', '', output)
  output = re.sub(r'\*{3}', '-', output)
  output = re.sub(r'\*', '.', output)
  output = re.sub(r'\s{2,}', ' | ', output)
  output = re.sub(r'\s', '', output)
  output = output.split('|')

  return output

def getPassword(morse):
  """Decode morse

  Convert morse back into text.
  Takes list of letters as input, returns converted text.

  Note that challenge uses lowercase letters.

  >>> getPassword(['----.'])
  '9'

  """
  MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-..-.': '/', '.-.-.-': '.', '-.--.-': ')', '..--..': '?',
    '-.--.': '(', '-....-': '-', '--..--': ','
  }

  for item in morse:
    return "".join([MORSE_CODE_DICT.get(item) for item in morse]).lower()

def main():
  """ Auto start

  Used for automation.
  Automatically call methods and use 'pwd.png' as input image.

  """
  print getPassword(getMorse("pwd.png"))


if __name__ == "__main__":
  main()


