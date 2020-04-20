# -- coding: cp1251
from odbcAccess import odbc
import sys
import os
kwds=sys.argv
if len(kwds)<3: exit
indb=odbc(os.path.abspath(kwds[1]))
outdb=odbc(os.path.abspath(kwds[2]))
ec1=indb.getInfo('Эксперимент', getFields='КодОбразца')
ec1=set([k['КодОбразца'] for k in ec1])
ec2=outdb.getInfo('Эксперимент', getFields='КодОбразца')
ec2=set([k['КодОбразца'] for k in ec2])
newec=ec1-ec2

for ec in newec:
    d=indb.getInfo('Эксперимент', 'КодОбразца', ec)
    if len(d):
        d=d[0]
    else:
        continue
    print(ec)
    d.pop('КодОбразца')
    d.pop('Код')
    outdb.insertInfo('Эксперимент', list(d.keys()), list(d.values()))