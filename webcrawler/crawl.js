const { JSDOM } = require("jsdom");


function getURLsFromHTML(htmlBody, baseURL) {
  const urls = [];
  const dom = new JSDOM(htmlBody);
  const aElements = dom.window.document.querySelectorAll("a");
  for (const aElement of aElements) {
    if (aElement.href.slice(0, 1) === "/") {
      try {
        urls.push(new URL(aElement.href, baseURL).href);
      } catch (err) {
        console.log(`${err.message}: ${aElement.href}`);
      }
    } else {
      try {
        urls.push(new URL(aElement.href).href);
      } catch (err) {
        console.log(`${err.message}: ${aElement.href}`);
      }
    }
  }
  return urls;
}

function normalizeURL(urlString) {
    const urlObj = new URL(urlString);
    const hostPath = `${urlObj.hostname}${urlObj.pathname}`;
    if (hostPath.length > 0 && hostPath.slice(-1) === "/") {
        return hostPath.slice(0, -1);
    }
    return hostPath;
}

async function crawlPage(baseURL, currentURL = baseURL, pages) {
    // if this is an offsite URL, bail immediately
    const currentUrlObj = new URL(currentURL)
    const baseUrlObj = new URL(baseURL)
    if (currentUrlObj.hostname !== baseUrlObj.hostname){
        return pages
    }
    const normalizedURL = normalizeURL(currentURL)

  // if we've already visited this page
  // just increase the count and don't repeat
  // the http request
  if (pages[normalizedURL] > 0){
    pages[normalizedURL]++
    return pages
  }

  // initialize this page in the map
  // since it doesn't exist yet
  pages[normalizedURL] = 1

  // fetch and parse the html of the currentURL
//   console.log(`crawling ${currentURL}`)
  let htmlBody = ''
  try {
    const resp = await fetch(currentURL)
    if (resp.status > 399){
    //   console.log(`Got HTTP error, status code: ${resp.status}`)
      return pages
    }
    const contentType = resp.headers.get('content-type')
    if (!contentType.includes('text/html')){
    //   console.log(`Got non-html response: ${contentType}`)
      return pages
    }
    htmlBody = await resp.text()
  } catch (err){
    console.log(err.message)
  }

  const nextURLs = getURLsFromHTML(htmlBody, baseURL)
  for (const nextURL of nextURLs){
    pages = await crawlPage(baseURL, nextURL, pages)
  }

  return pages
}

module.exports = {
    normalizeURL,
    getURLsFromHTML,
    crawlPage,
};
