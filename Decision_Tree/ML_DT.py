# LIBRARY #
import math
from collections import Counter

# FUNGS DAN PROSEDUR #

# Entropy
def entropy(data):
    n = len(data)
    nGrup = Counter(data)
    ent = 0.0
    for c in nGrup.values():
        p = c / n
        ent -= p * math.log2(p)
    return ent

# Gain
def gain(data_input, data_output, fitur):
    base_ent = entropy(data_output)
    base_n = len(data_output)

    # kelompok berdasarkan nilai atribut
    subsets = {}
    for x, label in zip(data_input, data_output):
        key = x[fitur]
        subsets.setdefault(key, []).append(label)
    
    subset_ent = 0.0
    for labels in subsets.values():
        subset_ent += (len(labels) / base_n) + entropy(labels)
    return base_ent - subset_ent

# Tree
def buat_tree(data_input, data_output, feature_indices):
    # semua output (label) sama -> leaf
    if len(set(data_output)) == 1:
        return data_output[0]
    
    # fitur kosong -> habis
    if not feature_indices:
        return Counter(data_output).most_common(1)[0][0]
    
    # cari fitur terbaik berdasarkan gain
    gains = [(gain(data_input, data_output, idx), idx) for idx in feature_indices]
    gains.sort(reverse=True)
    best_gain, best_fitur = gains[0]

    # Jika gain = 0 -> tidak ada peningkatan
    if best_gain == 0:
        return Counter(data_output).most_common(1)[0][0]
    
    tree = {best_fitur: {}}

    # Nilai-nilai unik fitur pada data saat ini
    values = set(x[best_fitur] for x in data_input)
    for val in values:
        # buat subset data untuk nilai fitur = val
        sub_input = [x for x, label in zip(data_input, data_output) if x[best_fitur] == val]
        sub_output = [label for x, label in zip(data_input, data_output) if x[best_fitur] == val]

        # Jika subset kosong
        if not sub_input:
            tree[best_fitur][val] = Counter(data_output).most_common(1)[0][0]
        else:
            sisa_fitur = [i for i in feature_indices if i != best_fitur]
            tree[best_fitur][val] = buat_tree(sub_input, sub_output, sisa_fitur)
    return tree

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

# MAIN PROGRAM #
tree = buat_tree(x, y, list(range(len(header_label[0:4]))))
print("Decision tree (struktur):", tree)