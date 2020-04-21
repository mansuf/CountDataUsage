import os
import time
import tkinter
from os import system
from tkinter import *
from tkinter import messagebox
from time import sleep


def prepare_init():
    if os.path.exists("data"):
        pass
    else:
        os.mkdir('data')


# Satuan Byte
# Kilobyte = 1,024 bytes
# Megabyte = 1,048,576 bytes
# Gigabyte = 1,073,741,824 bytes
# Terabyte = 1,099,511,627,776 bytes
# Petabyte = 1,125,899,906,842,624 bytes


def write_script():
    write = open("data/count.bat", "w")
    write.write("""@echo off 
goto loop

:loop
for /f "tokens=2" %%b in ('netstat -e ^| findstr Bytes') do set RECEIVED=%%b
for /f "tokens=3" %%b in ('netstat -e ^| findstr Bytes') do set SENT=%%b
echo %RECEIVED% > data\\RECEIVED.cache
echo %SENT% > data\\SENT.cache
goto loop2

:loop2
for /f "tokens=2" %%b in ('netstat -e ^| findstr Bytes') do set RECEIVED2=%%b
for /f "tokens=3" %%b in ('netstat -e ^| findstr Bytes') do set SENT2=%%b
echo %RECEIVED2% > data\\RECEIVED2.cache
echo %SENT2% > data\\SENT2.cache
goto loop3

:loop3
for /f "tokens=2" %%b in ('netstat -e ^| findstr Bytes') do set RECEIVED3=%%b
for /f "tokens=3" %%b in ('netstat -e ^| findstr Bytes') do set SENT3=%%b
echo %RECEIVED3% > data\\RECEIVED3.cache
echo %SENT3% > data\\SENT3.cache
goto loop4

:loop4
for /f "tokens=2" %%b in ('netstat -e ^| findstr Bytes') do set RECEIVED4=%%b
for /f "tokens=3" %%b in ('netstat -e ^| findstr Bytes') do set SENT4=%%b
echo %RECEIVED4% > data\\RECEIVED4.cache
echo %SENT4% > data\\SENT4.cache
ping localhost -n 2
goto loop
""")
    write.close()
    write2 = open("data/sb.vbs", "w")
    write2.write("""CreateObject("Wscript.Shell").Run \"\"\"\" & WScript.Arguments(0) & \"\"\"\", 0, False""")
    write2.close()
    write3 = open("data/total_download.cache", "w")
    write3.write('')
    write3.close()
    write4 = open("data/total_upload.cache", "w")
    write4.write('')
    write4.close()
    write5 = open("data/ping.bat", "w")
    write5.write("""@echo off
goto loop

:loop
set VAR=NOT_FOUND
set VAR_MODIFIED=NOT_FOUND
set VAR_MODIFED_VERIFY=NOT_FOUND
set VAR_MODIFED_VERIFY_2=NOT_FOUND
for /f "tokens=*" %%b in ('ping 8.8.8.8 -n 1 ^| findstr /C:Reply /C:General /C:Destination /C:Request') do set VAR=%%b
for /f "tokens=5" %%b in ("%VAR%") do set VAR_MODIFIED=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFIED% ^| findstr [0-9]') do set VAR_MODIFED_VERIFY=%%b
for /f "delims=time tokens=1" %%b in ('echo %VAR_MODIFED_VERIFY%') do set VAR_MODIFED_VERIFY_2=%%b
if %VAR_MODIFED_VERIFY_2%==NOT_FOUND (
    echo Timed out > data\\ping.cache
    ping localhost -n 2
    goto loop
) else (
    echo %VAR_MODIFED_VERIFY_2% > data\\ping.cache
    ping localhost -n 2
    goto loop
)
    """)
    write5.close()
    write7 = open("data/ping.cache", "w")
    write7.write('')
    write7.close()
    write8 = open("data/RECEIVED.cache", "w")
    write8.write('')
    write8.close()
    write9 = open("data/RECEIVED2.cache", "w")
    write9.write('')
    write9.close()
    write10 = open("data/RECEIVED3.cache", "w")
    write10.write('')
    write10.close()
    write11 = open("data/RECEIVED4.cache", "w")
    write11.write('')
    write11.close()
    write12 = open("data/SENT.cache", "w")
    write12.write('')
    write12.close()
    write13 = open("data/SENT2.cache", "w")
    write13.write('')
    write13.close()
    write14 = open("data/SENT3.cache", "w")
    write14.write('')
    write14.close()
    write15 = open("data/SENT4.cache", "w")
    write15.write('')
    write15.close()


