# Latihan 5: Eksperimen Scope
x = 10  # Variabel global (berada di luar fungsi)


def demo(x):
  y = x + 5  # Parameter x lokal bernilai 20, sehingga y = 20 + 5 = 25
  print("di dalam fungsi:", x, y)  # Keluaran: di dalam fungsi: 20 25
  return y


hasil = demo(20)  # Memanggil fungsi demo dengan argumen 20
print("di luar fungsi:", x, hasil)  # Keluaran: di luar fungsi: 10 25