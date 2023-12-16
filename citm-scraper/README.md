Basic webpage scraper written in Nodejs that extracts all images and text from a webpage using puppeteer.

To use, provide URLs in ```urls.txt``` and run the following commands:
```
npm install
node index.js
```

The output should appear in the ```text``` and ```images``` folders. Files are named after the webpage (this was done for CITM's setup). You may modify line 32 if you want to change how image files are saved. Replace ```${url}_${counter}``` with ```matches[0]``` to keep original filename.


Code blocks borrowed from:

https://stackoverflow.com/questions/52542149/how-can-i-download-images-on-a-page-using-puppeteer

https://stackoverflow.com/questions/46813042/get-all-plain-text-with-puppeteer
