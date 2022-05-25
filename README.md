# GoogleDDNS
Google DDNS update client for GoogleDomains(Support Linux/macOS)

## Features
- Efficient DDNS client
- Use reliable APIs for accuracy

## TO DO
- [ ] IPv6 Support
- [ ] Refactor Shell versions to support OpenWRT

## Usage
1. You need to add a dynamic domain resolution in [Google Domains](https://domains.google.com/).

![ac9faa5b6bc07de370aa3](https://telegraph.eowo.us/file/ac9faa5b6bc07de370aa3.png)

2. Check out the dynamic domain names you have added.

![9478ee671465b7309b9e7](https://telegraph.eowo.us/file/9478ee671465b7309b9e7.png)

3. Write down your username and password.

![bf153c173cc8b19a49ed0](https://telegraph.eowo.us/file/bf153c173cc8b19a49ed0.png)

4. Fill in the `GoogleDDNS.py` file with the hostname, username and password you recorded.
~~~python
# The domain name you want to update
HOSTNAME = "yourdomainname.com"
# Your Google Domains username(Not Google account)
USERNAME = "yourusername"
# Your Google Domains password
PASSWORD = "yourpassword"
~~~

5. Install the required dependencies to run.
~~~shell
pip3 install requests
~~~

6. [Recommended] Add to `Crontab`.
~~~
*/1 * * * * python3 GoogleDDNS.py
~~~

## Thanks
- [IP.SB](https://ip.sb): Free IP lookup interface provided

## License
[Apache License 2.0](https://github.com/missuo/GoogleDDNS/blob/main/LICENSE)
