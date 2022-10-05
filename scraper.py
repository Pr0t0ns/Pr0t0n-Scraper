import requests
import threading
import ctypes, time


class Scrape:
    def __init__(self) -> None:
        self.scraped = 0
        self.finished = False
        self.start_time = time.time()
        self.urls = ['http://alexa.lr2b.com/proxylist.txt', 'https://proxyspace.pro/https.txt', 'https://proxyspace.pro/http.txt', 'http://rootjazz.com/proxies/proxies.txt', 'https://raw.githubusercontent.com/almroot/proxylist/master/list.txt', 'https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt', 'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/http.txt', 'https://raw.githubusercontent.com/hanwayTech/free-proxy-list/main/https.txt', 'https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt', 'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt', 'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt', 'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', 'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt', 'https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt', 'https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt', 'https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/http.txt', 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXY_LIST/master/https.txt', 'https://rootjazz.com/proxies/proxies.txt', 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt']
        self.scraped_proxies = []
    def show_stats(self):
        while self.finished == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Pr0t0n Proxy Scraper | Scraped: {self.scraped} | Time: {time.time() - self.start_time}")
            time.sleep(0.1)
        exit(0)
    def scrape(self):
        for site in self.urls:
            print(f"[\]: Scraping Proxies from ({site})")
            response = requests.get(site).text
            site_scraped = 0
            for proxy in response.split('\n'):
                if proxy in self.scraped_proxies:
                    pass
                else:
                    self.scraped_proxies.append(proxy)
                    self.scraped += 1
                    site_scraped += 1
            print(f"[=]: Scraped ({site_scraped}) Proxies from ({site})")
        with open("scraped/proxies.txt", 'a+') as file:
            file.truncate(0)
            for proxy in self.scraped_proxies:
                proxy = proxy.replace("\n", "")
                if len(proxy) <= 4:
                    pass
                else:
                    file.write(f"{proxy}\n")
        self.finished = True
        input(f"[+]: Finished Scraping Proxies | Successfully Wrote ({self.scraped}) New Proxies to scraped/proxies.txt. Press Enter to continue")
        exit(0)

if __name__ == "__main__":
    Scrape = Scrape()
    threading.Thread(target=Scrape.scrape).start()
    threading.Thread(target=Scrape.show_stats).start()

