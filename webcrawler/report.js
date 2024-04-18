async function printReport(pages){
    console.log("Report is starting...")
    const newPages = await Array.prototype.sort.call(pages)
    const sortedPages = Object.entries(newPages).sort((a, b) => b[1] - a[1])
    const objSortedPages = Object.fromEntries(sortedPages)
    for (let page in objSortedPages){
        console.log(`Found ${objSortedPages[page]} internal links to ${page}`)
    }

}
module.exports = {
    printReport
};