import os
import time
import tkinter as tk
import subprocess
import tempfile
import shutil
from concurrent.futures import ThreadPoolExecutor
from subprocess import run
from tkinter import messagebox
from time import sleep
from tkinter import Label
from tkinter import StringVar
from tkinter import Button
from tkinter import Canvas
from os.path import exists
from tkinter import Toplevel

class KeepData():
    def __init__(self):
        self._var = None

    def set(self, value):
        self._var = value

    def get(self):
        return self._var

    def delete(self):
        self._var = None


class CountDataUsage():
    def __init__(self):
        self.netstat = "C:\\Windows\\System32\\netstat.exe"
        self.ping_args = "C:\\Windows\\System32\\ping.exe"
        self.DETACHED_PROCESS = 0x00000008
        if exists(self.netstat):
            if exists(self.ping_args):
                self.executor = ThreadPoolExecutor(max_workers=3)
                self.executor2 = ThreadPoolExecutor(max_workers=3)
                self.executor3 = ThreadPoolExecutor(max_workers=1)
                self.executor4 = ThreadPoolExecutor(max_workers=1)
                self.tempfolder = tempfile.mkdtemp()
                self.tempdownload = self.tempfolder + '\\totaldownload.cache'
                self.netstat = ["C:\\Windows\\System32\\netstat.exe", "-e"]
                self.ping_args = ["C:\\Windows\\System32\\ping.exe", "8.8.8.8", "-n", "1"]
                self.main_init = tk.Tk()
                self.focus_background = Toplevel()
                self.focus_background.withdraw()
                self.main_init.focus()
                self.N1_var = StringVar()
                self.N2_var = StringVar()
                self.status = StringVar()
                self.advanced_mode = StringVar()
                self.advanced_mode.set('Enable Advanced Mode')
                self.Ping_var = StringVar()
                self.n1_keep = KeepData()
                self.n2_keep = KeepData()
                self.ping_keep = KeepData()
                self.main_init.resizable(0,0)
                self.background = Toplevel()
                self.background.withdraw()
                self.main_init.title('Counting Data Usage')
                self.main = Canvas(self.main_init, width=300, height=300)
                self.main.pack()
                self.main.configure(background='white')
                word1 = Label(self.main, text='Welcome!', font='Vendeta 18 bold', background='white')
                self.main.create_window(150, 75, window=word1)
                word2 = Label(self.main, text='Click Here to Start !', background='white')
                self.main.create_window(150, 125, window=word2)
                button1 = Button(self.main, text='Start Now!!', command=self.gui_process, background='white')
                self.main.create_window(150, 150, window=button1)
                button2 = Button(self.main, text='', textvariable=self.advanced_mode, background='white', command=self.toggle_advanced_mode)
                self.main.create_window(70, 290, window=button2)
                self.main.mainloop()
                self.status.set('OFF')
            else:
                root = tk.Tk()
                root.withdraw()
                messagebox.showerror('Error', 'Your OS doens\'t have netstat')
                root.quit()
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror('Error', 'Your OS doens\'t have netstat')
            root.quit()
    
    def self_focus(self):
        self.main_init.focus_force()


    def toggle_advanced_mode(self):
        if self.advanced_mode.get() == 'Enable Advanced Mode':
            self.advanced_mode.set('Disable Advanced Mode')
        elif self.advanced_mode.get() == 'Disable Advanced Mode':
            self.advanced_mode.set('Enable Advanced Mode')

    def Net1(self):
        N1 = run(self.netstat, stdout=subprocess.PIPE, shell=False)
        self.N1 = N1.stdout.decode()
        self.N1_var.set('done')
        self.n1_keep.set(self.N1)

    def Net2(self):
        N2 = run(self.netstat, stdout=subprocess.PIPE, shell=False)
        self.N2 = N2.stdout.decode()
        self.N2_var.set('done')
        self.n2_keep.set(self.N2)
    
    def Received1(self):
        self.pointR1 = self.n1_keep.get().find('Bytes')
        self.point2R1 = self.n1_keep.get().find('Unicast packets')
        self.result_point_R1 = self.N1[self.pointR1:self.point2R1].strip()
        self.pointR1_2 = self.result_point_R1.find('s')
        self.pointR1_2+=1
        self.result_R1 = self.result_point_R1[self.pointR1_2:].strip()
        self.remove_space_R1 = self.result_R1.find(' ')
        self.R1 = self.result_R1[:self.remove_space_R1].strip().replace('-', '')

    def Received2(self):
        self.pointR2 = self.n2_keep.get().find('Bytes')
        self.point2R2 = self.n2_keep.get().find('Unicast packets')
        self.result_point_R2 = self.N2[self.pointR2:self.point2R2].strip()
        self.pointR2_2 = self.result_point_R2.find('s')
        self.pointR2_2+=1
        self.result_R2 = self.result_point_R2[self.pointR2_2:].strip()
        self.remove_space_R2 = self.result_R2.find(' ')
        self.R2 = self.result_R2[:self.remove_space_R2].strip().replace('-', '')

    def Sent1(self):
        self.pointS1 = self.n1_keep.get().find('Bytes')
        self.point2S1 = self.n1_keep.get().find('Unicast packets')
        self.result_point_S1 = self.N1[self.pointS1:self.point2S1].strip()
        self.pointS1_2 = self.result_point_S1.find('s')
        self.pointS1_2+=1
        self.result_S1 = self.result_point_S1[self.pointS1_2:].strip()
        self.remove_space_S1 = self.result_S1.find(' ')
        self.S1 = self.result_S1[self.remove_space_S1:].strip().replace('-', '')

    def Sent2(self):
        self.pointS2 = self.n2_keep.get().find('Bytes')
        self.point2S2 = self.n2_keep.get().find('Unicast packets')
        self.result_point_S2 = self.N2[self.pointS2:self.point2S2].strip()
        self.pointS2_2 = self.result_point_S2.find('s')
        self.pointS2_2+=1
        self.result_S2 = self.result_point_S2[self.pointS2_2:].strip()
        self.remove_space_S2 = self.result_S2.find(' ')
        self.S2 = self.result_S2[self.remove_space_S2:].strip().replace('-', '')

    def SpeedDownload(self):
        self.init_SD = int(self.R2.replace('-', '')) / 1024 - int(self.R1.replace('-', '')) / 1024
        self.init_SD = str(self.init_SD)
        self.pointSD = self.init_SD.find('.')
        self.SPEEDDOWNLOAD = self.init_SD[:self.pointSD].replace('-', '')
        if self.totaldownload.get() == '':
            self.totaldownload.set(self.SPEEDDOWNLOAD)
            self.totaldownload_inside.set(self.SPEEDDOWNLOAD)
        else:
            pass

    def SpeedUpload(self):
        self.init_SU = int(self.S2.replace('-', '')) / 1024 - int(self.S1.replace('-', '')) / 1024
        self.init_SU = str(self.init_SU)
        self.pointSU = self.init_SU.find('.')
        self.SPEEDUPLOAD = self.init_SU[:self.pointSU].replace('-', '')
        if self.totalupload.get() == '':
            self.totalupload.set(self.SPEEDUPLOAD)
            self.totalupload_inside.set(self.SPEEDUPLOAD)
        else:
            pass

    def TotalDownload(self):
        if self.totaldownload.get() == self.SPEEDDOWNLOAD:
            self.TD = self.totaldownload.get()
        else:
            point = str(self.totaldownload_inside.get()).find('-')
            if point == -1:
                td1 = float(self.totaldownload_inside.get())
            else:
                var = str(self.totaldownload_inside.get())
                td1 = float(var.replace('-', ''))
            td2 = int(self.SPEEDDOWNLOAD)
            self.result_TD = td1 + td2 / 1024
            self.result_TD_str = str(self.result_TD)
            self.point_TD = self.result_TD_str.find('.')
            self.TD = self.result_TD_str[:self.point_TD]
            self.totaldownload.set(self.TD)
            self.totaldownload_inside.set(self.result_TD)
        

    def TotalUpload(self):
        if self.totalupload.get() == self.SPEEDUPLOAD:
            self.TU = self.totalupload.get()
        else:
            point = str(self.totalupload_inside.get()).find('-')
            if point == -1:
                tu1 = float(self.totalupload_inside.get())
            else:
                var = str(self.totalupload_inside.get())
                tu1 = float(var.replace('-', ''))
            tu2 = int(self.SPEEDUPLOAD)
            self.result_TU = tu1 + tu2 / 1024
            self.result_TU_str = str(self.result_TU)
            self.point_TU = self.result_TU_str.find('.')
            self.TU = self.result_TU_str[:self.point_TU]
            self.totalupload.set(self.TU)
            self.totalupload_inside.set(self.result_TU)

    def ping(self):
        ping_out = run(self.ping_args, stdout=subprocess.PIPE, shell=False)
        self.ping_out = ping_out.stdout.decode()
        self.find_output_ping_point_start = self.ping_out.find('Reply from 8.8.8.8')
        self.find_output_ping_point_end = self.ping_out.find('Ping statistics')
        self.result_output_ping = self.ping_out[self.find_output_ping_point_start:self.find_output_ping_point_end].strip()
        self.result_output_ping_point_start = self.result_output_ping.find('time=')
        self.result_output_ping_point_start+=5
        self.result_output_ping_point_end = self.result_output_ping.find('ms')
        self.result_ping = self.result_output_ping[self.result_output_ping_point_start:self.result_output_ping_point_end].strip()
        self.Ping_var.set('done')

    def gui_process(self):
        self.read_ping2 = StringVar()
        self.read_speed_upload2 = StringVar()
        self.read_speed_download2 = StringVar()
        self.read_received2 = StringVar()
        self.read_sent2 = StringVar()
        self.totaldownload = StringVar()
        self.totalupload = StringVar()
        self.totaldownload_inside = StringVar()
        self.totalupload_inside = StringVar()
        self.main.destroy()
        self.main_init.configure(background='black')
        self.main2 = Canvas(self.main_init, width=300, height=300)
        self.main2.pack()
        self.main2.configure(background='black')
        word1 = Label(self.main2, text='Total Upload', foreground='green', background='black', font='Vendetta 12 bold')
        self.main2.create_window(85, 70, window=word1)
        word2 = Label(self.main2, text='Total Download', foreground='green', background='black', font='Vendeta 12 bold')
        self.main2.create_window(210, 70, window=word2)
        word3 = Label(self.main2, text='Speed Download', foreground='green', background='black', font='Vendeta 12 bold')
        self.main2.create_window(215, 150, window=word3)
        word4 = Label(self.main2, text='Speed Upload', foreground='green', background='black', font='Vendeta 12 bold')
        self.main2.create_window(75, 150, window=word4)
        word5 = Label(self.main2, text='Ping', foreground='green', background='black', font='Vendeta 12 bold')
        self.main2.create_window(150, 215, window=word5)
        word_sent = Label(self.main2, text='', textvariable=self.read_sent2, foreground='blue', background='black',
                        font='Vendeta 12 bold')
        self.main2.create_window(100, 95, window=word_sent)
        word_received = Label(self.main2, text='', textvariable=self.read_received2, foreground='blue', background='black',
                            font='Vendeta 12 bold')
        self.main2.create_window(195, 95, window=word_received)
        word_speed_download = Label(self.main2, text='', textvariable=self.read_speed_download2, foreground='blue',
                                    background='black', font='Vendeta 12 bold')
        self.main2.create_window(195, 175, window=word_speed_download)
        word_speed_upload = Label(self.main2, text='', textvariable=self.read_speed_upload2, foreground='blue', background='black',
                                font='Vendeta 12 bold')
        self.main2.create_window(100, 175, window=word_speed_upload)
        word_ping = Label(self.main2, text='', textvariable=self.read_ping2, foreground='blue', background='black',
                        font='Vendeta 12 bold')
        self.main2.create_window(150, 245, window=word_ping)
        self.main2.after(100, self.loop)
        self.main2.mainloop()
        self.status.set('OFF')

    def core_main(self):
        self.Received2()
        self.Received1()
        self.Sent1()
        self.Sent2()
        self.SpeedDownload()
        self.SpeedUpload()
        self.TotalDownload()
        self.TotalUpload()
        self.read_speed_download2.set(self.SPEEDDOWNLOAD + ' KBps')
        self.read_speed_upload2.set(self.SPEEDUPLOAD + ' KBps')
        self.read_received2.set(self.TD + ' MB')
        self.read_sent2.set(self.TU + ' MB')


    def pool_executor(self):
        while True:
            self.Net1()
            self.Net2()
            self.core_main()
            sleep(0.1)
            if self.status.get() == 'OFF':
                break

    def carry_b(self):
        self.executor4.submit(self.pool_executor)
    
    def loop_ping(self):
        while True:
            self.ping()
            if self.result_ping == '':
                self.read_ping2.set('Timed Out')
            else:
                self.read_ping2.set(self.result_ping + ' ms')
            sleep(0.1)
            if self.status.get() == 'OFF':
                break

    def carry_a(self):
        self.executor.submit(self.loop_ping)

    def loop(self):
        self.executor2.submit(self.carry_b)
        self.executor3.submit(self.carry_a)

if __name__ == "__main__":
        executor = ThreadPoolExecutor(max_workers=2)
        CDU = CountDataUsage()