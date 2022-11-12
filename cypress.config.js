const { defineConfig } = require("cypress");

module.exports = defineConfig({
  // reporterOptions: {
  //   "overwrite": true,
  //   "html": true,
  //   "json": false,
  //   "code": true,
  //   "timestamp": "mmddyyyy-HHMMss",
  // },
  e2e: {
    experimentalSessionAndOrigin: false,
    video: false,
    screenshots: false,
    // setupNodeEvents(on, config) {
    //   on('before:browsers:launch', (browser = {}, launchOptions) => {
    //     if(browser.name === 'chrome') {
    //       launchOptions.args.push('--disable-site-isolation-trials');
    //       launchOptions.args.push('--window-size=1920,1080');
    //       return launchOptions;
    //     }
    //   })
    // }
  },
  chromeWebSecurity: false,

});