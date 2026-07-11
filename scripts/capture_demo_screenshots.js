#!/usr/bin/env node
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const path = require('path');
const { pathToFileURL } = require('url');

const repo = path.resolve(__dirname, '..');
const out = path.join(repo, 'docs/demos/screenshots');

(async () => {
  const browser = await chromium.launch({headless: true});

  async function capture(url, filename, width, height, waitMs = 1000) {
    const page = await browser.newPage({viewport: {width, height}, deviceScaleFactor: 1});
    await page.goto(url, {waitUntil: 'load', timeout: 120000});
    await page.waitForTimeout(waitMs);
    await page.screenshot({path: path.join(out, filename), fullPage: false});
    await page.close();
    console.log(filename);
  }

  await capture('http://127.0.0.1:8899/demos/thread-canvas-demo.html', 'thread-canvas-workflow.png', 1600, 1000, 1400);
  await capture('http://127.0.0.1:8899/demos/paper-plan-demo.html', 'paper-plan-browser.png', 1600, 1200, 1000);
  const valueBrowser = process.env.VALUE_BROWSER_HTML;
  if (valueBrowser) {
    const valuePage = await browser.newPage({viewport: {width: 1600, height: 1000}, deviceScaleFactor: 1});
    await valuePage.goto(pathToFileURL(path.resolve(valueBrowser)).href, {waitUntil: 'load', timeout: 120000});
    await valuePage.waitForTimeout(3000);
    const valueRows = await valuePage.$$('#featureRows tr');
    if (valueRows.length > 2) await valueRows[2].click();
    await valuePage.waitForTimeout(500);
    await valuePage.screenshot({path: path.join(out, 'value-action-feature-atlas.png'), fullPage: false});
    await valuePage.close();
    console.log('value-action-feature-atlas.png');
  } else {
    console.log('VALUE_BROWSER_HTML is unset; preserving the checked-in Value Feature Browser cover.');
  }

  await browser.close();
})().catch(err => { console.error(err); process.exit(1); });
