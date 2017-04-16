"""Class to handle tinyMCE4 widgets"""
from django import forms


class TinyMCE4Widget(forms.Textarea):
    class Media:
        css = {
            'all': ('tinymce/css/style.css',)
        }
        js = (
            # 'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
            'tinymce/tinymce.min.js',
            'tinymce/tinymce.config.js',
        )
