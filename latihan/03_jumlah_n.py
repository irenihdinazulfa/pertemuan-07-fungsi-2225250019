# Latihan 3: Jumlah 1 sampai n
# Uji n = 1, 5, 10, dan 100. Bandingkan dengan rumus n(n+1)/2.
def jumlah_n(n):
  total = 0
  for i in range(1, n + 1):
    total += i
  return total


print("\n--- Hasil Latihan 3 ---")
nilai_uji = [1, 5, 10, 100]

for n in nilai_uji:
  hasil_loop = jumlah_n(n)
  hasil_rumus = n * (n + 1) // 2  # Menggunakan integer division
  print(f"n = {n} -> Fungsi Loop: {hasil_loop} | Rumus n(n+1)/2: {hasil_rumus}")
  