# from cProfile import label
from turtle import heading
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    """HomePage model"""

    template = 'home/home_page.html'

    subpage_types = ['home.ContentPage']


class PoemPage(Page):
    """PoemPage Model"""

    page_description = "Use this page for posting new poems"

    template = 'home/poem_page.html'

    body = RichTextField(blank=True)
    intro = models.TextField(max_length=255)
    bg = models.ForeignKey('wagtailimages.Image', related_name='+', blank=True, null=True, on_delete=models.SET_NULL)
    tc = models.CharField(max_length=15, default = 'white')

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('tc', heading="Title Colour"),
                FieldPanel('intro', heading="Introductory Note")
            ], heading="Basic Info"
        ),
        FieldPanel('body'),
        FieldPanel('bg', heading="Background Image")
    ]

    parent_page_types = ['home.ContentPage']
    subpage_types = []

class ContentPage(Page):
    """ContentPage Model"""

    template = 'home/content_page.html'

    parent_page_type = ['home.HomePage']
    subpage_types = ['home.PoemPage']