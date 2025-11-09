import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Path to your feed.xml and _posts directory
FEED_PATH = 'feed.xml'
POSTS_DIR = '_posts'

# Ensure _posts directory exists
os.makedirs(POSTS_DIR, exist_ok=True)

def slugify(title):
    # Simple slugify for filenames
    slug = re.sub(r'[^a-zA-Z0-9\- ]', '', title)
    slug = slug.replace(' ', '-').lower()
    return slug

def main():
    tree = ET.parse(FEED_PATH)
    root = tree.getroot()
    ns = {'atom': 'http://www.w3.org/2005/Atom', 'blogger': 'http://schemas.google.com/blogger/2018'}

    for entry in root.findall('atom:entry', ns):
        # Only process entries with <blogger:type>POST</blogger:type>
        blogger_type = entry.find('blogger:type', ns)
        if blogger_type is None or blogger_type.text != 'POST':
            continue

        title_elem = entry.find('atom:title', ns)
        title = title_elem.text if title_elem is not None else 'untitled'
        published_elem = entry.find('atom:published', ns)
        published = published_elem.text if published_elem is not None else None
        content_elem = entry.find('atom:content', ns)
        content = content_elem.text if content_elem is not None else ''
        # Get blogger:filename for permalink
        filename_elem = entry.find('blogger:filename', ns)
        permalink = filename_elem.text if filename_elem is not None else None
        # Fallback: use slugified title
        if not permalink:
            permalink = '/' + slugify(title) + '/'
        # Format date for filename
        if published:
            date = datetime.strptime(published[:10], '%Y-%m-%d')
        else:
            date = datetime.now()
        slug = slugify(title)
        md_filename = f"{date.strftime('%Y-%m-%d')}-{slug}.md"
        md_path = os.path.join(POSTS_DIR, md_filename)
        # Extract tags
        tags = [cat.attrib['term'] for cat in entry.findall('atom:category', ns)
                if 'term' in cat.attrib and not cat.attrib['term'].startswith('http://schemas.google.com/blogger/')]
        # Extract first image URL from content for thumbnail
        thumbnail = None
        img_match = re.search(r'<img[^>]+src=["\']([^"\' >]+)', content, re.IGNORECASE)
        if img_match:
            thumbnail = img_match.group(1)

        # Extract first YouTube video ID from iframe embed and prefer as thumbnail
        yt_iframe = re.search(r'<iframe[^>]+src=["\']https?://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)', content)
        if yt_iframe:
            video_id = yt_iframe.group(1)
            thumbnail = f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg'

        # Get metaDescription for excerpt
        meta_desc_elem = entry.find('blogger:metaDescription', ns)
        excerpt = meta_desc_elem.text.strip() if meta_desc_elem is not None and meta_desc_elem.text else None

        # Write markdown file
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write(f"title: \"{title.replace('"', '\\"')}\"\n")
            f.write(f"date: {date.strftime('%Y-%m-%d %H:%M:%S %z')}\n")
            f.write(f"permalink: {permalink}\n")
            if thumbnail:
                f.write(f"thumbnail: {thumbnail}\n")
            if excerpt:
                f.write(f"excerpt: \"{excerpt.replace('"', '\\"')}\"\n")
            if tags:
                f.write('tags: [' + ', '.join(f'\"{t}\"' for t in tags) + ']\n')
            f.write('---\n\n')
            f.write(content)
    print(f"Done! Posts written to {POSTS_DIR}/")

if __name__ == '__main__':
    main()
