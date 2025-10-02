# pyzk2

`pyzk2` is a forked version of [pyzk](https://github.com/fananimi/pyzk) as the original repository is upto date but has not published a new release on PYPI.
All credit to original author.

# Installation

* pip
```sh
pip install pyzk2
```

## Basic Usage

The following is an example code block how to use pyzk2.

```python
from pyzk2 import ZK, const

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=15, password=0, force_udp=False, ommit_ping=False)
try:
    conn = zk.connect()
    print ("-- Device Information --")
    print ("   Current Time            : %s" % conn.get_time())
    print ("   Firmware Version        : %s" % conn.get_firmware_version())
    print ("   Device Name             : %s" % conn.get_device_name())
    print ("   Serial Number           : %s" % conn.get_serialnumber())
    print ("   Face Algorithm Version  : %s" % conn.get_face_version())
    print ("   Finger Algorithm        : %s" % conn.get_fp_version())
    print ("   Platform Information    : %s" % conn.get_platform())
    print ("   Users list              : %s" % conn.get_users())
    print ("   Attendance data         : %s" % conn.get_attendance())
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
```

# Code Examples

You can find all code examples in example directory.
