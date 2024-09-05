# TOMARKET AUTO

## Persiapan

Pastikan kamu sudah install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**

## Cara Ambil Query ID

<https://irhamdz.notion.site/Cara-ambil-session-atau-query-id-c74ba0ccb66e45a6a9ef3182638a736f>

## Request API KEY

Script ini butuh custom API KEY , API KEY nya cuma disewakan only.

Chat [Irham](https://t.me/irhamdz) "bang mau sewa api key", buat harga sewa nya !

## Install

git clone ke pc / vps kamu:

```shell
git clone https://github.com/dzuhri-auto/tomarket.git
```

Masuk ke folder nya

```shell
cd tomarket
```

Lalu bisa pake command dibawah untuk otomatis install:

**Windows** :

```shell
install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh ubuntu/update.sh
```

```shell
./ubuntu/install.sh
```

***note : jangan lupa di isi `.env` nya***

## Update API KEY

Setelah install lalu kita update API KEY kita:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="GANTI PAKE API KEY KAMU"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="GANTI PAKE API KEY KAMU"/' .env

# contoh misalkan API KEY kamu "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Start Bot

Untuk menjalankan bot bisa pake command dibawah ini:

**Windows** :

```shell
run.bat
```

**Mac / Linux / VPS** :

```shell
. ubuntu/run.sh
```

## Update Bot

Untuk update bot bisa pake command dibawah ini:

**Windows** :

```shell
update.bat
```

**Mac / Linux / VPS** :

```shell
. ubuntu/update.sh
```
