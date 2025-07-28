from pathlib import Path
from bs4 import BeautifulSoup
import pytest

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = list(ROOT.glob('*.html'))

@pytest.mark.parametrize('html_file', HTML_FILES)
def test_nav_links_exist(html_file):
    """Ensure all navigation links point to existing files."""
    soup = BeautifulSoup(html_file.read_text(encoding='utf-8'), 'html.parser')
    for nav in soup.find_all('nav'):
        for a in nav.find_all('a', href=True):
            href = a['href']
            if href.startswith(('http://', 'https://', 'mailto:')):
                continue
            target = href.split('#', 1)[0].split('?', 1)[0]
            if not target:
                continue
            assert (ROOT / target).exists(), f"{html_file.name}: broken link {href}"
