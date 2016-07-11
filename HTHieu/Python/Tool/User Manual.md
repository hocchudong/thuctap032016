# Hướng dẫn dùng tool

- Yêu cầu cần có `Python 2.7` cùng các thư viện sau: `paramiko, pyside`

- Chú ý để chạy các lênh python một cách dễ dàng thì dùng `power shell` với `run with addmin`

- C1: Dùng lệnh `python <dường dẫn cái tool>`

- C1: Đơn giản dễ dùng nhưng mỗi lần chạy là phải thục hiện lênh

- C2: Dùng `p2exe` để chạy

<ul>
<li>chạy đoạn script có nội dung như sau bằng lênh `python + <đường dẫn của script>`:</li>
</ul>

```sh
import sys

from _winreg import *

# tweak as necessary

version = sys.version[:3]

installpath = sys.prefix

regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)

installkey = "InstallPath"

pythonkey = "PythonPath"

pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (

    installpath, installpath, installpath

)

def RegisterPy():

    try:

        reg = OpenKey(HKEY_CURRENT_USER, regpath)

    except EnvironmentError as e:

        try:

            reg = CreateKey(HKEY_CURRENT_USER, regpath)

            SetValue(reg, installkey, REG_SZ, installpath)

            SetValue(reg, pythonkey, REG_SZ, pythonpath)

            CloseKey(reg)

        except:

            print "*** Unable to register!"

            return

        print "--- Python", version, "is now registered!"

        return

    if (QueryValue(reg, installkey) == installpath and

        QueryValue(reg, pythonkey) == pythonpath):

        CloseKey(reg)

        print "=== Python", version, "is already registered!"

        return

    CloseKey(reg)

    print "*** Unable to register!"

    print "*** You probably have another Python installation!"

if __name__ == "__main__":

    RegisterPy()
```
<ul>
<li>Download `py2exe` tại link https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/</li>
<li>Chạy như file exe bình thường</li>
<li>Để chạy tool dùng lệnh ```
python tool.py py2exe
```</li>
</ul>
- C2 thực hiện phức tạp hơn nhưng sau khi hoàn thành ta có 1 file `exe` không phải thực hiện bất cứ lệnh nào để chạy
