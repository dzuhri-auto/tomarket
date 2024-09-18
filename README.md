# Tomarket AUTO

Tomarket Telegram Mini App Bot

For README in Bahasa Indonesia: [![en](https://img.shields.io/badge/README-id-red.svg)](https://github.com/dzuhri-auto/tomarket/blob/master/README.id.md)

## Feature

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
| POINTS_COUNT | Randomize score for each game  | [450, 600] |
| AUTO_PLAY_GAME | Auto Play Game | True |
| AUTO_TASK | Auto Clear Tasks | True |
| AUTO_DAILY_REWARD | Auto Claim Daily Reward| True |
| AUTO_CLAIM_STARS | Auto Claim Stars | True|
| AUTO_CLAIM_COMBO | Auto Claim Daily Combo | True |
| USE_RANDOM_DELAY_IN_RUN | Activate delay before start the bot | True |
| RANDOM_DELAY_IN_RUN | Randomize delay in seconds before start the bot | [5, 30] |
| USE_PROXY_FROM_FILE | For using proxy | False |

## Prerequisites

Obtain API ID and API HASH:

1. Go to [my.telegram.org](https://my.telegram.org/) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the .env file.

Make sure you already install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**
  
### Disclaimer

Please only use telegram account with id below `61xxxxx`, check `@userinfobot` for checking the id.
Otherwise the account will got automatically banned !!

## Request API KEY

This script use custom API KEY, The API KEY itself is for rent only

you can chat me, [Irham](https://t.me/irhamdz) to ask how much the rent price !

## Install

Clone to your PC / VPS:

```shell
git clone https://github.com/dzuhri-auto/tomarket.git
```

Go inside to the folder:

```shell
cd tomarket
```

Then use this command for automatic install:

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

***note : dont forget to edit file `.env`***

## Update API KEY

After install we can update using API KEY:

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

# example if your API KEY = "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Start Bot

For run the bot:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```

## Update Bot

For update the bot:

**Windows** :

```shell
windows\update.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/update.sh
```
