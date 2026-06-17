text = "banana"

dis = {}

for n in text:
    if n in dis:
        dis[n] += 1
    else:
        dis[n] = 1

# max_count = None 
# max_char = None   

# for key,value in dis.items():
#     if max_count is None or value > max_count:
#         max_count = value
#         max_char = key
print(dis)   
