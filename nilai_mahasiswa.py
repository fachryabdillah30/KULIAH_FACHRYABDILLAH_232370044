def fungsi_total_nilai(var_harian, var_uts, var_uas) :
  var_harian =int(var_harian) * 0.3
  var_uts = int(var_uts) * 0.3
  var_uas = int(var_uas) * 0.4
  
  var_total = var_harian + var_uts + var_uas
  return  var_total

print("nilai harian anda : ")
har = input()

print("nilai uts anda : ")
uts = input()

print("nilai uas anda : ")
uas = input()

nilai = fungsi_total_nilai(har, uts, uas)

print("Nilai anda adalah : ", nilai)