# secretum
Complex password generator

## Install

```
python3.8 -m pip install git+https://github.com/jxlil/secretum.git --user
```

## Usage
```
usage: secretum [-h] -k KEY -l LOGIN [--length LENGTH] [-v]

Complex password generator

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY
                        set keyfile/keyword
  -l LOGIN, --login LOGIN
                        set login for which you will use password
  --length LENGTH       set password length
  -v, --version         show program's version number and exit
```

## Example
```bash
# any file can be used as a keyfile
$ secretum -k photo.jpg --login example@domain.com

# or you can use a keyword
$ secretum -k blueeyes --login example@domain.com
```

**Warning:**

Modifying your keyfile generates a different password
```bash
$ secretum -k key.txt --login gmail
# d1d400d2d0a992fa87d1e19f209b6e0b48c3e0ca1a674f5b1df37e083656ed85

$ echo "0" >> key.txt
$ secretum -k key.txt --login gmail
# 5c5b1433e509752827cc015efb752912c0a271790baddd6759e8c9c713688989
```

---

