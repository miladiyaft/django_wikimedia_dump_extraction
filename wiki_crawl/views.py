from django.http import HttpResponse
from django.views import View
from django.views import View
from .models import Content, Video, Image, InternalLink, ExternalLink, Tag
from bs4 import BeautifulSoup
import os

class ParseAndSaveView(View):
    def get(self, request):
        root_directory = 'files/fa/articles'
        for root, dirs, files in os.walk(root_directory):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as html_file:
                        # Parse the HTML content
                        soup = BeautifulSoup(html_file.read(), 'html.parser')
                        # Extract the data from the HTML
                        head_title = soup.find('title')
                        desc = [desc.text for desc in soup.find_all('meta', {'name': 'description'})]
                        main_content = soup.find('div',{'id':'bodyContent'})

                        html_content = ""
                        if main_content:
                            for tag in main_content.find_all():
                                if tag.name == 'h2':
                                    if "جستارهای وابسته" or "پانویس" or "منابع" or "پیوند به بیرون" in tag.get_text(strip=True):
                                        break
                                else:
                                    html_content += str(tag)
                                    
                                   
                        videos = [{"url":vid.get('resource')} for vid in soup.find_all('video')]
                        images = [{"url":img.get('src'),"alt":img.get('alt')} for img in soup.find_all('img')]
                        links = [{"url":link.get('href'),"anchor_text":link.text} for link in soup.find_all('a')]
                        cat_links = soup.find('div',{'id':'catlinks'})
                        

                        # Save data to the database
                        #Content
                        content = Content(title=head_title.text if head_title else "",
                                          description=desc[0] if desc else "",
                                          main_content=html_content)
                        content.save()

                        content_instance = Content.objects.get(content_id=content.content_id)

                        # Videos
                        if videos:
                            for video in videos:
                                Video.objects.create(url=video['url'],content_id=content_instance)
                        else:
                            pass        

                        # Images
                        if images:
                            for img in images:
                                # Or Image.objects.create(url=img['url'],alt=img['alt'],content_id=content_instance)
                                image = Image(url=img['url'],alt=img['alt'],content_id=content_instance)
                                image.save()
                        else:
                            pass

                        # External links or Internal links
                        if links:  
                            for link in links:
                                if link['url'] and link['url'].startswith("/wiki/"): 
                                    InternalLink.objects.create(url=link['url'], anchor_text=link['anchor_text'], type="internal", content_id = content_instance)
                                elif link['url']:
                                    ExternalLink.objects.create(url=link['url'], anchor_text=link['anchor_text'], type="external", content_id = content_instance)
                                else:
                                    continue    
                        else:
                            pass

                        # Tags
                        if cat_links:
                            cat_links_ul = cat_links.find('ul')
                            if cat_links_ul:
                                tags = [{'text':tag.text}for tag in cat_links_ul.find_all('li')]
                                for tag in tags:
                                    Tag.objects.create(tag_text=tag['text'], content_id = content_instance)
                        




        return HttpResponse("Data parsed and saved successfully.")

