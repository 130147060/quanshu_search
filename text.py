start_url=[]
base_url='http://www.quanshuwang.com/list/'
tail_url='_1.html'
for i in range(12):
    url=base_url+f'{i+1}'+tail_url
    start_url.append(url)
print(start_url)