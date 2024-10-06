# TOMARKET AUTO

TOMARKET Telegram Mini App Bot Auto

> [!NOTE]
> This is a paid script that requires a valid license key to operate. For more information, please visit the [Dzuhri Auto](https://irhamdz.notion.site/Dzuhri-Auto-10f53e55353080f98fbae250bd7172d1) page.

## Features

- Auto Claim Daily Check-in
- Auto Farming
- Auto Claim Combo
- Auto Clear Mission / Tasks
- Auto Play Game

## Supported Modes

- Using Session

> [!WARNING]
> *When using `session mode`, please make sure to only add a Telegram account with an ID number below `61xxxxx`. You can check your ID by using `@userinfobot`. If your ID is higher than this, your account will be automatically banned.*

## Supported Operating Systems

- VPS
- Windows
- Mac
- Android (using Termux)

## Prerequisites

Before setting up the bot, ensure the following are installed:

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/) (version 3.10.0 - 3.11.9)

## .env Settings

All the configurations can be set in the .env file.

| Name                    | Description                                      | Default    |
| ----------------------- | ------------------------------------------------ | ---------- |
| LICENSE_KEY             | Custom LICENSE KEY                               |            |
| API_ID / API_HASH       | API and API HASH from telegram account           |            |
| POINTS_COUNT            | Random skor untuk setiap game                    | [450, 600] |
| AUTO_PLAY_GAME          | Auto Play Game                                   | True       |
| AUTO_TASK               | Auto Clear Tasks                                 | True       |
| AUTO_DAILY_REWARD       | Auto Claim Daily Reward                          | True       |
| AUTO_CLAIM_STARS        | Auto Claim Stars                                 | True       |
| AUTO_CLAIM_COMBO        | Auto Claim Daily Combo                           | True       |
| USE_RANDOM_DELAY_IN_RUN | Mengaktifkan delay sebelum menjalankan bot       | True       |
| RANDOM_DELAY_IN_RUN     | Random delay dalam detik sebelum menjalankan bot | [5, 30]    |
| USE_PROXY_FROM_FILE     | Menggunakan proxy                                | False      |

## How to Obtain API ID and API HASH

1. Go to [my.telegram.org](https://my.telegram.org/) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

<!-- ## How to obtain and use Query ID

To get the Query ID, [read this guide.](https://irhamdz.notion.site/Tutorial-Get-Query-ID-f415621d4a9843d2a7a9ad2cfb9abeb4?pvs=74)

Once you have the Query ID, add it to the `query_ids.txt` file.</br>
If you're using multiple accounts, simply add each query ID on a new line, like this:

```bash
query_id=xxxxxxxxx-User1
query_id=xxxxxxxxx-User2
``` -->

## How to Use Proxy

To use proxy, [read this guide.](https://irhamdz.notion.site/Use-Proxy-11153e553530807aaa14fdfde425723c?pvs=74)

To buy cheap proxy, [buy cheap proxy here](https://proxy-seller.com/?partner=QJGZSHEU86WI9Y)

## Installation Guide

### Step 1: Clone the Repository to Your PC / VPS

Run the following command to clone the repository:

```shell
git clone https://github.com/dzuhri-auto/tomarket.git
```

### Step 2: Navigate to the Project Folder

Once cloned, navigate to the project directory:

```shell
cd tomarket
```

### Step 3: Install the Dependencies

Run the following commands based on your operating system:

**Windows (Using Powershell)** :

```powershell
py -m venv venv
.\venv\Scripts\Activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

**Mac / Linux** :

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install wheel
pip3 install -r requirements.txt
cp .env-example .env
```

***Note : dont forget to edit `.env` file***

## Using the License Key

After installation, you need to input your license key in the `.env` file.

If you don't have a license key yet, you can purchase one here: [Buy the license key](https://irhamdz.notion.site/Dzuhri-Auto-10f53e55353080f98fbae250bd7172d1)

Once you have it, add it to your `.env` file like this:

```note
LICENSE_KEY="Your License Key"
```

## Starting the Bot

Run the bot using the following commands, depending on your operating system:

**Windows (Using Powershell)** :

```powershell
.\venv\Scripts\Activate
py main.py
```

**Mac / Linux** :

```shell
source venv/bin/activate
python3 main.py
```
