from django.shortcuts import render

from bs4 import BeautifulSoup

def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as html_file:
        soup = BeautifulSoup(html_file.read(), 'html.parser')
    return soup