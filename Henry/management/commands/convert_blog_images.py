from django.core.management.base import BaseCommand
from Henry.models import BlogPost
from Henry.image_utils import image_to_base64

class Command(BaseCommand):
    help = 'Convert existing blog post images to base64'

    def handle(self, *args, **options):
        blog_posts = BlogPost.objects.all()
        converted_count = 0
        
        for post in blog_posts:
            if post.image_file and post.image_file.name and not post.image_base64:
                try:
                    self.stdout.write(f"Converting image for blog post: {post.title}")
                    post.image_base64 = image_to_base64(post.image_file)
                    post.save()
                    converted_count += 1
                    self.stdout.write(self.style.SUCCESS(f"✓ Converted image for: {post.title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"✗ Error converting image for {post.title}: {e}"))
            else:
                self.stdout.write(f"- Skipping {post.title} (no image file or already converted)")
        
        self.stdout.write(self.style.SUCCESS(f"\nConversion complete! Converted {converted_count} blog post images to base64."))
