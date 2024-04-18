const { crawlPage } = require('./crawl.js')
const { printReport } = require('./report.js')
const { argv, exit } = require('node:process');


function main(){

    let BASE_URL = ""
    if (argv.length != 3){
        console.log("ERROR not enough arguments")
        exit()
    } else {
        BASE_URL = argv[2]
        console.log("Starting at:", BASE_URL)
    }
        const pages = crawlPage(BASE_URL, BASE_URL, {})
        printReport(pages)

    }
    

    main()
