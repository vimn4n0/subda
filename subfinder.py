from coconut import *
from modules import subdomains,     findSubdomains

line        = "-" * 69
user_agent  = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
_headers    = {
    'User-Agent': user_agent,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

def heading(heading, host, color, afterWebHead):
    space = " " * 15
    var = str(space + heading + " '" + host + "'" + str(afterWebHead) + " ..." + space)
    length = len(var) + 1; print() # \n
    print(f"{w}" + "-" * length + "-")
    print(f"{color}" + var)
    print(f"{w}" + "-" * length + "-"); print() # \n

    print(Banner)

host = input(f"\n{b}[L.O.L] Please Enter The Website You Want To Scan SubDomain {r}(i.e, coconut.or.id): {y}"); host=addHTTP(host)
try:
    if host:
        heading(heading="Finding SubDomains Of", host=host, afterWebHead="", color=c)
        findSubdomains(host)
    else:
        exit()
except KeyboardInterrupt:
    write(var="LOL", color=w, data="Err0r: User Interrupted!")

print(Footer)

#bye 