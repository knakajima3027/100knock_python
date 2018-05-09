def tmpl(x, y, z):
    result = str(x) + '時の' + str(y) + 'は' + str(z)
    return result

target = tmpl(12, '気温', 22.4)

print(target)
