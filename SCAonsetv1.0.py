import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import copy



def f(k):
    return k
def plot_onset(disease, repeatk, i, age3, root, label5):
    if disease == 'DRPLA':
        whas100 = pd.read_csv('survival_time_drpla20230205public.csv')
        whas1 = pd.read_csv('drplaonsetsurvival20230205public.csv')
    else:
        whas100 = pd.read_csv('survival_time_mjd20230205public.csv')
        whas1 = pd.read_csv('mjdonsetsurvival20230205public.csv')

    dat60 = whas100[whas100['repeat2'] ==repeatk ]
    whas1 = whas1[whas1['CAG_repeat'] ==repeatk]
    dat60['current_age'] = 0 
    i_bool = (whas1['time']==i)
    if disease == 'DRPLA':
        if (repeatk < 60)or(repeatk > 70):
            label5["text"] = 'Unsupported CAG repeat'
            return 0
        if (age3 < (i + 1))or(age3 > 76)or(i<0)or(i>76):
            label5["text"] = 'Unsupported age'
            return 0
    else:
        if (repeatk < 67)or(repeatk > 78):
            label5["text"] = 'Unsupported CAG repeat'
            return 0
        if (age3 < (i + 1))or(age3 > 81)or(i<0)or(i>81):
            label5["text"] = 'Unsupported age'
            return 0
    if whas1.iloc[i_bool.tolist().index(True) , whas1.columns.get_loc('analysis')] == 1 :
        datb = copy.deepcopy(dat60)
        datb['current_age'] = i
        datb['mean_s'] = -1
        dat60 = dat60.reset_index()
        datb = datb.reset_index()
        if disease == 'DRPLA':
            i3 = 760
        else:
            i3 = 810
        for i2 in range(1, i3):
            if (len(dat60[dat60['onset10']==(i*10)])>0)and(len(dat60[dat60['onset10']==(i2*1)+(i*10)])>0):
                i_bool = (datb['onset10']==(i2*1)+(i*10))
                i2_bool = (dat60['onset10']==(i2*1)+(i*10))
                i3_bool = (dat60['onset10']==(i*10))
                datb.iloc[i_bool.tolist().index(True) , datb.columns.get_loc('mean_s')] = dat60.iloc[ i2_bool.tolist().index(True),dat60.columns.get_loc('mean_s')]/dat60.iloc[ i3_bool.tolist().index(True),dat60.columns.get_loc('mean_s')]
        datb = datb[datb['mean_s'] != -1]
        datb = datb.dropna(subset=['mean_s'])
        datb['age'] = datb['onset10']/10
        datb['probability'] = datb['mean_s'] 

        x = datb['age'].to_numpy()
        y = datb['probability'].to_numpy()


        master = tk.Tk()
        master.title(disease + ", CAG repeat: " + str(repeatk) + ", current age: " + str(i))
        fig = plt.figure()
        ax = plt.axes([0.1, 0.1, 0.8, 0.8])
        ax2 = plt.axes([0.35, 0.95, 0.3, 0.2])
        slider_pos = plt.axes([0.1, 0.01, 0.8, 0.03])
        sli_a = Slider(slider_pos, 'age', i+1, i3/10, valinit=age3,valstep=1)
        ax.set_xlim(0, 80)
        ax.set_ylim(0, 1)
        ax.plot(x, y)
        i4_bool = (datb['age'] == age3)
        pa = ax2.text(0.0, 0.0, "Asymptomatic probability at age " + str(age3) + " : " + str(round(datb.iloc[i4_bool.tolist().index(True),datb.columns.get_loc('probability') ],2)), size=12)
        #ax2.text(0.0, 0.0, "Probability at age " + str(age3) + " : " + str(round((mae.iloc[len(mae)-1,mae.columns.get_loc('probability')]+ato.iloc[0,ato.columns.get_loc('probability')])/2,2)), size=12)
        def update(val):
            age3 = val
            i4_bool = (datb['age'] == age3)
            pa.set_text("Asymptomatic probability at age " + str(age3) + " : " + str(round(datb.iloc[i4_bool.tolist().index(True),datb.columns.get_loc('probability') ],2)))
        sli_a.on_changed(update)
        ax2.axis("off") 
        label5["text"] = 'Analysis completed.'
        #label5 = ttk.Label(frame1, text='Analysis completed.', padding=(5, 2))
        #label5.grid(row=5, column=1)
        fig_canvas = FigureCanvasTkAgg(fig, master)
        tmp = fig_canvas.get_tk_widget()
        tmp.pack()
        master.mainloop()
    else: 
        label5["text"] = 'Too little information for the specified condition to be displayed'
        #label5 = ttk.Label(frame1, text='Too little information for the specified condition to be displayed', padding=(5, 2))

        


tab = ['DRPLA', 'SCA3']
root = tk.Tk()
root.geometry("640x480")
root.title('Input')

frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

label1 = ttk.Label(frame1, text='disease', padding=(5, 2))
label1.grid(row=0, column=0)

label2 = ttk.Label(frame1, text='CAG repeat (DRPLA:60-70, SCA3:67-78)', padding=(5, 2))
label2.grid(row=1, column=0)

label3 = ttk.Label(frame1, text='current age', padding=(5, 2))
label3.grid(row=2, column=0)

label4 = ttk.Label(frame1, text='Age at which you want to find the probability', padding=(5, 2))
label4.grid(row=3, column=0)

label5 = ttk.Label(frame1, text='', padding=(5, 2))
label5.grid(row=5, column=1)

dis = tk.StringVar()
dis_cb = ttk.Combobox(
    frame1, 
    textvariable=dis, 
    values=tab, 
    width=20)
dis_cb.set(tab[0])
dis_cb.bind(
    '<<ComboboxSelected>>')
dis_cb.grid(row=0, column=1)

repeatk2 = tk.IntVar()
repeatk = ttk.Entry(
    frame1,
    textvariable=repeatk2,
    width=20)
repeatk.grid(row=1, column=1)

age2 = tk.IntVar()
i = ttk.Entry(
    frame1,
    textvariable=age2,
    width=20)
i.grid(row=2, column=1)

age3 = tk.IntVar()
age_t = ttk.Entry(
    frame1,
    textvariable=age3,
    width=20)
age_t.grid(row=3, column=1)

button1 = ttk.Button(
    frame1, text='OK', 
    command=lambda:plot_onset(dis.get(), repeatk2.get(), age2.get(), age3.get(), root, label5))
button1.grid(row=4, column=1)

root.mainloop()

