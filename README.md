# 🖼️ InterNACHI Gallery Scraper

currently only gets the thumbnails.  having issues with anti scraping or some weird hooks.  you're welcome to try, i may get to it when i get some spare time.

This Python project automates logging into the [InterNACHI](https://www.nachi.org/) member portal, navigating to the **Home Inspection Image Gallery**, and downloading all available images from every gallery category.

It was developed by **Kanawha IT Security LLC** as a tool to assist inspectors in building a local library of illustrations and diagrams from the InterNACHI marketing resources.

The project is released into the public domain under **The Unlicense** and is free for anyone to use, modify, or distribute.

---

## 📜 Features

This tool automatically:
- Logs into InterNACHI using your member credentials
- Navigates to the "Marketing" section and the Image Gallery
- Dynamically scrapes all gallery categories found on the page
- Downloads images from each category, including Cloudinary-hosted files
- Avoids re-downloading images already saved locally
- Provides download status feedback as it runs
- Supports running headless or with the browser visible

---

## 🛠 Requirements

To run this scraper, you need:
- Python 3.9 or newer installed
- The following Python libraries installed:
  - `playwright`
  - `requests`

You can install them using the following commands:
```
pip install playwright requests
playwright install
```
The `playwright install` step downloads the required Chromium browser for automation.

---

## 🚀 How to Use

Before running the script, edit the `scraper.py` file and replace the placeholder credentials with your own valid InterNACHI login information:

Replace:
```
USERNAME = "user-name"
PASSWORD = "password"
```
with your actual **InterNACHI Username** and **Password**.

Once your credentials are set, run the script by executing:
```
python scraper.py
```

The script will launch a browser window, perform the login, and navigate to the gallery. It automatically detects and cycles through all gallery categories, downloading images into a folder named `downloaded_images`.

If the folder does not exist, it will be created automatically. Images already downloaded will be skipped to avoid duplicates.

---

## ⚙️ Options and Notes

The browser runs in visible mode by default (`headless=False`) so you can monitor its progress. If you prefer to run it silently, you can edit the script and change:
```
browser = p.chromium.launch(headless=False)
```
to:
```
browser = p.chromium.launch(headless=True)
```

The script handles:
- Session management
- Login redirects
- Dynamic content loading
- Cloudinary asset fetching
- Download resumption without duplicates

When finished, the downloaded images are saved in the following structure:
```
nachi-gallery-scraper/
│
├── scraper.py
├── README.md
└── downloaded_images/
    ├── image1.jpg
    ├── image2.png
    ├── ...
```

---

## 📄 License - The Unlicense

This project is released into the Public Domain under **The Unlicense**.

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

There are no restrictions or limitations. Attribution is appreciated but not required.

Full license text: [https://unlicense.org/](https://unlicense.org/)

---

## 🤝 Credits

**Developed by:**  
Kanawha IT Security LLC  
[https://kitswv.com](https://kitswv.com)  
📧 **tim@kitswv.com**

**Script development and troubleshooting assistance provided by:**  
Larry Jones, OpenAI’s ChatGPT

---

## ✅ Summary

This tool is designed to assist home inspectors and InterNACHI members in building a complete, local collection of visual aids directly from the InterNACHI image galleries. It automates the tedious process of downloading each illustration by hand and ensures you have an organized set of images ready for use in reports, marketing materials, or training guides.

Follow the simple installation and usage steps above, and you’ll have a full backup of the gallery in minutes.

No additional configuration is needed once the script is set up — run it as often as needed to grab new images.

