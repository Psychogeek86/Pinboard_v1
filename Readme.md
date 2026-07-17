# Pinboard

Pinboard is a browser extension designed for Chromium-based browsers (Chrome, Brave, Edge) that allows you to collect, organize, and protect your visual web pages and notes in a fast and elegant way.

Unlike traditional tab managers or bookmarks, Pinboard organizes your content into visual **Collections**, saving pages as actual *snapshots* complete with a graphical preview. This allows you to quickly recognize any saved element at a glance.

## 🎬 Video Demo

https://github.com/user-attachments/assets/1981c5b1-a1c2-491b-b3ce-a72ae615a54a

## 🚀 Key Features

- **Visual Snapshots:** Save web pages inside containers called "Collections", complete with graphical previews for immediate visual recognition.
- **Post-it Style Notes:** Create, edit, and save custom text notes directly inside your collections, just like digital sticky notes.
- **Privacy & Password Protection:** Lock and secure your sensitive collections by setting a password, keeping them safe from other users on the same computer.
- **Flexible Exporting:** Save and export individual elements or entire collections in various formats so you never lose your data.
- **Multi-language Support:** The extension is fully localized and available in **English, Italian, French, Spanish, German, Portuguese, Russian, and Arabic**.

## 🛡️ Release Notes & Privacy

This build was originally developed to meet my personal needs and is being shared publicly as a **free test build** to showcase the project's potential.

* **Project Status:** This project is not open-source. This build is distributed "as-is" and will not receive further support or updates. 
* **Tested & Reliable (with a catch):** I have personally tested this extension across multiple browsers, and it works correctly. However, since this is a test build, please note that minor bugs might still be present.
* **The Future (Version 2):** I am actively working on **Pinboard Version 2**. It will be completely rewritten from scratch and will eventually be released through official browser web stores and channels.
* **Privacy & Security:** This extension contains no malicious code. It does not collect, store, or transmit any of your personal data or browsing history. All data generated and saved remains strictly local on your device.

## 📦 Installation

1. Download the repository source code (or the release ZIP).
2. Extract the ZIP file to your computer.
3. Open your browser and navigate to the extensions page (e.g., `chrome://extensions` or `brave://extensions`).
4. Enable **Developer mode** via the toggle in the top-right corner.
5. Clicca **Load unpacked** in the top-left corner and select the main root folder of the project.

## 🔄 Migrating from Microsoft Edge Collections

If you are transitioning from Microsoft Edge, you can easily migrate your saved collections into Pinboard using the included Python utility script: `edge_collections_import_lite.py`.

### Prerequisites
* You must have **Python** installed on your computer.

### ⚠️ Important Note regarding Edge Sticky Notes
Please note that while the text and links of your collections will import, **it is not guaranteed that any Sticky Notes saved inside your Edge Collections will work or display correctly in Pinboard**. Even though both systems look similar, their underlying architecture is different. 

I might find a definitive solution to this limitation in the future, which would eventually be integrated into **Pinboard Version 2**. Because of this, **it is highly recommended to create a ZIP file backup of your original Edge "Collections" folder and keep it safe**, so you can preserve all your raw note data for future use.

### How to use the script:
1. Locate the script file `edge_collections_import_lite.py` in your directory.
2. Simply double-click and run the script. It will automatically scan the default Microsoft Edge directory to find your collections.
3. Once completed, the script will generate a backup file `.json` inside the exact same directory where the script was executed.

> [!IMPORTANT]
> The script automatically searches for the Edge data folder in its default location:  
> `C:\Users\<Your_User>\AppData\Local\Microsoft\Edge\User Data\Default`  
> If you have previously moved or backed up your Edge Collections folder elsewhere, you **must copy it back** into that specific default path before running the script.

### How to import the file into Pinboard:
1. Open the Pinboard extension in your browser.
2. Click on the general menu icon (the **three vertical dots** in the top-right corner).
3. Click on **"Import backup"**.
4. Select the generated `.json` file to restore all your collections.

## ☕ Support the Project

If you find Pinboard useful and want to support my work on future versions and independent development, you can buy me a coffee! Any contribution is greatly appreciated.

[![Ko-fi](https://img.shields.io/badge/Support--me--on--Ko--fi-F16061?style=flat&logo=ko-fi&logoColor=white)](https://ko-fi.com/Psychogeek)

---
