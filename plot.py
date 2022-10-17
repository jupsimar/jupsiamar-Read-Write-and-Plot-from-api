import matplotlib.pyplot as plt 

result = []
with open("weather.txt","r") as file_obj:
    for line in file_obj:
        stripline = line.strip()
        result.append(stripline)
  
fig, ax = plt.subplots()
plt.xlabel("Time")
plt.ylabel("Temp")

ax.plot(result)

plt.savefig("weather.png")