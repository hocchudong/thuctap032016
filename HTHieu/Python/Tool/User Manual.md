# Hướng dẫn dùng tool

## Cài đặt môi trường

- Yêu cầu cần có `Python 2.7` cùng các thư viện sau: `paramiko, pyside`

- Chú ý để chạy các lênh python một cách dễ dàng thì dùng `power shell` với `run with addmin`

- Cách 1: Dùng lệnh `python <dường dẫn tool.py>` ví dụ file `tool.py` có đường dẫn:

 `f:\workspace\testplace\tool.py` ta có lệnh `python f:\workspace\testplace\tool.py`

Cách này đơn giản dễ dùng nhưng mỗi lần chạy là phải thục hiện lênh `python`

- Cách 2: Dùng `p2exe` để chạy < Cách này chỉ dùng trên `Window` >

Tạo một file `.py` bằng `notepad` và copy đoạn code sau:

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
<p>
Dùng lệnh `python <dường dẫn file .py>`

Đoạn script này để khai báo registry cho `python

Download `py2exe` tại link https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/

Chạy như file vừa down về 

Để chạy `tool` dùng lệnh `python tool.py py2exe` 

C2 thực hiện phức tạp hơn nhưng sau khi hoàn thành ta có 1 file `exe` không phải thực hiện bất cứ lệnh 
nào để chạy
</p>

- Hướng dẫn sử dụng

B1: Đăng nhập

<img src=http://imgur.com/xJNXXDH.png>

B2: Lấy file về

<img src=http://i.imgur.com/2zBuLPk.png>

Tìm kiếm

<img src=http://imgur.com/zShdEws.png>

Thay thế:

<img src=http://imgur.com/kbQZccz.png>

B3: Đẩy file sau chỉnh sửa lên máy remote

<img src=http://imgur.com/Q7GjnEP.png>

Kết quả :

<img src=http://imgur.com/t8IOeLM.png>

