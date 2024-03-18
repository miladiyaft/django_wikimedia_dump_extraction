from django.shortcuts import render

from wiki_crawl.models import Content, Video, Image, InternalLink, ExternalLink, Tag

def save_content(soup, content_instance):
    # Extract data from soup and save to database
    # This is a simplified example, you'll need to adapt it to your specific needs
    content = Content(title=soup.find('title').text if soup.find('title') else "",
                      description=soup.find('meta', {'name': 'description'}).text if soup.find('meta', {'name': 'description'}) else "",
                      main_content="") # You'll need to implement the logic to extract main_content
    content.save()
    return content

def save_videos(soup, content_instance):
    videos = [{"url": vid.get('resource')} for vid in soup.find_all('video')]
    for video in videos:
        Video.objects.create(url=video['url'], content_id=content_instance)

def save_images(soup, content_instance):
    images = [{"url": img.get('src'), "alt": img.get('alt')} for img in soup.find_all('img')]
    for img in images:
        Image.objects.create(url=img['url'], alt=img['alt'], content_id=content_instance)

def save_links(soup, content_instance):
    links = [{"url": link.get('href'), "anchor_text": link.text} for link in soup.find_all('a')]
    for link in links:
        if link['url'] and link['url'].startswith("/wiki/"):
            InternalLink.objects.create(url=link['url'], anchor_text=link['anchor_text'], type="internal", content_id=content_instance)
        elif link['url']:
            ExternalLink.objects.create(url=link['url'], anchor_text=link['anchor_text'], type="external", content_id=content_instance)

def save_tags(soup, content_instance):
    cat_links = soup.find('div', {'id': 'catlinks'})
    if cat_links:
        tags = [{'text': tag.text} for tag in cat_links.find_all('li')]
        for tag in tags:
            Tag.objects.create(tag_text=tag['text'], content_id=content_instance)

