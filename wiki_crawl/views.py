# views.py
from django.http import HttpResponse
from django.views import View
import os
from parse_html.views import parse_html
from save_data.views import save_content, save_videos, save_images, save_links, save_tags

class ParseAndSaveView(View):
    def get(self, request):
        root_directory = 'files/fa/articles'
        try:
            for root, dirs, files in os.walk(root_directory):
                for file in files:
                    if file.endswith('.html'):
                        file_path = os.path.join(root, file)
                        soup = parse_html(file_path)
                        # Define content_instance as None before using it
                        content_instance = None
                        # Save content and retrieve the saved instance
                        content_instance = save_content(soup, content_instance)
                        save_videos(soup, content_instance)
                        save_images(soup, content_instance)
                        save_links(soup, content_instance)
                        save_tags(soup, content_instance)
        except Exception as e:
            print(f"An error occurred: {e}")
            return HttpResponse(f"An error occurred while parsing and saving data. Error is: {e}", status=500)

        return HttpResponse("Data parsed and saved successfully.")
