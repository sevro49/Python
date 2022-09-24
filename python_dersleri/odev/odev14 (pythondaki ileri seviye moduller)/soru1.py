"""
Bilgisayarınızdaki tüm mp4,txt ve pdf dosyalarını os modülüyle arayın ve bunların nerede bulunduklarını ve 
isimlerini ayrı ayrı "pdf_dosyalari.txt","mp4_dosyaları.txt","txt_dosyaları.txt" adlı dosyalara kaydedin."""

import os

for file in os.listdir("C:/Users/emreg"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))

os.listdir("C:/Users/emreg")