def gui_process():
    global main2
    global read_received2
    global read_sent2
    global read_speed_download2
    global read_speed_upload2
    global read_ping2
    read_ping2 = StringVar()
    read_speed_upload2 = StringVar()
    read_speed_download2 = StringVar()
    read_received2 = StringVar()
    read_sent2 = StringVar()
    main.destroy()
    main_init.configure(background='black')
    system('cscript \"data\\sb.vbs\" \"data\\count.bat\" && cscript \"data\\sb.vbs\" \"data\\ping.bat\"')
    main2 = Canvas(main_init, width=300, height=300)
    main2.pack()
    main2.configure(background='black')
    word1 = Label(main2, text='Total Upload', foreground='green', background='black', font='Vendetta 12 bold')
    main2.create_window(85, 70, window=word1)
    word2 = Label(main2, text='Total Download', foreground='green', background='black', font='Vendeta 12 bold')
    main2.create_window(210, 70, window=word2)
    word3 = Label(main2, text='Speed Download', foreground='green', background='black', font='Vendeta 12 bold')
    main2.create_window(215, 150, window=word3)
    word4 = Label(main2, text='Speed Upload', foreground='green', background='black', font='Vendeta 12 bold')
    main2.create_window(75, 150, window=word4)
    word5 = Label(main2, text='Ping', foreground='green', background='black', font='Vendeta 12 bold')
    main2.create_window(150, 215, window=word5)
    word_sent = Label(main2, text='', textvariable=read_sent2, foreground='blue', background='black',
                      font='Vendeta 12 bold')
    main2.create_window(100, 95, window=word_sent)
    word_received = Label(main2, text='', textvariable=read_received2, foreground='blue', background='black',
                          font='Vendeta 12 bold')
    main2.create_window(195, 95, window=word_received)
    word_speed_download = Label(main2, text='', textvariable=read_speed_download2, foreground='blue',
                                background='black', font='Vendeta 12 bold')
    main2.create_window(195, 175, window=word_speed_download)
    word_speed_upload = Label(main2, text='', textvariable=read_speed_upload2, foreground='blue', background='black',
                              font='Vendeta 12 bold')
    main2.create_window(100, 175, window=word_speed_upload)
    word_ping = Label(main2, text='', textvariable=read_ping2, foreground='blue', background='black',
                      font='Vendeta 12 bold')
    main2.create_window(150, 245, window=word_ping)
    main2.after(500, process)
    main2.mainloop()
    system('rmdir /Q /S data')


