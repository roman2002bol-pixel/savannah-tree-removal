"""Build the production-domain sitemap from canonical URLs in public HTML."""
from pathlib import Path
import re
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
SITE = 'https://www.savannahtreeremovalco.com'

def build():
    urls = []
    for path in sorted(ROOT.rglob('*.html')):
        if any(part.startswith('.') for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding='utf-8')
        match = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', text)
        if not match or not match.group(1).startswith(SITE + '/'):
            raise ValueError(f'Unexpected or missing canonical: {path}')
        urls.append(match.group(1))
    if len(urls) != len(set(urls)):
        raise ValueError('Duplicate canonical URLs')
    body = '\n'.join('  <url><loc>'+escape(url)+'</loc></url>' for url in urls)
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+body+'\n</urlset>\n', encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+SITE+'/sitemap.xml\n', encoding='utf-8')
    print(f'Sitemap: {len(urls)} canonical URLs. Configure the production domain before submission.')

if __name__ == '__main__':
    build()
