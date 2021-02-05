# sklylnader
A kly (kommand line ynterface) to read and write skylanders using an arduino and rc522

This is based on nfc.toys project 


## sklykeys.py
This software is for educational purposes.
sklykeys.py creates a file that include the keys from your skylander copy.
```
sklykeys.py a cli interface for tnp3xxx.py library from nfc.toys 
that allows us to read a copy in binary mode and write in eml format
or in binary format
  -u uid (6 bytes in hex) prints keys in stdout
  -f file read from file (in binary mode)
  -t file write to file otherwise to stdout
  -b output format binary otherwise in Proxmark emulator format (EML)
example: ./sklykeys.py -f spiro.bin -t spiro_keys.bin -b
```