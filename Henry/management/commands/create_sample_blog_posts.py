from django.core.management.base import BaseCommand
from Henry.models import BlogPost


class Command(BaseCommand):
    help = 'Create sample blog posts for testing'

    def handle(self, *args, **options):
        # Sample blog posts data
        sample_posts = [
            {
                'title': 'Exploring Real Estate Investment Opportunities',
                'author': 'John Doe',
                'excerpt': 'Discover the latest insights into the real estate investment market and tips for maximizing returns.',
                'content': '''
                <h3>Understanding Real Estate Investment</h3>
                <p>Real estate investment has long been considered one of the most stable and profitable investment strategies. Whether you're a seasoned investor or just starting out, understanding the fundamentals is crucial for success.</p>
                
                <h4>Types of Real Estate Investments</h4>
                <ul>
                    <li><strong>Residential Properties:</strong> Single-family homes, condos, and townhouses</li>
                    <li><strong>Commercial Properties:</strong> Office buildings, retail spaces, and warehouses</li>
                    <li><strong>Industrial Properties:</strong> Manufacturing facilities and distribution centers</li>
                    <li><strong>Mixed-Use Properties:</strong> Combinations of residential and commercial spaces</li>
                </ul>
                
                <h4>Key Investment Strategies</h4>
                <p>There are several approaches to real estate investment, each with its own benefits and considerations:</p>
                
                <h5>1. Buy and Hold</h5>
                <p>This strategy involves purchasing properties and holding them for long-term appreciation and rental income. It's ideal for investors seeking steady cash flow and long-term wealth building.</p>
                
                <h5>2. Fix and Flip</h5>
                <p>This approach involves purchasing properties that need renovation, improving them, and selling for a profit. It requires more active involvement but can yield higher returns in shorter timeframes.</p>
                
                <h5>3. Real Estate Investment Trusts (REITs)</h5>
                <p>REITs allow investors to participate in real estate markets without directly owning properties. They offer liquidity and diversification benefits.</p>
                
                <h4>Market Analysis and Due Diligence</h4>
                <p>Before making any investment, thorough market research is essential. Consider factors such as:</p>
                <ul>
                    <li>Local market trends and growth patterns</li>
                    <li>Property values and rental rates</li>
                    <li>Economic indicators and job market stability</li>
                    <li>Infrastructure development and future plans</li>
                </ul>
                
                <h4>Risk Management</h4>
                <p>Like any investment, real estate carries risks. Diversification, proper insurance, and maintaining adequate cash reserves are crucial for managing these risks effectively.</p>
                
                <p>Remember, successful real estate investment requires patience, research, and a long-term perspective. Start small, learn continuously, and consider working with experienced professionals to guide your investment decisions.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'featured': True,
                'published': True
            },
            {
                'title': 'First-Time Homebuyer Guide: Everything You Need to Know',
                'author': 'Sarah Johnson',
                'excerpt': 'A comprehensive guide for first-time homebuyers covering everything from pre-approval to closing.',
                'content': '''
                <h3>Your Journey to Homeownership</h3>
                <p>Buying your first home is one of life's most significant milestones. This comprehensive guide will walk you through every step of the process, from initial planning to closing day.</p>
                
                <h4>Step 1: Assess Your Financial Readiness</h4>
                <p>Before you start house hunting, it's crucial to understand your financial situation:</p>
                <ul>
                    <li><strong>Credit Score:</strong> Aim for a score of 620 or higher for conventional loans</li>
                    <li><strong>Down Payment:</strong> Save 20% if possible, but some programs allow as little as 3%</li>
                    <li><strong>Emergency Fund:</strong> Maintain 3-6 months of expenses in savings</li>
                    <li><strong>Debt-to-Income Ratio:</strong> Keep total monthly debt payments under 43% of income</li>
                </ul>
                
                <h4>Step 2: Get Pre-Approved for a Mortgage</h4>
                <p>Pre-approval gives you a clear picture of your budget and shows sellers you're a serious buyer. Gather these documents:</p>
                <ul>
                    <li>Recent pay stubs and tax returns</li>
                    <li>Bank statements and investment account statements</li>
                    <li>Employment verification letter</li>
                    <li>List of current debts and monthly payments</li>
                </ul>
                
                <h4>Step 3: Find the Right Real Estate Agent</h4>
                <p>A good agent will be your advocate throughout the process. Look for someone who:</p>
                <ul>
                    <li>Has experience in your target area</li>
                    <li>Understands your needs and budget</li>
                    <li>Communicates clearly and promptly</li>
                    <li>Has positive reviews from past clients</li>
                </ul>
                
                <h4>Step 4: House Hunting</h4>
                <p>Create a list of must-haves and nice-to-haves. Consider factors like:</p>
                <ul>
                    <li>Location and neighborhood amenities</li>
                    <li>School district quality</li>
                    <li>Commute times to work</li>
                    <li>Future resale potential</li>
                    <li>Property condition and maintenance needs</li>
                </ul>
                
                <h4>Step 5: Making an Offer</h4>
                <p>Your agent will help you craft a competitive offer based on:</p>
                <ul>
                    <li>Recent comparable sales in the area</li>
                    <li>Market conditions and competition</li>
                    <li>Property condition and inspection results</li>
                    <li>Your budget and timeline</li>
                </ul>
                
                <h4>Step 6: Home Inspection and Appraisal</h4>
                <p>These steps protect your investment:</p>
                <ul>
                    <li><strong>Home Inspection:</strong> Identifies potential issues and maintenance needs</li>
                    <li><strong>Appraisal:</strong> Ensures the property value matches the purchase price</li>
                </ul>
                
                <h4>Step 7: Closing Process</h4>
                <p>During the final weeks before closing:</p>
                <ul>
                    <li>Review all loan documents carefully</li>
                    <li>Conduct a final walkthrough of the property</li>
                    <li>Prepare for closing costs (typically 2-5% of purchase price)</li>
                    <li>Bring required identification and certified funds</li>
                </ul>
                
                <h4>Common First-Time Buyer Mistakes to Avoid</h4>
                <ul>
                    <li>Not getting pre-approved before house hunting</li>
                    <li>Focusing only on the purchase price (ignoring other costs)</li>
                    <li>Making emotional decisions without considering resale value</li>
                    <li>Skipping the home inspection to save money</li>
                    <li>Not shopping around for the best mortgage rates</li>
                </ul>
                
                <p>Remember, buying a home is a significant financial commitment. Take your time, ask questions, and don't hesitate to seek professional advice throughout the process.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=300&fit=crop',
                'featured': False,
                'published': True
            },
            {
                'title': 'Market Trends: What to Expect in 2024',
                'author': 'Michael Chen',
                'excerpt': 'An in-depth analysis of real estate market trends and predictions for the coming year.',
                'content': '''
                <h3>2024 Real Estate Market Outlook</h3>
                <p>As we look ahead to 2024, several key trends are shaping the real estate landscape. Understanding these trends can help both buyers and sellers make informed decisions in the coming year.</p>
                
                <h4>Interest Rate Environment</h4>
                <p>Interest rates have been a major factor in the 2023 market, and their trajectory will continue to influence 2024:</p>
                <ul>
                    <li>Federal Reserve policy remains data-dependent</li>
                    <li>Inflation trends will drive rate decisions</li>
                    <li>Buyers should prepare for potential rate volatility</li>
                    <li>Refinancing opportunities may emerge</li>
                </ul>
                
                <h4>Inventory and Supply</h4>
                <p>Housing supply continues to be a challenge in many markets:</p>
                <ul>
                    <li>New construction is increasing but slowly</li>
                    <li>Existing homeowners are staying put longer</li>
                    <li>Rental markets remain competitive</li>
                    <li>Affordable housing initiatives are expanding</li>
                </ul>
                
                <h4>Technology and Innovation</h4>
                <p>Technology continues to transform the real estate industry:</p>
                <ul>
                    <li>Virtual and augmented reality tours</li>
                    <li>AI-powered property valuations</li>
                    <li>Blockchain in property transactions</li>
                    <li>Smart home technology integration</li>
                </ul>
                
                <h4>Demographic Shifts</h4>
                <p>Changing demographics are influencing market dynamics:</p>
                <ul>
                    <li>Millennials entering prime homebuying years</li>
                    <li>Baby boomers downsizing and relocating</li>
                    <li>Remote work continuing to impact location preferences</li>
                    <li>Multigenerational living arrangements increasing</li>
                </ul>
                
                <h4>Regional Variations</h4>
                <p>Market conditions vary significantly by region:</p>
                <ul>
                    <li><strong>Urban Markets:</strong> Recovery in downtown areas</li>
                    <li><strong>Suburban Markets:</strong> Continued strong demand</li>
                    <li><strong>Rural Markets:</strong> Growing interest from remote workers</li>
                    <li><strong>Coastal Markets:</strong> Climate considerations affecting values</li>
                </ul>
                
                <h4>Investment Opportunities</h4>
                <p>For investors, 2024 presents both challenges and opportunities:</p>
                <ul>
                    <li>Multifamily properties in growing markets</li>
                    <li>Single-family rental properties</li>
                    <li>Commercial real estate in emerging areas</li>
                    <li>Real estate investment trusts (REITs)</li>
                </ul>
                
                <h4>What This Means for You</h4>
                <p>Whether you're buying, selling, or investing:</p>
                <ul>
                    <li><strong>Buyers:</strong> Be prepared for competitive markets, consider pre-approval</li>
                    <li><strong>Sellers:</strong> Price strategically, prepare for longer market times</li>
                    <li><strong>Investors:</strong> Focus on cash flow and long-term appreciation</li>
                    <li><strong>Everyone:</strong> Stay informed and work with experienced professionals</li>
                </ul>
                
                <p>The 2024 market will likely present both challenges and opportunities. Success will depend on staying informed, being flexible, and making decisions based on your individual circumstances and long-term goals.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'featured': True,
                'published': True
            }
        ]

        # Create blog posts
        created_count = 0
        for post_data in sample_posts:
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults=post_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created blog post: {post.title}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Blog post already exists: {post.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} new blog posts')
        )

