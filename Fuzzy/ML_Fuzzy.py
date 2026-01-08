# FUNGSI DAN PROSEDUR #

# Fungsi Keanggotaan suhu
def suhu_dingin(x):
    if x <= 20:
        return 1
    elif 20 < x < 30:
        return (30 - x) / 10
    else:
        return 0

def suhu_sejuk(x):
    if 20 < x < 30:
        return (x - 20) / 10
    elif 30 <= x <= 40:
        return (40- x) / 10
    else:
        return 0

def suhu_panas(x):
    if x <= 30:
        return 0
    elif 30 < x < 40:
        return (x - 30) / 10
    else:
        return 1

# Fungsi Keanggotaan kelembaban
def lembab_rendah(x):
    if x <= 30:
        return 1
    elif 30 < x < 50:
        return (50 - x) / 20
    else:
        return 0

def lembab_sedang(x):
    if 30 < x < 50:
        return (x - 30) / 20
    elif 50 <= x <= 70:
        return 1
    elif 70 < x < 90:
        return (90 - x) / 20
    else:
        return 0

def lembab_tinggi(x):
    if x <= 70:
        return 0
    elif 70 < x < 90:
        return (x - 70) / 20
    else:
        return 1
    
#fungsi Keanggotaan output (kecepatan kipas angin)
def kecepatan_rendah(x):
    if x <= 0:
        return 1
    elif 0 < x < 40:
        return (40 - x) / 40
    else:
        return 0

def kecepatan_sedang(x):
    if 20 < x < 40:
        return (x - 20) / 20
    elif 40 <= x < 60:
        return (40 - x) / 20
    else:
        return 0
    
def kecepatan_tinggi(x):
    if x <= 40:
        return 0
    elif 40 < x < 100:
        return (x - 40) / 60
    else:
        return 1
    
# INISIALISASI #

# Mengatur kecepatan kipas berdasar suhu dan kelembapan
# Suhu [16,50]: Dingin, Sejuk, Panas
# Kelembapan [10,100]: Rendah, Sedang, Tinggi
# Kecepatan kipas [0,100]

# IF Suhu=Dingin AND kelembapan=Tinggi THEN Kecepatan=Rendah
# IF Suhu=Sejuk AND kelembapan=Sedang