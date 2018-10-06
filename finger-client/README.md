Finger Client
-------------

Requirements:
```bash
$ sudo apt-get install python-minimal # Or install python2.7 using any package manager
$ cd finger-client
$ chod +x finger-client # If the file is not executable
```

Executable
```bash
$ ./finger-client
$ ./finger-client [user]
$ ./finger-client [user@host]
```

How to make executable:
* Add line __#!/usr/bin/python2__ in the first line of __finger-client__ file
* Remove extension __.py__ from file name
* Make file excutable with command __chomd +x finger-client__

Source code:
* Python source code can be found in __finger-client.py__ file
```bash
$ python2 finger-client.py
```
