# -- coding: cp1251
from odbcAccess import odbc
import sys
import os
kwds=sys.argv
if len(kwds)<3: exit
indb=odbc(os.path.abspath(kwds[1]))
outdb=odbc(os.path.abspath(kwds[2]))
ec1=indb.getInfo('�����������', getFields='����������')
ec1=set([k['����������'] for k in ec1])
ec2=outdb.getInfo('�����������', getFields='����������')
ec2=set([k['����������'] for k in ec2])
newec=ec1-ec2

for ec in newec:
    d=indb.getInfo('�����������', '����������', ec)
    if len(d):
        d=d[0]
    else:
        continue
    print(ec)
    d.pop('����������')
    d.pop('���')
    outdb.insertInfo('�����������', list(d.keys()), list(d.values()))