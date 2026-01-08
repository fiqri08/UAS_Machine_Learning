# LIBRARY #
from collections import Counter

# FUNGSI DAN PROSEDUR #

# Buat model Naive Bayes
def naiveBayes(x, y):
    model = {}
    output = Counter(y)
    N = len(y)
    probabilitas_fitur = {} #Likelihood

    model["prior"] = {k: output[k]/N for k in output}

    for k in output:
        probabilitas_fitur[k] = {}
        x_k = [x[i] for i in range(len(x)) if y[i] == k] #ambil semua data dengan output k

        for f in range(len(x[0])):
            probabilitas_fitur[k][f] = {} #kelas K, fitur f
            fitur_f = [xf[f] for xf in x_k] #ambil semua nilai fitur f untuk kelas k
            kategori_count = Counter(fitur_f) #hitung jumlah kemunculan setiap kategori
            n_kategori = len(fitur_f)

            for v in kategori_count:
                probabilitas_fitur[k][f][v] = kategori_count[v] / n_kategori #kelas K, fitur f, probabilitas nilai v
        
    model["likelihood"] = probabilitas_fitur
    return model

# Prediksi
def prediksi_naiveBayes(model, x):
    probabilitas = {}

    for k in model["prior"]:
        probabilitas_x = model["prior"][k] #mulai dengan prior
        for f in range(len(x)):
            probabilitas_x *= model["likelihood"][k][f].get(x[f], 1e-6) #kalikan dengan likelihood fitur f
        probabilitas[k] = probabilitas_x
    return max(probabilitas, key=probabilitas.get)

# INISIALISASI #

# Outlook = [1=Sunny, 2=Overcast, 3=Rain],
# Temperatur = [1=Hot, 2=Cool, 3=Mild],
# Humidity = [1=Normal, 2=High],
# Wind = [1=Strong, 2=Weak],
# Play = [0=No, 1=Yes]
header_label = ["Outlook", "Temperature", "Humidity", "Wind", "Play"]
x = [[1, 1, 2, 2],
     [1, 1, 2, 1],
     [2, 1, 2, 2],
     [3, 3, 2, 2],
     [3, 2, 1, 2],
     [3, 2, 1, 1],
     [2, 2, 1, 1],
     [1, 3, 2, 2],
     [1, 2, 1, 2],
     [3, 3, 1, 2],
     [1, 3, 1, 1],
     [2, 3, 2, 1],
     [2, 1, 1, 2],
     [3, 3, 2, 1]]
y = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]

x_uji = [3, 1, 1, 2]
y_uji = []

# MAIN PROGRAM #
model_naiveBayes = naiveBayes(x, y)
prediksi = prediksi_naiveBayes(model_naiveBayes, x_uji)
print(prediksi)