# sklylander
A kly (kommand line ynterface) to read and write skylanders using an arduino and rc522

This is based on nfc.toys project 
and you also need a mfrc522cli:
https://github.com/elbuit/mfrc522cli




## sklykeys.py
This software is for educational purposes.
sklykeys.py creates a file that include the keys from your skylander copy.
```
sklykeys.py a cli interface for tnp3xxx.py library from nfc.toys 
that allows us to read a copy in binary mode and write in eml format , binary format or mfrc522cli format
  -h prints this help
  -u uid (6 bytes in hex) prints keys in stdout
  -f file read from file (in binary mode)
  -t file write to file otherwise to stdout
  -o output format binary, eml or mfrc522cli format. Default Proxmark emulator format (EML)

example: ./sklykeys.py -f spiro.bin -t spiro_keys.m5c -o mfrc522cli

```




# examples
## How to make a backup of your favourite Skylander
https://toni.cunyat.net/2021/03/make-backup-of-your-favourite.html