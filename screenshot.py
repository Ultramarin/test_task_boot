from logging import getLogger
from pathlib import Path
from typing import Union

from pyppeteer import launch

import settings

logger = getLogger()


def prepare_url(url: str) -> str:
    """Append http/https to urls without it."""
    return (
        url
        if url.startswith("http://") or url.startswith("https://")
        else f"http://{url}"
    )


async def capture_screenshot(
    url: str,
    viewport_width: int = settings.SCREENSHOT_WIDTH,
    viewport_height: int = settings.SCREENSHOT_HEIGHT,
) -> Union[bytes, str]:
    browser = await launch(handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
    page = await browser.newPage()
    await page.setViewport({"width": viewport_width, "height": viewport_height})
    await page.goto(url)
    screenshot = await page.screenshot()
    await browser.close()

    return screenshot
