const puppeteer = require("puppeteer");
const fs = require('fs');
const path = require('path');
const readline = require('readline');

(async () => {
var url_count = 0

const fileStream = fs.createReadStream('urls.txt');

const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

for await (const url of rl) {
    if (url_count < 100){

    
const browser = await puppeteer.launch({headless : true})
const page = await browser.newPage()

try{
// Saves images
page.on('response', async (response) => {
    counter = 0
    const matches = /.*\.(jpg|png|svg|gif|jpeg)$/.exec(response.url());
    if (matches && (matches.length === 2)) {
      const extension = matches[1];
      const buffer =  await response.buffer().catch(() => {});
      if (buffer){
        fs.writeFileSync(`images/${url}_${counter}.${extension}`, buffer, 'base64');
        counter = counter+1
      }
      
    }
  });


await page.goto(`https://${url}`,{ waitUntil: 'networkidle2' });

// Saves text
const text = await page.$eval('*', el => el.innerText);
fs.writeFileSync(`text/${url}.txt`, text);
await browser.close();
url_count = url_count+1} catch (err){
    console.log("ERR:", err)
}
}
}
}

)();