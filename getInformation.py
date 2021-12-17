import asyncio
from pyppeteer import launch

async def main(text):
        # Create a browser instance and goto "google.com"  
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://en.wikipedia.org/wiki')

        # Type in search keyword and press enter
    await page.type('[id=searchInput]', text)

        # Take a screenshot and export it to a png file: "test.png"
    await page.screenshot({'path': 'test.png'})

        # Press enter and Wait for results to load
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    await page.screenshot({'path': 'results.png'})

        # Close browser 
    await browser.close()


asyncio.get_event_loop().run_until_complete(main('family'))
