/** Adapt `baseURL`, actual routes and selectors before running. */
import { test, expect } from '@playwright/test';

const viewports = [
  { width: 360, height: 780 },
  { width: 390, height: 844 },
  { width: 768, height: 1024 },
  { width: 1280, height: 800 },
];

test.describe('UI smoke + responsive', () => {
  for (const viewport of viewports) {
    test(`homepage ${viewport.width}x${viewport.height}`, async ({ page }) => {
      await page.setViewportSize(viewport);
      const errors: string[] = [];
      page.on('pageerror', error => errors.push(error.message));
      await page.goto('/', { waitUntil: 'domcontentloaded' });
      await expect(page.locator('main')).toBeVisible();
      const overflow = await page.evaluate(() =>
        document.documentElement.scrollWidth > window.innerWidth + 1
      );
      expect(overflow, 'Unexpected horizontal overflow').toBeFalsy();
      expect(errors, 'Browser page errors').toEqual([]);
      await page.screenshot({ path: `test-results/home-${viewport.width}.png`, fullPage: true });
    });
  }

  test('reduced motion keeps the content accessible', async ({ page }) => {
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto('/');
    await expect(page.locator('main')).toBeVisible();
  });
});
