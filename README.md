 
<p align="center">
  <img  width="100" height="100" src="logo/llave.svg" />
</p>

# secretum
Complex password generator

## Install

```
pip3 install git+https://github.com/x-jalil/secretum.git --user
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
$ secretum -k photo.jpg --login gmail

# or you can use a keyword
$ secretum -k blueeyes --login gmail
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

## Author

**Jalil SA**

Do you want to support this project? You can send a **pull request**, write an **issue** or just **buy me a coffee**!


<a href="https://www.buymeacoffee.com/jxlil" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-2.svg"></a>


