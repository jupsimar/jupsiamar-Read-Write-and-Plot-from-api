import statistics as s
result = []

with open("weather.txt","r") as file_obj:
    for line in file_obj:
        stripline = line.strip()
        result.append(stripline)

result = [float(i) for i in result]

print(result)   
print("max",max(result))
print("min",min(result))
print("len",len(result))
print("Mean",s.mean(result))