def process():
    global total_download2, total_upload2
    R1 = ''
    R2 = ''
    R3 = ''
    R4 = ''
    S1 = ''
    S2 = ''
    S3 = ''
    S4 = ''
    S4minS3 = ''
    S2minS1 = ''
    R4minR3 = ''
    R2minR1 = ''
    SPEEDDOWNLOAD = ''
    SPEEDUPLOAD = ''
    if not os.path.exists("data"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/count.bat"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/ping.bat"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/sb.vbs"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/ping.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/RECEIVED.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/RECEIVED2.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/RECEIVED3.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/RECEIVED4.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/SENT.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/SENT2.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/SENT3.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/SENT4.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/total_download.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    if not os.path.exists("data/total_upload.cache"):
        messagebox.showerror("Error", "Something Happened, App will Restart")
        main_init.destroy()
        main_self()
    read1 = open("data/ping.cache", "r")
    read_ping = read1.read()
    read1.close()
    read2 = open("data/total_download.cache", "r")
    total_download = read2.read()
    read2.close()
    read3 = open("data/total_upload.cache", "r")
    total_upload = read3.read()
    read3.close()
    read8 = open("data/RECEIVED.cache", "r")
    R1 = read8.read()
    read8.close()
    read9 = open("data/RECEIVED2.cache", "r")
    R2 = read9.read()
    read9.close()
    read10 = open("data/RECEIVED3.cache", "r")
    R3 = read10.read()
    read10.close()
    read11 = open("data/RECEIVED4.cache", "r")
    R4 = read11.read()
    read11.close()
    read12 = open("data/SENT.cache", "r")
    S1 = read12.read()
    read12.close()
    read13 = open("data/SENT2.cache", "r")
    S2 = read13.read()
    read13.close()
    read14 = open("data/SENT3.cache", "r")
    S3 = read14.read()
    read14.close()
    read15 = open("data/SENT4.cache", "r")
    S4 = read15.read()
    read15.close()
    if R1 == '':
        pass
    else:
        R1 = int(R1) / 8 / 1024
        R1 = str(R1)
        R1_point = R1.find('.')
        if R1_point == -1:
            pass
        else:
            R1 = R1[:R1_point]
            R1 = int(R1)
    if R2 == '':
        pass
    else:
        R2 = int(R2) / 8 / 1024
        R2 = str(R2)
        R2_point = R2.find('.')
        if R2_point == -1:
            pass
        else:
            R2 = R2[:R2_point]
            R2 = int(R2)
            try:
                R2minR1 = R2 - R1
            except:
                pass
    if R3 == '':
        pass
    else:
        R3 = int(R3) / 8 / 1024
        R3 = str(R3)
        R3_point = R3.find('.')
        if R3_point == -1:
            pass
        else:
            R3 = R3[:R3_point]
            R3 = int(R3)
    if R4 == '':
        pass
    else:
        R4 = int(R4) / 8 / 1024
        R4 = str(R4)
        R4_point = R4.find('.')
        if R4_point == -1:
            pass
        else:
            R4 = R4[:R4_point]
            R4 = int(R4)
            try:
                R4minR3 = R4 - R3
            except:
                pass
    if S1 == '':
        pass
    else:
        S1 = int(S1) / 8 / 1024
        S1 = str(S1)
        S1_point = S1.find('.')
        if S1_point == -1:
            pass
        else:
            S1 = S1[:S1_point]
            S1 = int(S1)
    if S2 == '':
        pass
    else:
        S2 = int(S2) / 8 / 1024
        S2 = str(S2)
        S2_point = S2.find('.')
        if S2_point == -1:
            pass
        else:
            S2 = S2[:S2_point]
            S2 = int(S2)
            try:
                S2minS1 = S2 - S1
            except:
                pass
    if S3 == '':
        pass
    else:
        S3 = int(S3) / 8 / 1024
        S3 = str(S3)
        S3_point = S3.find('.')
        if S3_point == -1:
            pass
        else:
            S3 = S3[:S3_point]
            S3 = int(S3)
    if S4 == '':
        pass
    else:
        S4 = int(S4) / 8 / 1024
        S4 = str(S4)
        S4_point = S4.find('.')
        if S4_point == -1:
            pass
        else:
            S4 = S4[:S4_point]
            S4 = int(S4)
            try:
                S4minS3 = S4 - S3
            except:
                pass
    try:
        SPEEDDOWNLOAD = R4minR3 - R2minR1
    except:
        pass
    try:
        SPEEDUPLOAD = S4minS3 - S2minS1
    except:
        pass
    if SPEEDDOWNLOAD == '':
        pass
    else:
        SPEEDDOWNLOAD = str(SPEEDDOWNLOAD)
        SPEEDDOWNLOAD = SPEEDDOWNLOAD.replace('-', '')
        write_total_download = open("data/total_download.cache", "w")
        write_total_download.write(SPEEDDOWNLOAD)
        write_total_download.close()
        total_download2 = SPEEDDOWNLOAD
        SPEEDDOWNLOAD = SPEEDDOWNLOAD + ' KBps'
    if SPEEDUPLOAD == '':
        pass
    else:
        SPEEDUPLOAD = str(SPEEDUPLOAD)
        SPEEDUPLOAD = SPEEDUPLOAD.replace('-', '')
        write_total_upload = open("data/total_upload.cache", "w")
        write_total_upload.write(SPEEDUPLOAD)
        write_total_upload.close()
        total_upload2 = SPEEDUPLOAD
        SPEEDUPLOAD = SPEEDUPLOAD + ' KBps'
    if total_download == '':
        pass
    else:
        try:
            total_download = int(total_download)
            total_download2 = int(total_download2)
            truth_total_download = total_download + total_download2
            truth_total_download = str(truth_total_download)
            write_total_download = open("data/total_download.cache", "w")
            write_total_download.write(truth_total_download)
            write_total_download.close()
            truth_total_download = int(truth_total_download)
            truth_total_download = truth_total_download / 1024
            truth_total_download = str(truth_total_download)
            pttp = truth_total_download.find('.')
            if pttp == -1:
                pass
            else:
                truth_total_download = truth_total_download[:pttp]
                truth_total_download = truth_total_download + ' MB'
            read_received2.set(truth_total_download)
        except:
            pass
    if total_upload == '':
        pass
    else:
        try:
            total_upload = int(total_upload)
            total_upload2 = int(total_upload2)
            truth_total_upload = total_upload + total_upload2
            truth_total_upload = str(truth_total_upload)
            write_total_upload = open("data/total_upload.cache", "w")
            write_total_upload.write(truth_total_upload)
            write_total_upload.close()
            truth_total_upload = int(truth_total_upload)
            truth_total_upload = truth_total_upload / 1024
            truth_total_upload = str(truth_total_upload)
            pttu = truth_total_upload.find('.')
            if pttu == -1:
                pass
            else:
                truth_total_upload = truth_total_upload[:pttu]
                truth_total_upload = truth_total_upload + ' MB'
            read_sent2.set(truth_total_upload)
        except:
            pass
    if read_ping.strip() == 'Timed out':
        read_ping = read_ping.strip()
    else:
        read_ping = read_ping.strip() + 'ms'
    read_speed_upload2.set(SPEEDUPLOAD)
    read_speed_download2.set(SPEEDDOWNLOAD)
    read_ping2.set(read_ping)
    main2.after(1000, process)


def gui():
    global main_init
    global main
    global word2
    main_init = tkinter.Tk()
    main_init.title('Counting Data Usage')
    main = Canvas(main_init, width=300, height=300)
    main.pack()
    main.configure(background='white')
    word1 = Label(main, text='Welcome!', font='Vendeta 18 bold', background='white')
    main.create_window(150, 75, window=word1)
    word2 = Label(main, text='Click Here to Start !', background='white')
    main.create_window(150, 125, window=word2)
    button1 = Button(main, text='Start Now!!', command=gui_process, background='white')
    main.create_window(150, 150, window=button1)
    main.mainloop()
    system('rmdir /Q /S data')


# for i in range(101):
#     i = str(i)
#     print(i + '\r', end='')
#     sleep(0.1)

def main_self():
    prepare_init()
    write_script()
    gui()


if __name__ == "__main__":
    main_self()
