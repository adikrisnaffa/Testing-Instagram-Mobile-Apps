![Teks][def]

[def]: Python.gif

# Testing Instagram Mobile Apps
Disini saya menggunakan Appium Server, Appium Inspector dan Python sebagai bahasa untuk melakukan Testing Automationnya

## Instalasi
1. Appium Server
 - Pastikan komputer Anda sudah terinstal Node.js. Anda dapat mengunduh dan menginstal Node.js di situs web resminya, https://nodejs.org/en/download/.
 - Buka Command Prompt atau PowerShell dengan hak akses administrator.
 - Jalankan perintah berikut untuk menginstal Appium secara global: npm install -g appium
 - Setelah Appium terinstal, cek versi Appium yang terpasang dengan menjalankan perintah: appium -v
 - Selanjutnya, Anda perlu menginstal Appium Doctor, alat yang membantu Anda memeriksa apakah lingkungan pengembangan Anda sudah siap untuk menjalankan Appium. Jalankan perintah berikut untuk menginstal Appium Doctor: npm install -g appium-doctor
 - Setelah Appium Doctor terinstal, jalankan perintah berikut untuk memeriksa lingkungan pengembangan Anda: appium-doctor
 - Jika semua persyaratan yang diperlukan telah dipenuhi, Anda dapat memulai Appium Server dengan menjalankan perintah: appium
 - Appium Server sekarang sudah berjalan dan siap digunakan untuk menguji aplikasi di perangkat seluler.

2. Appium Inspector
 - Pastikan komputer Anda sudah terinstal Node.js dan Appium Server. Anda dapat mengunduh dan menginstal Node.js dari situs web resminya, https://nodejs.org/en/download/. Untuk menginstal Appium Server, ikuti langkah-langkah yang saya jelaskan di pertanyaan sebelumnya atau kunjungi situs web resmi Appium, https://appium.io/.
 - Buka Command Prompt atau PowerShell dengan hak akses administrator.
 - Jalankan perintah berikut untuk menginstal Appium Desktop, yang berisi Appium Inspector: npm install -g appium-desktop
 - Setelah Appium Desktop terinstal, jalankan Appium Desktop dengan mencarinya di menu Start atau melalui Command Prompt atau PowerShell dengan menjalankan perintah: appium-desktop
 - Setelah Appium Desktop terbuka, klik tab "Inspector".
 - Untuk terhubung dengan perangkat seluler, Anda dapat menggunakan kabel USB atau WiFi. Untuk menghubungkan perangkat melalui USB, pastikan perangkat seluler Anda terhubung ke komputer melalui kabel USB dan mode pengembang serta USB debugging telah diaktifkan. Untuk menghubungkan perangkat melalui WiFi, pastikan perangkat seluler dan komputer terhubung ke jaringan WiFi yang sama.
 - Klik tombol "Start Session" di bagian atas jendela Appium Inspector untuk memulai sesi pengujian.
 - Setelah sesi dimulai, Anda dapat menavigasi dan menguji aplikasi dengan Appium Inspector.