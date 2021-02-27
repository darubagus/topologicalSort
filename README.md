# Tucil-2-Stima-2020

Program ini dibuat untuk memenuhi tugas Mata Kuliah **IF 2211 Strategi Algoritma** <br />

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2020/2021*


## Description
Dalam menyelesaikan persoalan topological sort untuk course scheduling menggunakan metode decrease-and-conquer, saya memanfaatkan data structure berupa array. Array digunakan untuk menyimpan course beserta mata kuliah prerequisite nya, serta untuk menyimpan course yang dapat diselenggarakan di setiap semesternya.<br />

Langkah-langkah program :
1. Membaca file persoalan topological sort yang akan diselesaikan, lalu dilakukan parsing pada setiap course untuk dimasukkan ke dalam array listOfCourse.
2. Selama list listOfCourse masih belum kosong, dilakukan looping untuk penghapusan course yang tidak memiliki prerequisite.
   a. Mencari course yang tidak memiliki prerequisite kemudian memasukkannya ke dalam array noPrereq.
   b. Lakukan penghapusan course terkait di dalam list course lainnya apabila course tersebut menjadi prerequisite dari course lainnya.
   c. Lakukan penghapusan course terkait dari array listOfCourse.
   d. Tambahkan array noPrereq ke dalam array courseSemester. index dari array courseSemester merepresentasikan pada semester berapa course tersebut diambil.

**LINK LAPORAN** <br />
*http://bit.ly/bukanLaporanTucil2Stima*

## Screenshot
![Example screenshot](./doc/img/1.png)
![Example screenshot](./doc/img/2.png)
![Example screenshot](./doc/img/3.png)

### Build With

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Libraries

- Roman

```
$ pip3 install roman
```

## Getting Started

### Executing program

- Buka Terminal atau Command Line
- Arahkan directory ke dalam folder yang berisi file dan folder yang sudah di download
- Kemudian arahkan directory ke dalam folder src (topologicalSort\src)
- Run program dengan command dibawah ini :

```
$ python3 topoSort.py
```


## Author
Daru Bagus Dananjaya (13519080)
