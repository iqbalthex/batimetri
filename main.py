import matplotlib.pyplot as plt

filename = 'data.txt'
f = open(filename)

# kode warna rgb
'''(
  (  0,  0,  150), (  8,   8, 215), ( 58,  58, 248), ( 74, 103, 248),
  (103, 127, 249), (137, 137, 255), (159, 159, 255), (193, 193, 255),
  (  0, 164,  74), (  0, 214,  97), (  3, 255, 133), (252, 246,   0),
  (250, 215,   2), (249, 161,   3), (251, 108,   1), (252,  42,   0)
)'''

# kode warna hex
c = [
  '#00044A','#000096','#0808D7','#3A3AF8',
  '#4A67F8','#677FF9','#8989FF','#9F9FFF',
  '#C1C1FF','#00D661','#03FF85','#FCF600',
  '#FAD702','#F9A103','#FB6C01','#FC2A00'
]

x = y = {}
for i in range(len(c)):
  x['x%d'%i] = []
  y['y%d'%i] = []

def apnd(i):
  x['x%d'%i].append(data[1])
  y['y%d'%i].append(data[0])

for line in f:
  data = [float(d) for d in line.split()]
  if   data[2] > 11.6: apnd(15)
  elif data[2] > 10.8: apnd(14) 
  elif data[2] >  9.6: apnd(13)
  elif data[2] >  8.8: apnd(12)
  elif data[2] >  8.0: apnd(11)
  elif data[2] >  7.2: apnd(10)
  elif data[2] >  6.4: apnd(9)
  elif data[2] >  5.6: apnd(9)
  elif data[2] >  4.8: apnd(7)
  elif data[2] >  4.0: apnd(6)
  elif data[2] >  3.2: apnd(5)
  elif data[2] >  2.4: apnd(4)
  elif data[2] >  1.6: apnd(3)
  elif data[2] >  0.8: apnd(2) 
  elif data[2] >  0.0: apnd(1)
  else: apnd(0)

for i in range(len(c)):
  plt.scatter(
    x['x%d'%i],
    y['y%d'%i],
    color=c[i],
    s=15
  )

plt.grid()
plt.show()
