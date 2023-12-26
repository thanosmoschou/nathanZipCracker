Nathan Zip Cracker

This is a simple zip cracking tool made with Python.

How to run it:

```
python3 nathan.py -f /path/to/file.zip -l /path/to/dictionary.txt
```


Disclaimer:

This is a proof of concept and is made for educational purposes only. <br>
I am not responsible for any harm you may cause by using this program. <br>
Use it at your own risk. Also keep in mind that this program is not as fast as other tools when you specify a big dictionary. <br>
For a zip with password Maria123 and rockyou.txt as the dictionary list, it needs about 28-35 seconds (Brute Force side effects). Other tools need about 3-4 seconds. <br>
For a zip with password aaaaaaaaaa and rockyou.txt as the dictionary list, it needs about a second. Other tools need about half a second or less. <br>


Possible improvements:

Use threading in order to make it faster