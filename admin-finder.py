import asyncio
import aiohttp
from aiohttp import ClientSession
import time
import socket
#Admin panel finder script coded by Amanullah-code77
print(""" 
        \33[93;1madmin-finder\33[97;1m
         \33[96;1madmin-finder coded by:
          \33[91;1mAmanullah-code77 
""")

target = input("\33[93;1mEnter Target Url here: \33[1;0m")
print("")
#Basic filter of input
target = target.replace('https://', '')
target = target.replace('http://', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target

#define variables, functions, etc.
start = time.time()

yay = []

conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    ) #used because of issues some might have with the AsyncResolver

async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status #gets status codes to see if page is up
        if status == 200:
            print("\33[97;1mpew (>O_O)>  \33[1;0m{}\33[97;1m  <(O_O<) pew {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1mx_x \33[94;1m{}\33[91;1m x_x {}".format(response.url, status))
        elif status == 403:
            print("\33[91;1mx_x \33[94;1m{}\33[91;1m x_x \33[95;1m{}".format(response.url, status))
        else:
            print("\33[95;1m??? {} ??? {}".format(response.url, status))
        return await response.read()

async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('admin.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)

    async with ClientSession(connector=conn) as session: #creates the tasks
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
        
#start loop        
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)

#Results
end = time.time()
script_time = end - start
print("\33[93;1mScan took {} seconds to complete\n".format(script_time))
print("\33[91;1m### \33[93;1mResults \33[91;1m###\33[1;0m")
if len(yay) == 0:
    print("\33[94;1m!!! NO RESULTS !!!")
else:
    for y in yay:
        print(y)    
print("\33[91;1m###############")
   
