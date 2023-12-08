# utilities-checksum

This application provides an easy to use GUI for checking the hash values of any file. The use case is for when you download a file for which the author has provided a checksum value: this app will generate the hash value of the downloaded file (on the local host machine) and allow you to simply paste in the published hash value. It will then compare the two values and indicate if they are a match, or not a match.

Although PGP signature files are becoming more popular, you'll still come across this kind of file verification and this app is an easy and pleasant way to use this time honoured process.

The app supports four hash digests:

- MD5
- SHA-1
- SHA-256
- SHA-512

... and has been written in Python3 code, using the Tkinter framework for the GUI. I have kept the dependencies to the minimum and used standard Python libraries, so there should be no `pip install` requirements. As for the app itself, again, there are no install requirements, per se, but a working Python3 environment is a given, along with the Tkinter framework.

To create this app, I used a GUI design application called PAGE and you'll find some details about that in the `README.md` page for my `utilities` repository, of which this is a sub-section.

Apps written using PAGE, have two `.py` files; both are required in order for said app to run.

For this app, the two files are:

`checksum.py`

`checksum_support.py`

Either can be used to run the app, but `checksum.py` should be considered as the 'application' file: it creates the GUI front end, while the `_support.py` file can be considered as the 'driver', so to speak.

The application can be launched as is, by granting the `checksum.py` file 'executable' permission, or it can be launched from a command line, via your `python3` interpreter, without elevated privileges.

As a part of this application, there is also a `icons` folder (which speaks for itself) and all three of these objects should reside in the same location of your file system, where said location does not need, again, any elevated user privileges.

There is just one file that you need to create for yourself: `config.ini`, which is a very simple 'text' based file. It's used as a pointer to whatever default directory you choose as a working directory (possibly, you should choose your downloads directory). If the `config.ini` file is either missing or incorrectly formatted, the app will indicate that and use the directory in which it resides, as its default working directory.

I have provided an in-app editor for the `config.ini` file; alternatively, you can create it with any standard text editing application. Please ensure that you use the `UTF-8` character encoding standard, which is the default with most text editors.

### Controls & Usage

There are four control buttons; from left to right:

- `config.ini` editor
- File search & load
- Hash digest comparison check
- App exit

When you first launch the application, if the `config.ini` file has not been created, you will see a message, in red, to inform you of this, and the app will default to its own file location: the 'fallback'. Clicking the left icon will launch the editor, which will be pre-loaded with a correctly formatted `.ini` file. Clicking `Save` will then save that file, and the information message will turn yellow and tell you that the fallback file location is active. Changing the `.ini` file, before you save it, to a valid file path, will turn the information message blue, indicating that the file location is anything other than the fallback. If a invalid file path is provided in the `.ini` file, the information message will be displayed in Red and the application will once again use its fallback location.

Here is an example of a correctly formatted `config.ini` file:

```
[root]
root = /home/marvin/Downloads/
```
The File search & load (the first button in the group of three on the right) will open a 'Select file' widget, from which you can navigate to the file for which you need a hash digest. Once selected, the app will display the file path, file date stamp and file size. The MD5 Hash digest will also be displayed and you can select any one from the other three on offer.

**Please note:** With larger files (size > 100 MB) it will take a noticeable about of time to generate the hash digest. There is no known (by me) file size limit (computer RAM/swap space not withstanding) but logically, the larger the file for which you need a hash value, the more time it's going to take to generate said hash value. This app will freeze while the hash digest is being created, which is does in buffered, 1024 byte, chunks. This has been done as a system load management measure, so that if one does need to create a hash value for a large file, the RAM/swap file space requirements are minimised, so please be patient if you use large file sizes: it may take five seconds or more, to process a gigabyte of data.

The box below the Hash digest is where you enter the published hash value, which you should obtain from the same location from which you downloaded the file that you are now checking.

The SHA-256 hash values for my application files are as follows:

`checksum.py`:

`066e3e2c73b4d319dc91cc7ec6c5fcc91ca0cc7672c43cc0bc58cad2df902ad3`

`checksum_support.py`:

`c1b24bd1e3c216376919fafa13a3b0373787230c832ea06943ac5ed559d7d29d`

`checksum.zip`:

`1884d796f7b3decf44c476931da7274c7953a5b326abf2fe05499be080810226`

C&P the published hash value into the light blue box and press the Green Shield icon to check that the two values are a match. If the text in the light blue box turns Red, it indicates that there is a mismatch between the calculated hash digest and the published one. You should be **VERY** wary about that, because it could mean that an unauthorised change has been made to the file that you have downloaded. Check that you have not made an error and contact the files's author, to let them know of the issue. 

If all is well, the text will turn Green and you will know that the file that you have just downloaded has not been changed since the published hash value was generated.

The Red 'off' button should need no explanation.

Thank you for your interest in this and I trust the you will enjoy using my creation.
