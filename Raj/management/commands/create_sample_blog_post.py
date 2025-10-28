#!/usr/bin/env python
"""
Management command to create a sample blog post with rich formatting
"""
from django.core.management.base import BaseCommand
from Raj.models import BlogPost

class Command(BaseCommand):
    help = 'Create a sample blog post with rich formatting examples'

    def handle(self, *args, **options):
        # Check if sample post already exists
        if BlogPost.objects.filter(slug='sample-rich-text-blog-post').exists():
            self.stdout.write("Sample blog post already exists!")
            return

        # Create sample blog post with rich content
        sample_content = """
<h1>Welcome to Our Real Estate Blog!</h1>

<p>This is a sample blog post demonstrating the rich text formatting capabilities of our new blog system.</p>

<h2>Key Features</h2>
<p>Our blog now supports:</p>
<ul>
    <li><strong>Custom text colors</strong> - Choose any color for your text</li>
    <li><strong>Font families</strong> - Select from various font options</li>
    <li><strong>Font sizes</strong> - Adjust text size to your preference</li>
    <li><strong>Line height</strong> - Control spacing between lines</li>
    <li><strong>Background colors</strong> - Add background colors to sections</li>
</ul>

<h2>Rich Text Formatting</h2>
<p>You can use various HTML tags to format your content:</p>

<h3>Text Formatting</h3>
<p>Make text <strong>bold</strong> or <em>italic</em> as needed.</p>

<h3>Lists</h3>
<p>Create ordered lists:</p>
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>

<h3>Tables</h3>
<p>Add tables for structured data:</p>
<table border="1" style="width: 100%; border-collapse: collapse;">
    <tr>
        <th style="padding: 8px; background-color: #f2f2f2;">Property Type</th>
        <th style="padding: 8px; background-color: #f2f2f2;">Average Price</th>
        <th style="padding: 8px; background-color: #f2f2f2;">Market Trend</th>
    </tr>
    <tr>
        <td style="padding: 8px;">Single Family</td>
        <td style="padding: 8px;">$450,000</td>
        <td style="padding: 8px;">↗️ Rising</td>
    </tr>
    <tr>
        <td style="padding: 8px;">Condos</td>
        <td style="padding: 8px;">$320,000</td>
        <td style="padding: 8px;">↗️ Rising</td>
    </tr>
    <tr>
        <td style="padding: 8px;">Townhouses</td>
        <td style="padding: 8px;">$380,000</td>
        <td style="padding: 8px;">→ Stable</td>
    </tr>
</table>

<h3>Images</h3>
<p>You can also include images in your blog posts:</p>
<img src="https://via.placeholder.com/400x200/4F46E5/FFFFFF?text=Sample+Image" alt="Sample image" style="max-width: 100%; height: auto; border-radius: 8px;">

<h3>Links</h3>
<p>Add links to external resources: <a href="https://www.example.com" target="_blank">Visit our website</a></p>

<hr>

<h2>Conclusion</h2>
<p>This rich text editor gives you complete control over your blog post formatting. You can create professional-looking content with tables, lists, images, and custom styling.</p>

<p><em>Happy blogging!</em></p>
        """

        blog_post = BlogPost.objects.create(
            title="Sample Rich Text Blog Post",
            slug="sample-rich-text-blog-post",
            author="Henry Oak Reality",
            content=sample_content.strip(),
            excerpt="A demonstration of our new rich text formatting capabilities with examples of tables, lists, images, and custom styling.",
            text_color="#2d3748",
            font_family="Georgia",
            font_size="18px",
            line_height="1.6",
            background_color="#f7fafc",
            featured=True,
            published=True
        )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created sample blog post: "{blog_post.title}"')
        )
        self.stdout.write(f'You can view it at: /blog/{blog_post.slug}/')
