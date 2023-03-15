import requests

"""
    Try to get the public IP address of the machine
"""


def get_ip():
    ip = _ipify()
    if ip == None:
        ip = _ipecho()
        if ip == None:
            ip = _ipinfo()
            if ip == None:
                ip = _ipconfig()
                if ip == None:
                    return 'ERROR : Unable to get the public IP from multiple services. pls check my internet connection! Ooops but If I am not connected to the internet, How can you see this message! Wierd!'
    return ip


def _ipify():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def _ipecho():
    url = 'https://ipecho.net/plain'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def _ipinfo():
    url = 'https://ipinfo.io/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def _ipconfig():
    url = 'https://ifconfig.me/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
