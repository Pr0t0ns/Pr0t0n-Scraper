import requests, threading, random, ctypes, time, json


class Check:
    def __init__(self) -> None:
        self.valid = 0
        self.invalid = 0
        self.total = 0
        self.working = []
        self.to_check = []
        self.lock = threading.Lock()
        data = open('scraped/proxies.txt', 'r+').read()
        for proxy in data.split('\n'):
            self.to_check.append(proxy)
            self.total += 1
        with open('config.json') as f:
            data = f.read()
            data = json.loads(data)
            self.delay = data['max_delay_sec']
            self.url = data['url']
            self.expected_status = data['expected_status']
            del data
    def stats(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Pr0t0n Proxy Checker | Proxies Loaded: {self.total} | Invalid Proxies: {self.invalid} | Working Proxies: {self.valid} | Proxies Checked: {self.valid + self.invalid}")
            time.sleep(0.3)
    def check(self):
        url = self.url
        try:
            proxy = random.choice(self.to_check)
            self.to_check.remove(proxy)
        except Exception:
            self.lock.acquire()
            while True:
                if self.total == int(self.invalid + self.valid):
                    try:
                        f = open("scraped/proxies.txt", 'a+')
                        f.truncate(0)
                        for value in self.working:
                            f.write(f'{value}\n')
                        f.close()
                        input("Checked all proxies press enter to continue!")
                        exit(0)
                    except Exception:
                        exit(0)
                else:
                    pass
                time.sleep(0.2)
        try:
            data = requests.get(url, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'}, timeout=self.delay)
        except Exception:
            print("[-]: Proxy Invalid")
            self.invalid += 1
            return self.check()
        if data.status_code != self.expected_status:
            print("[-]: Proxy Invalid")
            self.invalid += 1
            return self.check()
        else:
            print("[+]: Valid Proxy!")  
            self.valid += 1
            self.working.append(proxy)
            return self.check() 
if __name__ == "__main__":
    Check = Check()
    for i in range(int(input("Enter Threads: "))):
        threading.Thread(target=Check.check).start()
    Check.stats()
    
