const { test, expect } = require('@jest/globals')
const { normalizeURL, getURLfromHTML } = require('./crawl.js')

test('normalizeURL strip protocol https', () => {
    const input = "https://blog.boot.dev/path/"
    const actual = normalizeURL(input)
    const expected = "blog.boot.dev/path"
    expect(actual).toEqual(expected)
})
test('normalizeURL strip protocol http', () => {
    const input = "http://blog.boot.dev/path/"
    const actual = normalizeURL(input)
    const expected = "blog.boot.dev/path"
    expect(actual).toEqual(expected)
})

test('normalizeURL strip trailing slash', () => {
    const input = "https://blog.boot.dev/path/"
    const actual = normalizeURL(input)
    const expected = "blog.boot.dev/path"
    expect(actual).toEqual(expected)
})

test('normalizeURL strip trailing slash', () => {
    const input = "https://blog.boot.dev/path/"
    const actual = normalizeURL(input)
    const expected = "blog.boot.dev/path"
    expect(actual).toEqual(expected)
})

test('getURLfromHTML', () => {
    const input = "<a href='https://boot.dev'>Learn Backend Development</a><a href='https://boot.com'>Learn Backend Development</a><a href='https://boot.org'>Learn Backend Development</a>"
    const actual = getURLfromHTML(input)
    const expected = ["boot.dev", "boot.com", "boot.org"]
    expect(actual).toEqual(expected)
})