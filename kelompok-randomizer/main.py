from random import randrange

def gen_group(students, members):
	result = {}
	count = 0
	curr_group = []
	while students:
		group_length = len(curr_group)
		if group_length < members:
			student = students[randrange(0, len(students))]
			curr_group.append(student)
			students.remove(student)
		if group_length >= members or (curr_group and not students):
			count += 1
			result[f"Kelompok {count}"] = curr_group
			curr_group = []

	return result
	
if __name__ == "__main__":
	students = ["Ade Ilham Hidayat", "Adya Nadila Putri Nugraha", "Adytia Dwi Putra",
			 "Agnia Maulida", "Anis Pitria", "Asep Lutfi", "Azizah Nur Aisiyah",
			 "Azril Ramdani", "Chania Dewi", "Dendi Pamungkas", "Devita Lizyanti Rinjani Nur Saputri",
			 "Elisa Oktaviani", "Erin Kalisna", "Farel Tsany Angkasa", "Gita Jamaatul Hasanah", "Hasyim Asyari",
			 "Indrya Fadisya Putri", "Kheila Khoerunisa", "Muhammad Anwar Musadad", "Muhammad Galih Nugraha", "Muhammad Haikal Hilalul Hamdi",
			 "Na Diva", "Nabil Maulana Alhakim", "Nita Nur Amalia", "Opik", "Pebi Pebriyanti", "Radikha Alief Heryanto",
			 "Rikja Nur Fikri", "Rispa Lailatinur", "Riyanti Nur Apriliyani", "Sheila Nuurlaila", "Susi Sumiati", "Talia Astriani",
			 "Titin Supriyatin", "Muhammad Arya", "Irpa Saripah"]
	members_per_team = int(input("Masukan anggota per kelompok: "))
	groups = gen_group(students, members_per_team)
	print("\nHasil Pembagian Kelompok secara Acak untuk Tugas PPKn.")
	for key in groups:
		print(f" {key} = {', '.join(groups[key])}")
