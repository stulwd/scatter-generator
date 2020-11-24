import xlrd

x1 = xlrd.open_workbook("data.xlsx")
sheets = x1.sheets()

# kelvin_table sheet
kelvin_table = sheets[0]
# temperature-image table
imgTmp_table = sheets[1]

# graph dataSet
graphData = []

def tmp2rgb(tmpVal):
    i = 0
    rgb = []
    while True:
        if tmpVal == kelvin_table.row_values(i)[0]:
            rgb = kelvin_table.row_values(i, 1, 4)
            break
        i += 1
    return rgb

print(tmp2rgb(1100))

for i in range( imgTmp_table.nrows ):
    # ignore row 1
    if i == 0:
        continue
    dot = imgTmp_table.row_values(i)
    # tempture before aug
    dot.append(tmp2rgb(imgTmp_table.row_values(i)[1]))
    # tempture after aug
    dot.append(tmp2rgb(imgTmp_table.row_values(i)[2]))
    # put every dot into graphData set
    graphData.append(dot)

# print graph info
print(graphData)

# draw graph
import matplotlib.pyplot as plt

# draw dot one by one
x = 0
for dot in graphData:
    color = hex( (int(dot[3][0])<<16) + (int(dot[3][1])<<8) + (int(dot[3][2])))
    plt.scatter(x, dot[1], marker="o", color="#"+color[2:], s = 40, label = "preAug")
    color = hex( (int(dot[4][0])<<16) + (int(dot[4][1])<<8) + (int(dot[4][2])))
    print(color)
    plt.scatter(x, dot[2], marker="x", color="#"+color[2:], s = 40, label = "afterAug")
    x += 1

plt.show()
