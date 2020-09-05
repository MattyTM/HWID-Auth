import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter, subprocess
import discord_webhook
import socket
from discord_webhook import DiscordWebhook
from colorama import Fore, init
from datetime import date
from tkinter import filedialog, messagebox

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get(' PUT YOUR PASTEBIN /RAW HERE ') # Here you have to put your pastebin where are the HWID's

try:
    if hwid in r.text:
        pass
    else:
        os.system("cls")
        print(f"[ERROR] YOUR ERROR ")
        print(f'Your HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    os.system("cls")
    print(f"[ERROR] YOUR ERROR")
    time.sleep(5) 
    os._exit() 
