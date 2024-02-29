# from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views import View
from .models import Content, Video, Image, InternalLink, ExternalLink
from bs4 import BeautifulSoup
import os

class ParseAndSaveView(View):
    def get(self, request):
        root_directory = 'files/fa/articles'
        # total_data = []
        counter = 0
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
                        # main_content_h2 = main_content.find_all('h2')

                        html_content = ""
                        if main_content:
                            for tag in main_content.find_all():
                                if tag.name == 'h2':
                                    if "جستارهای وابسته" or "پانویس" or "منابع" or "پیوند به بیرون" in tag.get_text(strip=True):
                                        break
                                else:
                                    html_content += str(tag)
                                    
                        print('='*30)
                        print(html_content)
                        print('='*30)
                                   
                        videos = [{"url":vid.get('resource')} for vid in soup.find_all('video')]
                        images = [{"url":img.get('src'),"alt":img.get('alt')} for img in soup.find_all('img')]
                        links = [{"url":link.get('href'),"anchor_text":link.text} for link in soup.find_all('a')]
                        tags = [tag for tag in soup.find_all('b')]

                        # Save data to the database
                        #Content
                        content = Content(title=head_title.text if head_title else "",
                                          description=desc[0] if desc else "",
                                          main_content=html_content)
                        content.save()

                        # print('='*30)
                        # print(content.content_id)
                        # print('='*30)

                        content_instance = Content.objects.get(content_id= content.content_id)

                        # Videos
                        if videos:
                            for video in videos:
                                Video.objects.create(url=video['url'],content_id=content_instance)
                        else:
                            continue        

                        # Images
                        # print('='*30)
                        # print(content_instance.content_id)
                        # print('='*30)
                        if images:
                            for img in images:
                                Image.objects.create(url=img['url'],alt=img['alt'],content_id=content_instance)
                                # image = Image(url=img['url'],alt=img['alt'],content_id=content_instance)
                                # image.save()
                        else:
                            continue
                        




        return HttpResponse("Data parsed and saved successfully.")

# page = wikipedia.page("tiger")

# ref = page.content
# print('='*30)
# print(ref)
# print('='*30)