def draw_hospital(a):
    b=["_"]
    c=["|"]
    d=["/"]
    e=[chr(92)]
    for i in range(20,70):
        a[i][30]=c
        a[i][70]=c
    for j in range(30,70):
        a[20][j]=b
        a[70][j]=b
    for m in range(40,50):
        a[m][40]=b
        a[m][50]=b
        a[40][m]=c
        a[50][m]=c
        a[45][m]=b
        a[m][45]=c
    return
