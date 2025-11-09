#!/usr/bin/env python3
"""
Script to replace YouTube iframe embeds with Jekyll video-embed include syntax
"""

import os
import re
import glob

def extract_video_id(iframe_html):
    """Extract YouTube video ID from various iframe formats"""
    patterns = [
        r'youtube\.com/embed/([a-zA-Z0-9_-]+)',
        r'youtube\.com/v/([a-zA-Z0-9_-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, iframe_html)
        if match:
            # Remove any query parameters
            video_id = match.group(1).split('?')[0].split('&')[0]
            return video_id
    return None

def extract_title_from_file(filepath):
    """Extract title from the post front matter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for title in front matter
            title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
            if title_match:
                return title_match.group(1)
            # Fallback: use filename
            basename = os.path.basename(filepath)
            title = basename.replace('.md', '').replace('-', ' ').title()
            return title
    except:
        return "Video"

def replace_iframes_in_file(filepath):
    """Replace YouTube iframes in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        post_title = extract_title_from_file(filepath)
        replacements_made = 0
        
        # Pattern to match YouTube iframes with various formats
        iframe_pattern = r'<(?:p[^>]*>)?<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)[^"]*"[^>]*>(?:</iframe>)?</p>?'
        
        def replace_iframe(match):
            nonlocal replacements_made
            full_match = match.group(0)
            video_id = match.group(1)
            
            if not video_id:
                return full_match
            
            # Clean up video_id from query parameters
            video_id = video_id.split('?')[0].split('&')[0]
            
            replacements_made += 1
            # Return the Jekyll include syntax
            return f'{{% include video-embed.html video_id="{video_id}" title="{post_title}" %}}'
        
        # Replace all iframes
        content = re.sub(iframe_pattern, replace_iframe, content)
        
        # Also handle simpler iframe patterns without <p> tags
        simple_iframe_pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)[^"]*"[^>]*></iframe>'
        content = re.sub(simple_iframe_pattern, replace_iframe, content)
        
        if replacements_made > 0 and content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filepath}: Replaced {replacements_made} embed(s)")
            return replacements_made
        else:
            return 0
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return 0

def main():
    """Main function to process all markdown files in _posts"""
    posts_dir = '/home/tom/Public/lorenzosmusic.github.io/_posts'
    
    if not os.path.exists(posts_dir):
        print(f"Error: Directory {posts_dir} not found")
        return
    
    # Find all markdown files
    md_files = glob.glob(os.path.join(posts_dir, '*.md'))
    
    print(f"Found {len(md_files)} markdown files to process\n")
    
    total_replacements = 0
    files_modified = 0
    
    for filepath in sorted(md_files):
        replacements = replace_iframes_in_file(filepath)
        if replacements > 0:
            files_modified += 1
            total_replacements += replacements
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"Files modified: {files_modified}")
    print(f"Total replacements made: {total_replacements}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
