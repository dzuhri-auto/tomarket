# Tomarket AUTO

Tomarket Telegram Mini App Bot

For README in English: [![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/dzuhri-auto/tomarket/blob/master/README.md)

## Fitur

- Auto Claim Daily Check-in
- Auto Farming
- Auto Claim Combo
- Auto Clear Mission / Tasks
- Auto Play Game

## .env Settings

| Name | Description | Default |
| --- | ----------- | --------- |
| API_KEY | Custom API KEY | |
| API_ID / API_HASH | API and API HASH from telegram account | |
| POINTS_COUNT | Random skor untuk setiap game  | [450, 600] |
| AUTO_PLAY_GAME | Auto Play Game | True |
| AUTO_TASK | Auto Clear Tasks | True |
| AUTO_DAILY_REWARD | Auto Claim Daily Reward| True |
| AUTO_CLAIM_STARS | Auto Claim Stars | True|
| AUTO_CLAIM_COMBO | Auto Claim Daily Combo | True |
| USE_RANDOM_DELAY_IN_RUN | Mengaktifkan delay sebelum menjalankan bot | True |
| RANDOM_DELAY_IN_RUN | Random delay dalam detik sebelum menjalankan bot | [5, 30] |
| USE_PROXY_FROM_FILE | Menggunakan proxy | False |

## Persiapan

Cara Mendapatkan API ID and API HASH:

1. Buka [my.telegram.org](https://my.telegram.org/) via browser, lalu login dengan akun telegram mu.
2. Pilih menu `API development tools` dan isi form nya untuk mendaftarkan aplikasi baru.
3. Simpan `API_ID` dan `API_HASH` yang diberikan setelah mendaftarkan aplikasi ke file .env.

Pastikan kamu sudah menginstal:

- [Python](https://www.python.org/downloads/release/python-31014/) **versi 3.10**

## Mendapatkan API KEY

Script ini menggunakan kustom API KEY, API KEY nya hanya tersedia untuk disewa.

Kamu bisa chat saya, [Irham](https://t.me/irhamdz) untuk menanyakan harga sewanya!

## Install

Clone ke PC / VPS kamu:

```shell
git clone https://github.com/dzuhri-auto/tomarket.git
```

Masuk ke folder:

```shell
cd tomarket
```

Kemudian gunakan perintah ini untuk instal otomatis:

**Windows** :

```shell
windows\install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh ubuntu/update.sh
```

```shell
./ubuntu/install.sh
```

***note : Jangan lupa untuk mengedit file `.env`***

## Update API KEY

Setelah instalasi, kita bisa memperbarui menggunakan API KEY:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="YOUR API KEY"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="YOUR API KEY"/' .env

# contoh jika API KEY kamu = "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Menjalankan Bot

Untuk menjalankan bot:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```

## Update Bot

FUntuk update bot:

**Windows** :

```shell
windows\update.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/update.sh
```
