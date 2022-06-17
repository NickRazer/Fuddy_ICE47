    # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Fuddy")
define r = Character("Rio")
define b = Character("Bagas")
define p = Character("Pak Ferdi")
define s = Character("Sony")
define m = Character("Para Siswa")

default benar = 0
default positif = 0
default negatif = 0

style startButton:
    xalign 0.5
    # xpos 600
    # ypos 600
    background Frame("gui/button_start_idle.png")
    hover_background Frame("gui/button_start_hover.png")

style infoButton:
    xalign 0.5
    # xpos 600
    # ypos 700
    background Frame("gui/info_idle.png")
    hover_background Frame("gui/info_hover.png")

style settingButton:
    xalign 0.5
    # xpos 600
    # ypos 700
    background Frame("gui/button_setting.png")
    hover_background Frame("gui/button_setting.png")

# The game starts here.

label start:
    scene bg_depansekolah
    play music suarapagihari
    "Pagi ini, Matahari bersinar begitu cerah" 
    "Menyoroti gerbang SD Patimura 1 yang siap menyambut kedatangan para siswannya."
    "Beginilah suasana SD Patmimura 1 di setiap paginya." 
    "Sejuk dan asri menyemangati para siswa untuk belajar hingga siang hari."
    #play sound Belberbunyi
    play sound bell
    "Waktu telah menunjukan pukul 06.45."
    "Bel pun berbunyi," 
    stop sound
    "Pertanda para siswa harus memasuki kelasnya untuk mempersiapkan pembelajaran yang akan dimulai pukul 7 nanti."
    
    stop music
    scene black
    with dissolve   
    jump scene1

label scene1:
    play music sekolah
    scene bg_lorong_kelas
    "Seperti biasa," 
    "Para guru akan memasuki kelas saat bel berdua berbunyi yakni pukul 07.00,"
    "Namun anehnya, meski jam masih menunjukan pukul 6.45, terlihat dari kejauhan Pak Ferdi berjalan menuju ke ruang kelas 5."
    "Selaku ketua kelas, Rio pun memberi tahu teman-temanya untuk duduk di posisi masing-masing karena Pak Ferdi akan segera tiba."

    show rio_panik at center:
        zoom 0.15 
    r "Teman-teman...Pak Ferdi otw, semuanya ayo kembali ke posisi masing-masing"
    hide rio_panik

    show bagas_cemberut at right:
        zoom 0.15
    b "Loh, kok tumben ya, padalah bel kedua belum berbunyi."
    hide bagas_cemberut
    
    #Play sound jeng-jeng
    "Pak Ferdi pun tiba di ruang kelas 5"

    show pferdi_casual_flip at center:
        zoom 0.18
    "Ini adalah Pak Ferdi, Guru wali kelas 5"
    hide pferdi_casual_flip
    show pferdi_senang at center with dissolve:
        zoom 0.18
    p "Selamat pagi para siswa sekalian..."
    "Pagi Pak...(jawab para siswa)"
    p "Anak-anak...pada hari ini, karena sekolah kita akan mengikuti lomba sekolah adiwiyata, maka bapak ibu guru harus mengikuti rapat untuk membahas persiapan lomba tersebut."
    p "Karena bapak ibu guru harus mengkuti rapat, maka agenda hari ini adalah membersihkan dan merapikan kelas kalian"
    p "Bersih-bersih akan dilakukan hingga jam istirahat tiba, setelah itu kalian harus mengikuti apel di lapangan ya..."
    p "Oiya ketua kelasnya siapa?"

    show rio_casual at right:
        zoom 0.15
    r "Saya Pak"
    hide rio_casual 
    p "Ok, Rio to"
    hide pferdi_senyum

    #play sound Knock
    "Tiba-tiba ada seseorang yang mengetuk pintu, dan ternyata ia adalah Fuddy."
    hide pferdi_senang
    show fuddy_cemas at right:
        zoom 0.15
    show pferdi_casual_flip at center:
        zoom 0.18 
    f "Permisi Pak maaf datang terlambat"
    p "Oh Fuddy, oke langsung duduk aja"
    hide fuddy_cemas
    p "Oh iya, saya lanjutkan yang tadi ya...Rio sebagai ketua kelas, tolong teman-temannya diawasi ya agar membersihkan kelas bersama"
    p "Jangan ada yang bermain sendiri ya, semuanya harus kerjasama, oke!"
    "Siap Pak..."
    p "Oh iya, satu lagi, jangan lupa besok ada ulangan sistem pencernaan, mumpung nanti pulang awal, manfaatkan waktu sebaik mungkin untuk belajar ya!"
    "Yah (Para Siswa menolak ulangan)"

    show rio_senang at right:
        zoom 0.15
    r "Soalnya jangan banyak-banyak ya, Pak. Hehe..."
    hide rio_senang

    hide pferdi_casual_flip
    show pferdi_senang at center with dissolve:
        zoom 0.18
    p "Santai saja, ulangan tidak akan jauh-jauh dengan latihan soal yang kita bahas pada pertemuan sebelumnya kok." 
    p "kalian ulangi saja soal latihan kemarin, dan baca juga ya materi di buku"
    hide pferdi_senang
    show pferdi_terkejut_flip at center with dissolve:
        zoom 0.18
    p "Oh iya, Fuddy, kamu kemarin tidak berangkat 2 kali ya di kelas saya, minggu kemarin dan minggu ini?"
    
    show fuddy_bingung at right:
        zoom 0.15
    f "Iya Pak, kemarin saya sakit pak"
    hide fuddy_bingung
    hide pferdi_terkejut_flip
    show pferdi_casual_flip at center:
        zoom 0.18
    p "Oke, Habis ini kamu ikut ke ruang saya ya Fuddy!"
    show fuddy_senang at right:
        zoom 0.15
    f "Baik, Pak"
    hide fuddy_senang

    hide pferdi_casual_flip
    show pferdi_senang at center:
        zoom 0.18
    p "Oke anak-anak, selamat dan semangat bersih-bersihnya"
    m "Baik Pak"
    hide pferdi_senang with dissolve
    "Pak Ferdi pun meninggalkan kelas"
    "Sony dan Rony, teman sekelas Fuddy pun menakut-nakutinya yang akan menemui Pak Ferdi di kelas"
    show sony_flip at center:
        zoom 0.15
    s "Hayyo Fuddy, Selamat dan semangat yan ke ruang Pak Ferdi nya..."
    s "Hahah makanya jangan hobi bolos dong Fud..."
    show fuddy_bingung at right with dissolve:
        zoom 0.15
    "Fuddy pun kesal dengan Soni dan Roni karena ia dituduh membolos , padahal dia sakit. Namun Fuddy hanya terdiam dan meninggalkan kelas menuju ke ruang Pak Ferdi"
    hide fuddy_bingung with dissolve
    hide sony_flip with dissolve

    
    scene black
    with dissolve
    jump scene2

