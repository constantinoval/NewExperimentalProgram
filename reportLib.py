# -- coding: cp1251
from __future__ import print_function
import json
import numpy as np
import matplotlib
import os
import base64
import pyodbc
import sys

# matplotlib.use('PS')
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib import rcParams
from math import log10
rcParams['font.size'] = 10
rcParams['font.family'] = 'verdana'
rcParams['figure.dpi'] = 100
rcParams['savefig.dpi'] = 100
rcParams['figure.figsize'] = (8, 4)
sys.path.append('wkhtmltopdf/bin/')


def formTableLines(data, nPoints=0):
    nCols = len(data)
    nRows = len(data[0])
    if nPoints:
        for i, d in enumerate(data):
            nd = np.interp(np.linspace(0, nRows, nPoints), range(nRows), d)
            data[i] = nd
        nRows = nPoints
    rez = """<TABLE BORDER=2 CELLSPACING=0 WIDTH=700><caption> <center><b>Таблица экспериментальных данных</caption>
<tr><b><td>Время, мкс</td><td>Падающий</td><td>Отраженный</td><td>Прошедший</td>"""
    if nCols > 4:
        rez += "<td>Деформация</td><td>Напряжение, МПа</td><td>Скорость деформации, 1/c</td></b></tr>"
    rez += '\n'
    cell_f = '<td align=center><font size=2>{:.3f}</font></td>'
    cell_e = '<td align=center><font size=2>{:.3e}</font></td>'
    for j in range(nRows):
        rez += '<tr>'
        for i in range(nCols):
            num = data[i][j]
            if num == 0:
                cell = cell_f
            else:
                cell = cell_f if log10(abs(num)) > -1 else cell_e
            rez += cell.format(num)
        rez += '</tr>'
    return rez+"\n</table>\n"


def plotPulses(dt, ei, er, et, fout='sync.png', sig=1.0, eps=None):
    t = np.array([dt*i for i in range(len(ei))])
    summ = ei-er-et
    plt.figure()
    N = len(ei)
    mev = N//20
    if mev == 0:
        mev = 1
    plt.plot(t, ei, 'k', marker='s', markevery=mev,
             markersize=5, label=u'падающий')
    plt.plot(t, er, 'k', marker='v', markevery=mev,
             markersize=5, label=u'отраженный')
    plt.plot(t, et, ':k', lw=2, label=u'прошедший')
    plt.plot(t, summ, '--k', label=u'сумма')
    if eps:
        plt.axhline(eps, color='k', lw=1,
                    label=u'калибровка\nпо скорости\nударника')
    plt.axhline(0, color='k')
    plt.xlabel(u'время, мкс')
    plt.ylabel(u'деформация')
    plt.subplots_adjust(left=0.12, bottom=0.15, right=0.75)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.grid()
    plt.title(
        u'Импульсы деформации в мерных стержнях')
    plt.savefig(fout)


def plotDiagr(e, s, de, fout='diag.png'):
    f = plt.figure()
#    ax1=SubplotZero(f,111)
    ax1 = plt.subplot(111)
#    f.add_subplot(ax1)
#    ax1.axis['xzero'].set_visible(True)
#    for direction in ["bottom", "top"]:
#        ax1.axis[direction].set_visible(False)
    ls1 = ax1.plot(e, s, 'k', label=u'напряжение')
#    plt.axhline(0, color='k')
    plt.xlabel(u'деформация')
    plt.ylabel(u'напряжение, МПа')
    plt.ylim(0, plt.ylim()[1])
    plt.grid()
    ax2 = plt.twinx()
    ls2 = plt.plot(
        e, de, 'k--', label=u'скорость\nдеформации')
    plt.ylim(((min(de)*1.5)//100+1)*100, (max(de)*2//100+1)*100)
    plt.xlabel(u'деформация')
    plt.ylabel(u'скорость деформации, 1/c')
    plt.subplots_adjust(left=0.12, bottom=0.15, right=0.7)
    ls = ls1+ls2
    labs = [l.get_label() for l in ls]
    plt.legend(ls, labs, bbox_to_anchor=(1.15, 1),
               loc=2, borderaxespad=0.)  # fontsize=12)
#    ax1.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 10))
    ax2.set_yticks(np.linspace(ax2.get_ybound()[
                   0], ax2.get_ybound()[1], len(ax1.get_yticks())))
    plt.title(u'Диаграмма деформирования образца')
    plt.savefig(fout)


tensParams = """<tr><td>Средняя скорость деформации, 1/c</td><td><b>{0:.3f}</b></td>
<td>Дефориация разрушения, %</td><td><b>{1:.3f}</b></td>
</tr>
<tr><td>Относительное удлинение после разрыва, %</td><td><b>{2:.3f}</b></td>
<td>Относительное сужение после разрыва, %</td><td><b>{3:.3f}</b></td>
</tr>
"""
compressParams = """<tr><td>Средняя скорость деформации, 1/c</td><td><b>{0:.0f}</b></td>
<td>Пластическая деформация, %</td><td><b>{1:.2f}</b></td>
</tr>
"""


def createReport(data, outdir):
    if len(data['pulses'][0]):
        pulses = data['pulses']
        dt = pulses[0][1]-pulses[0][0]
        plotPulses(dt*1e6, pulses[1][0], pulses[1][1], pulses[1][2],
                   'img1.png', sig=1, eps=data['strikerV']/2.0/data['bar1C'])
        plotDiagr(data['diag'][1], data['diag'][2],
                  data['diag'][3], fout='img2.png')
        data_uri = base64.b64encode(open('img1.png', 'rb').read()).decode(
            'utf-8').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,%s">' % data_uri
        data['syncImg'] = img_tag

        data_uri = base64.b64encode(open('img2.png', 'rb').read()).decode(
            'utf-8').replace('\n', '')
        img_tag = '<img src="data:image/png;base64,%s">' % data_uri
        if data['expCode'][0] in ['c', 't']:
            data['diagrImg'] = img_tag
        else:
            data['diagrImg'] = ''
        if data['expCode'][0] in ['c', 't']:
            data['tableLines'] = formTableLines([pulses[0]*1e6, pulses[1][0],
                                                 pulses[1][1], pulses[1][2], data['diag'][0], data['diag'][1], data['diag'][2]], nPoints=85)
        else:
            data['tableLines'] = formTableLines([pulses[0]*1e6, pulses[1][0],
                                                 pulses[1][1], pulses[1][2]], nPoints=85)
    if data['expCode'][0] == 'c':
        data['expAdditionalCells'] = compressParams.format(
            data['expDE'], data['ep'])
    elif data['expCode'][0] == 't':
        data['expAdditionalCells'] = tensParams.format(
            data['expDE'], data['ep'], data['delta'], data['ksi'])
    shablon = open('protokol.smp').read()
    open(data['expCode']+'.html', 'w').write(shablon.format(**data))
#    dr=os.path.abspath('wkhtmltopdf/bin')+os.sep
    command = "wkhtmltopdf --margin-left 30mm --margin-right 5mm --header-left {}_{} --header-right [page]/[toPage] --header-line ".format(
        u'Протокол_динамического_испытания', data['expCode'])
    command += "--encoding cp1251 " + \
        data['expCode']+'.html '+outdir+os.sep+data['expCode']+'.pdf'
    os.system(command)
    try:
        os.remove(data['expCode']+'.html')
        os.remove('img1.png')
        os.remove('img2.png')
    except:
        pass
