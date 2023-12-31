#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Dec 05, 2023 01:41:39 AM GMT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import checksum
import os
import hashlib
from datetime import datetime
from tkinter import filedialog
from pathlib import Path
from configparser import ConfigParser

location = os.path.dirname(os.path.realpath(__file__))
_debug = False  # False to eliminate debug printing from callback functions.


def main(*args):
    """main entry point for the application
    """
    if _debug:
        print(main.__name__)
        print(f"\t{main.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = checksum.Toplevel1(_top1)
    start_up()  # added code line
    root.mainloop()


def start_up(*args):
    """application initialization
    """
    if _debug:
        print(start_up.__name__)
        print(f"\t{start_up.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    _w1.text_hash_digest.set("Hash digest:")
    if not _w1.text_file_path.get():
        _w1.text_file_attributes.set(f"Date:          \tSize:")
    ini_load()
    banner = """
    ============================================
    Running Checksum, file hash verification app
    ============================================
    """
    print(banner)
    if _debug:
        print("Debugging mode is enabled.\n")
    else:
        print("Debugging mode is disabled.\n")
    print("Dependencies...")
    print(sys.__name__)
    print(os.__name__)
    print(hashlib.__name__)
    print(datetime.__name__)
    print(Path.__name__)
    print(ConfigParser.__name__)
    print(tk.__name__, "    v" + str(float(tk.TkVersion)))
    print(ttk.__name__, "v" + ttk.__version__)
    print()
    print("GUI designed using the PAGE framework, version 7.6")
    print("https://sourceforge.net/projects/page/")
    print()


def config(*args):
    """create or edit the config.ini file
    """
    if _debug:
        print(config.__name__)
        print(f"\t{config.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()

    def file_save():
        content = text.get('0.1', tk.END).split("\n")
        with open("config.ini", mode="w", encoding="UTF-8") as output:
            for line in content:
                if line:
                    print(line, file=output)
        if _debug:
            print("config.ini file saved")
        window.destroy()
        start_up()
    root_dir = ini_load()
    window = tk.Tk()
    window.title("config.ini editor")
    window.geometry("600x160")
    window.resizable(False, False)
    window.configure(background="#313338")

    text = tk.Text(window)
    text.configure(
        font="-family {DejaVu Sans} -size 12",
        foreground="#babdb6",
        background="#555753",
        relief="solid",
        height=5,
        width=56,
        padx=2,
        pady=10,
        borderwidth=2
    )

    save = tk.Button(window)
    save.configure(
        text="Save",
        font="-family {DejaVu Sans} -size 12",
        foreground="#babdb6",
        background="#313338",
        activeforeground="#44AD4D",
        activebackground="#313338",
        highlightbackground="#313338",
        height=1,
        width=2,
        borderwidth=0,
        command=file_save
    )

    text.grid(row=0, column=0, padx=1, pady=1)
    save.grid(row=1, column=0, padx=280, pady=4, sticky="w")
    text.insert("0.1", f"[root]\nroot = {root_dir}")
    text.focus()
    window.mainloop()


def ini_load(*args):
    """check for a valid config.ini file
    conditional app object update
    """
    if _debug:
        print(ini_load.__name__)
        print(f"\t{ini_load.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    example_config = """
    [root]
    root = /home/user_name/Downloads/
    """
    errors = {}
    config_file = 'config.ini'
    if Path(config_file).exists():
        config_file_exists = True
    else:
        config_file_exists = False
        errors["config_file_missing"] = "config.ini file not found"
    if config_file_exists:
        # read it
        config = ConfigParser()
        try:
            config.read(config_file, encoding="UTF-8")
            root_dir_read = config['root']['root']
            config_file_error = False
        except Exception as Exception_error:
            config_file_error = Exception_error.args
            root_dir = False
            root_dir_read = False
            errors["config_file_error"] = config_file_error
        if os.path.isdir(root_dir_read):
            root_dir_error = False
        else:
            root_dir_error = True
            errors["root_dir_error"] = root_dir_read
        if root_dir_read == location:
            errors["fallback"] = True
    if errors:
        root_dir = location
    else:
        root_dir = root_dir_read
    if errors:
        if _debug:
            print("\tError report:")
            for error in errors:
                print("\t\t", f"{error}: {errors[error]}")
            print()
            print(f"\tusing fallback: '{root_dir}'")
        if "root_dir_error" in errors:
            _w1.text_w_dir.set(" invalid path. using fallback")
            _w1.working_dir.configure(foreground="#EF2929")
        elif "config_file_missing" in errors:
            _w1.text_w_dir.set(f"{errors['config_file_missing']}: using fallback")
            _w1.working_dir.configure(foreground="#EF2929")
        elif "fallback" in errors:
            _w1.text_w_dir.set("config.ini file is set to the fallback location")
            _w1.working_dir.configure(foreground="yellow")
    else:
        _w1.text_w_dir.set("config.ini file is valid")
        _w1.working_dir.configure(foreground="#689fdc")
    return root_dir


def file_open(*args):
    """display the filedialog.askopenfilename() widget
        update the filePath object by setting `text_file_path`
        hand off to 'file_status' with a call to os.stat(file)
            'file' stores the return value of 'filedialog.askopenfilename()'
    """
    if _debug:
        print(file_open.__name__)
        print(f"\t{file_open.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    filetypes = [
        ('All files', '*.*'),
        ('Python files', '*.py'),
        ('Tar archive', '*.tar.gz'),
        ('Zip archive', '*.zip'),
        ('Exe files', '*.exe'),
        ('Text files', '*.txt'),
    ]
    filetypes.sort()
    file_path = ini_load()
    file = filedialog.askopenfilename(
        title="Select file",
        initialdir=file_path,
        filetypes=filetypes
    )
    _w1.text_file_path.set(file)
    if file_selectd():
        file_status(os.stat(file))


def file_status(*args):
    """process the os.stat_result() and update the file attributes object
       hand off to hash_gen()
    """
    if _debug:
        print(file_status.__name__)
        print(f"\t{file_status.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    output = "Date: "
    byts = args[0].st_size
    date, time = str(datetime.fromtimestamp(args[0].st_ctime)).split(" ")
    y, m, d = date.split("-")
    output += f"{d}-{m}-{y}\t"
    kb = byts / 1000
    mb = kb / 1000
    gb = mb / 1000
    if int(gb) > 0:
        output += f"Size: {gb:0.2f} GB"
    elif int(mb) > 0:
        output += f"Size: {mb:0.2f} MB"
    elif int(kb) > 0:
        output += f"Size: {kb:0.2f} kB"
    else:
        output += f"Size: {byts} bytes"
    _w1.text_file_attributes.set(output)
    hash_gen()


def hash_gen(*args):
    """generate the file hash digest and update the hash value object
        the values from text_selected_hash.get() are:
            0:MD5 | 1:SHA-1 | 2:SHA-256 | 3:SHA-512
    """
    if _debug:
        print(hash_gen.__name__)
        print(f"\t{hash_gen.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    if file_selectd():
        file_name = _w1.text_file_path.get()
        if not _w1.text_selected_hash.get():
            ht = 0
        else:
            ht = _w1.text_selected_hash.get()
        hash_type = [hashlib.md5(), hashlib.sha1(), hashlib.sha256(), hashlib.sha512()]
        h_lib = hash_type[ht]
        with open(file_name, 'rb') as file:
            # loop till the end of the file
            rBytes = 0
            while rBytes != b'':
                # read 1024 bytes at a time
                rBytes = file.read(1024)
                h_lib.update(rBytes)
        hash_digest = h_lib.hexdigest()
        if _debug:
            print(hash_digest)
        _w1.text_hash_digest.set(f"Hash digest:\n{hash_digest}")


def verify(*args):
    """compare the hash values and do a conditional format of the font
    colour held in the published_hash_entry object
    """
    if _debug:
        print(verify.__name__)
        print(f"\t{verify.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    file_hash, pub_hash = _w1.text_hash_digest.get(), _w1.published_hash_entry.get('1.0', tk.END)
    if file_selectd():
        pub_hash = pub_hash.strip()
        if file_hash and pub_hash:
            file_hash = file_hash.split("\n")[1]
            if file_hash == pub_hash:
                _w1.published_hash_entry.configure(foreground="#8AE234")
            else:
                _w1.published_hash_entry.configure(foreground="#F8374B")
    else:
        _w1.published_hash_entry.delete('1.0', tk.END)
        _w1.published_hash_entry.configure(foreground="#babdb6")


def file_selectd(*args):
    """check that a valid file path has been selected
    conditional update of the app objects
    """
    if _debug:
        print(file_selectd.__name__)
        print(f"\t{file_selectd.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    fs = False
    nfs = "No file selected"
    file_name = _w1.text_file_path.get()
    if file_name and file_name != nfs:
        fs = True
    else:
        _w1.text_file_path.set(nfs)
        _w1.text_hash_digest.set("Hash digest:")
        _w1.published_hash_entry.delete('1.0', tk.END)
        _w1.text_file_attributes.set(f"Date:          \tSize:")
        _w1.published_hash_entry.configure(foreground="#babdb6")
    return bool(fs)


def quit(*args):
    """app exit point
    """
    if _debug:
        print(quit.__name__)
        print(f"\t{quit.__doc__}")
        for index, arg in enumerate(args):
            print(f"\targ {index}:\n\t{arg}\n")
        sys.stdout.flush()
    sys.exit("Checksum: clean exit")


if __name__ == '__main__':
    checksum.start_up()