label scene2:
    scene bg_lorong_kelas
    show fuddy_cemas at center :
        zoom 0.15
    f "Duh kenapa ya kok aku dipanggil, padahal kan aku sudah memberikan surat izin..."

    scene bg_ruangguru
    show fuddy_casual at right with dissolve:
        zoom 0.15
    "Tibalah Fuddy di ruang Pak Ferdi"
    show pferdi_terkejut_flip with dissolve:
        zoom 0.18
    p "Ya Fuddy, sini masuk"
    f "Baik, Pak."
    show fuddy_cemas at right with dissolve:
        zoom 0.15
    hide pferdi_terkejut_flip    
    show pferdi_senang_flip at center with dissolve:
        zoom 0.18
    p "Tidak usah tegang gitu Fuddy, santai saja bapak cuma mau tanya, kamu kok sudah dua kali izin dikelas bapak itu kenapa ya..."
    f"Pada minggu kemarin, saya izin tidak berangkat karena penjaga kandang sapi dipanti sedang sakit Pak, jadi saya yang harus memberi makan dan membersihkan kandang"
    f "Lalu pada pertemuan minggu ini, saya terkena diare karena tertular sapi yang saya rawat Pak, kebetulan sapi yang saya rawat terkena diare, Pak."
    show pferdi_tertawa_flip at center with dissolve:
        zoom 0.18
    "Pak Ferdi pun tertawa berbahak-bahak"
    hide fuddy_cemas
    show fuddy_bingung at right with dissolve:
        zoom 0.15
    f"Ada yang salah Pak?"
    hide pferdi_tertawa_flip
    show pferdi_senang_flip at center with dissolve:
        zoom 0.18
    p "Kamu ini lucu sekali Fuddy, makanan mana ada tertular diare, tertular sapi lagi."
    p "Makanya, meskipun tidak berangkat, harusnya kamu tetap membaca buku ya, dan tanya temenmu tentang materi apa yang dipelajari saat kamu tidak masuk."
    hide fuddy_bingung
    show fuddy_senang at right with dissolve:
        zoom 0.15
    f "Baik, Pak. Lain kali akan saya lakukan hehehe..."
    hide pferdi_senang_flip
    show pferdi_casual_flip at center:
        zoom 0.18
    p "Oke, Jadi begini Fuddy, kamu masih ingat kan kalau besok kita ada ulangan tentang materi proses pencernaan makanan?"
    hide fuddy_senang
    show fuddy_casual at right with dissolve:
        zoom 0.15
    f "Iya Pak, saya ingat"
    p "Oke, jadi saat kamu kemarin tidak berangkat, pembelajaran di kelas itu membahas tentang pencernaan makanan di tubuh manusia dan hewan, iklan kesehatan pencernaan, dan manfaat makanan sehat bagi tubuh kita."
    p " Nah pembelajaran singkat tentang materi ada di buku ya, sebagai pemantapan, akan saya kirimkan link latihan soal kepada ibu asuhmu ya."
    p "Akan ada 3 link yang berisi latihan soal pencernaan manusia, pencernaan hewan, dan interaksi sosial dan lingkungan."
    f "Baik pak saya akan belajar, lalu mengerjakan soal latihan tersebut..."
    p "Bapak kirimkan 3 link ya, dan latihan tersebut adalah sebuah tahapan yang harus dikerjakan dengan urut, kamu harus menyelesaikan link pertama untuk dapat lanjut ke latihan berikutnya, dan seterusnya, paham kan?"
    f "Paham, Pak..."
    p "Jika kamu bisa  menuntaskan latihan-latihan tersebut, saya jamin kamu pasti bisa mengerjakan soal ulangan besok, karena tidak akan jauh dari pembahasan besok."
    hide fuddy_casual
    show fuddy_senang at right:
        zoom 0.15
    f "Siap, Pak!"
    p "Okey, Kalo begitu silahkan kamu kembali ke kelas untuk bersih-bersih."
    f "Baik, Pak. Terima kasih."
    
    scene bg_lorong_kelas:
    "Fuddy pun kembali ke kelas"
    scene bg_kelas_kotor with dissolve:
    "Sesampainya di kelas, Fuddy pun langsung membantu bersih-bersih."

    #Scene Ruang kelas bersih:
    #play sound Bel istirahat
    "Tidak terasa, bel istirahat pun berbunyi, pertanda apel akan segera dimulai, tepat sekali dengan bersih-bersih kelas yang sudah selesai,"
    scene bg_kelas_bersih with dissolve:
    "Kelas pun menjadi sangat rapi dan bersih."
    "Para siswa pun berkumpul di lapangan"

    scene bg_lapangansekolah:
    "Di lapangan, Bapak Kepala Sekolah pun menyampaikan bahwa sekolah akan mengikuti lomba Adiwiyata, sehingga setiap siswa harus menjaga kebersihan lingkungan sekolah agar sekolah terlihat bersih dan astri"
    "Setelah selesai menyampaikan informasi, para siswa pun dibubarkan untuk dapat pulang kerumah."

    #scene ruang kelas:
    "Fuddy dan teman-temanya pun pulang ke rumah masing-masing"

    scene bg_kamar:
    show fuddy_baju_tidur_flip at left:
        zoom 0.15
    "Sesampainya di kamar, Fuddy pun langsung bergegas untuk belajar mempersiapkan ulangan."
    menu:
        "Berdasarkan pesan Pak Ferdi, Fuddy harus mempelajari materi apa?"
        "Pola Makan Sehat":
            play sound click
            scene bg_kamar
            show fuddy_baju_tidur_flip at left:
                zoom 0.15
            f "Wah kurang tepat ya kawan."
            "Jawaban yang benar adalah Sistem Pencernaan Manusia"
            $negatif += 1
        "Sistem Pencernaan Manusia":
            play sound click
            scene bg_kamar
            show fuddy_baju_tidur_flip at left:
                zoom 0.15
            f "Wah tepat sekali!"
            $positif += 1

    "Baru saja membuka buku, Fuddy melihat bagian-bagian tubuh hewan dan manusia yang digunakan untuk mencerna makanan, melihat gambar tersebut, mental Fuddy pun down."
    f "Ya ampun gambar apa ini, aduh kok aku asing sekali dengan materi ini"
    f "Sepertinya aku harus kerumah Rony untuk meminta diajari"
    f "Tapi kok ngantuk ya, yasudah deh tidur dulu."
    hide fuddy_baju_tidur

    "Fuddy pun tidur dan mengatur alarm untuk 1 jam kedepan, saat bangun, ia akan pergi kerumah Soni untuk mengajaknya belajar bersama."

    "To Be Continue..."



    # This ends the game.
    return
