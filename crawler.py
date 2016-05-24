__author__ = 'xudongwu'

import sys
import urllib
import json

url_base = "http://dict-co.iciba.com/api/dictionary.php?key=50047AA12F0CBAF069B6052DC978EDAE&type=json&w="

out = open(sys.argv[2], mode='w')
for line in open(sys.argv[1]):
    word = line;
    result = json.load(urllib.urlopen(url_base + word))
    if 'word_name' in result:
        word_name = result['word_name']
        definition = result['symbols'][0]
        pronunciation = definition['ph_am']
        parts = definition['parts']

        out.write("Q: " + word )
        if pronunciation is None:
            out.write(("A: " + word_name + "<br/>").encode('utf8'))
        else:
            out.write(("A: " + word_name + " | " + pronunciation + "<br/>").encode('utf8'))

        for part in parts:
            form = part['part']
            meaning = part['means']

            out.write(("<br/>" + form + " " + ";".join(meaning)).encode('utf8'))

        out.write('\n\n\n')

