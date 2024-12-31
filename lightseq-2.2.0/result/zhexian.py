import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import numpy as np
import scienceplots
import pandas as pd

mpl.rcParams['font.family'] = 'SimHei'
font = {"family":"SimHei"}
mpl.rcParams['axes.unicode_minus'] = False


def Plot1(y1,y2,size,figr):
    x0=range(41)
    y1.insert(0,0)
    y2.insert(0, 0)
    ymax=max(max(y2),max(y1))+1
    tick=list(range(0,round(ymax),2))
    with plt.style.context(['ieee']):
        plt.plot(x0, y1, c='green',label='Lightseq2')
        plt.plot(x0, y2, c='orange',label='Fairseq')
        plt.xlim((0, 40))
        plt.ylim((0, ymax))
        plt.ylabel('显存 (GB)',font,fontsize=12)
        plt.xlabel('时间 (min)',font,fontsize=12)
        plt.yticks(tick)

        plt.tight_layout()

        plt.legend(loc='lower right', frameon=True)

        plt.savefig(f'{size}_{figr}.svg', bbox_inches='tight',dpi=500)
        plt.show()

def Plot2(y3,y4,size,figr):
    x0=range(41)
    y3.insert(0,0)
    y4.insert(0, 0)
    tick=list(range(0,105,20))
    with plt.style.context(['ieee']):
        plt.plot(x0, y3, c='green',label='Lightseq2')
        plt.plot(x0, y4, c='orange',label='Fairseq')
        plt.xlim((0, 40))
        plt.ylim((0, 105))
        plt.ylabel('显存占用率 (%)',font,fontsize=12)
        plt.xlabel('时间 (min)',font,fontsize=12)
        plt.yticks(tick)

        plt.tight_layout()

        plt.legend(loc='lower right', frameon=True)

        plt.savefig(f'{size}_{figr}_1.svg', bbox_inches='tight',dpi=500)
        plt.show()

for size in['4096','8192']:
    for figr in['a','b']:
        lightseq_csv=size+'_lightseq_'+figr+'.csv'
        fairseq_csv=size+'_fairseq_'+figr+'.csv'


        Dlight=pd.read_csv(lightseq_csv,usecols=[4,5],nrows=40)
        Dlight.columns=range(len(Dlight.columns))
        Dlight[0]=Dlight[0].str.extract('(\d+)')
        Dlight[1] = Dlight[1].str.extract('(\d+)')

        Dfair = pd.read_csv(fairseq_csv, usecols=[4, 5], nrows=40)
        Dfair.columns = range(len(Dfair.columns))
        Dfair[0] = Dfair[0].str.extract('(\d+)')
        Dfair[1] = Dfair[1].str.extract('(\d+)')

        #显存占用量折线图
        y1=[round(float(x)/1024,2) for x in Dlight[0].tolist()]
        y2=[round(float(x)/1024,2) for x in Dfair[0].tolist()]
        Plot1(y1,y2,size,figr)

        #显存占用率折线图
        y3=[int(x) for x in Dlight[1].tolist()]
        y4=[int(x) for x in Dfair[1].tolist()]
        Plot2(y3,y4,size,figr)
        # print(y3, y4)


