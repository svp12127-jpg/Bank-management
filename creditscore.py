def creditscores(sal,late):
    crdlate=200-(5*late)
    if sal>=1000000:
        x=600
    elif sal>=750000:
        x=550
    elif sal>=500000:
        x=500
    elif sal>=250000:
        x=450
    elif sal>=200000:
        x=400
    elif sal>=150000:
        x=350
    elif sal>=100000:
        x=300
    elif sal>=50000:
        x=250
    else:
        x=100
    y=200-(5*late)
    cred=x+y
    return cred
