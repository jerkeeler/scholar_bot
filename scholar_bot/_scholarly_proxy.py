from fp.fp import FreeProxy
from scholarly import scholarly


def get_new_proxy():
    proxy_works = False
    while not proxy_works:
        proxy = FreeProxy(country_id=["US"], rand=True, timeout=1).get()
        proxy_works = scholarly.use_proxy(http=proxy, https=proxy)
    print("Found new proxy!")
    return proxy
