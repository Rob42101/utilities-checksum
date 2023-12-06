# utilities-checksum

This application provides any easy to use GUI for checking the hash values of any file. The use case is for when you download a file for which the author has provided a checksum value: this app will generate the hash value of the downloaded file (on the local host machine) and allow you to simply paste in the publish hash value. It will then compare the two values and indicate if they are a match, not not a match.

Although PGP signature files are becoming more popular, you'll still come across this kind of file verification and this app is an easy and pleasant way to use this time honored process.

It supports four hash digests:

- MD5
- SHA-1
- SHA-256
- SHA-512

The app has been written in Python3 code and uses the Tkinter framework for the GUI, with a minimum of dependencies. I used the a GUI design application called PAGE and you'll find some details about that in the main `README.md` page for this repository.

Apps written using PAGE, have two `.py` files; both are required in order to run the app.

For this app, the two files are:

`checksum.py`

`checksum_support.py`

There is also a `icons` folder and all three of these need to be in the same location of your file system.
