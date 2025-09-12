from django.core.management.base import BaseCommand
from Henry.models import BlogPost


class Command(BaseCommand):
    help = 'Populate the database with sample blog posts'

    def handle(self, *args, **options):
        # Sample blog posts
        blog_posts = [
            {
                'title': 'Real Estate Investment: A Complete Guide for Beginners',
                'author': 'Henry Oak Reality Team',
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
                    <li>Bank statements</li>
                    <li>Employment verification</li>
                    <li>Credit report</li>
                </ul>
                
                <h4>Step 3: Find the Right Real Estate Agent</h4>
                <p>A good agent will guide you through the process, negotiate on your behalf, and help you avoid common pitfalls. Look for someone with:</p>
                <ul>
                    <li>Local market expertise</li>
                    <li>Strong communication skills</li>
                    <li>Positive client reviews</li>
                    <li>Experience with first-time buyers</li>
                </ul>
                
                <h4>Step 4: Start House Hunting</h4>
                <p>Create a list of must-haves and nice-to-haves. Consider factors like:</p>
                <ul>
                    <li>Location and commute</li>
                    <li>School districts</li>
                    <li>Property condition</li>
                    <li>Future resale value</li>
                </ul>
                
                <h4>Step 5: Make an Offer and Negotiate</h4>
                <p>Your agent will help you craft a competitive offer based on market conditions and comparable sales. Be prepared to negotiate on price, closing date, and contingencies.</p>
                
                <h4>Step 6: Home Inspection and Appraisal</h4>
                <p>These steps protect your investment by identifying potential issues and ensuring the property's value matches the purchase price.</p>
                
                <h4>Step 7: Final Walkthrough and Closing</h4>
                <p>Before closing, do a final walkthrough to ensure the property is in the agreed-upon condition. At closing, you'll sign the final documents and receive the keys to your new home.</p>
                
                <p>Remember, buying a home is a process that typically takes 30-45 days. Stay patient, ask questions, and lean on your real estate professional for guidance throughout the journey.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=300&fit=crop',
                'featured': False,
                'published': True
            },
            {
                'title': 'Market Trends: What to Expect in 2024',
                'author': 'Michael Chen',
                'excerpt': 'An analysis of current real estate market trends and predictions for the coming year.',
                'content': '''
                <h3>2024 Real Estate Market Outlook</h3>
                <p>As we move through 2024, the real estate market continues to evolve with new trends and opportunities. Here's what buyers, sellers, and investors should know.</p>
                
                <h4>Interest Rate Environment</h4>
                <p>Interest rates have stabilized after the volatility of recent years. While rates remain higher than the historic lows of 2020-2021, they're expected to remain relatively stable throughout 2024, providing more predictability for buyers.</p>
                
                <h4>Inventory Levels</h4>
                <p>Housing inventory remains tight in most markets, though we're seeing gradual improvements in some areas. This continued shortage is supporting home prices even as demand moderates.</p>
                
                <h4>Technology Integration</h4>
                <p>Virtual tours, AI-powered property matching, and digital transaction management are becoming standard. These technologies are making the buying and selling process more efficient and accessible.</p>
                
                <h4>Sustainability Focus</h4>
                <p>Energy-efficient homes and sustainable building practices are increasingly important to buyers. Properties with green features often command premium prices and sell faster.</p>
                
                <h4>Suburban vs. Urban Trends</h4>
                <p>The work-from-home trend continues to influence location preferences, with many buyers prioritizing space and amenities over proximity to city centers.</p>
                
                <h4>Investment Opportunities</h4>
                <p>Rental markets remain strong, making investment properties attractive. However, investors should carefully analyze cash flow and market fundamentals before purchasing.</p>
                
                <h4>What This Means for You</h4>
                <p><strong>For Buyers:</strong> Be prepared to move quickly when you find the right property. Get pre-approved and work with an experienced agent who understands local market conditions.</p>
                
                <p><strong>For Sellers:</strong> Price your home competitively and ensure it's in excellent condition. Consider minor updates that can increase appeal without major investment.</p>
                
                <p><strong>For Investors:</strong> Focus on markets with strong fundamentals, including job growth, population growth, and rental demand.</p>
                
                <p>As always, local market conditions vary significantly. Work with a knowledgeable real estate professional who can provide insights specific to your area and situation.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'featured': False,
                'published': True
            },
            {
                'title': 'Selling Your Home: 10 Tips for Maximum Value',
                'author': 'Jennifer Martinez',
                'excerpt': 'Expert advice on preparing your home for sale and maximizing its market value.',
                'content': '''
                <h3>Maximize Your Home's Value</h3>
                <p>Selling your home is one of the most significant financial transactions you'll make. Here are proven strategies to help you get the best possible price and terms.</p>
                
                <h4>1. Price It Right from the Start</h4>
                <p>Overpricing can lead to extended time on market and lower final sale prices. Work with your agent to analyze comparable sales and market conditions to set a competitive price.</p>
                
                <h4>2. Enhance Curb Appeal</h4>
                <p>First impressions matter. Simple improvements like fresh paint, landscaping, and clean walkways can significantly impact buyer interest.</p>
                
                <h4>3. Declutter and Depersonalize</h4>
                <p>Remove personal items and excess furniture to help buyers envision themselves in the space. Consider professional staging for maximum impact.</p>
                
                <h4>4. Make Necessary Repairs</h4>
                <p>Address obvious issues before listing. Small repairs can prevent larger problems during negotiations and inspections.</p>
                
                <h4>5. Deep Clean Everything</h4>
                <p>A spotless home suggests it's been well-maintained. Consider professional cleaning services for the best results.</p>
                
                <h4>6. Maximize Natural Light</h4>
                <p>Open curtains, clean windows, and ensure all light fixtures are working. Bright, airy spaces are more appealing to buyers.</p>
                
                <h4>7. Stage Key Rooms</h4>
                <p>Focus on the kitchen, living room, and master bedroom. These areas have the most impact on buyer decisions.</p>
                
                <h4>8. Professional Photography</h4>
                <p>High-quality photos are essential for online listings. Most buyers start their search online, so great photos drive showings.</p>
                
                <h4>9. Be Flexible with Showings</h4>
                <p>Make your home available for showings, even if it's inconvenient. The more accessible your home is, the more potential buyers will see it.</p>
                
                <h4>10. Work with an Experienced Agent</h4>
                <p>A skilled real estate professional will guide you through the process, handle negotiations, and help you avoid common pitfalls.</p>
                
                <h4>Additional Considerations</h4>
                <p><strong>Market Timing:</strong> While you can't control market conditions, understanding seasonal trends in your area can help with timing decisions.</p>
                
                <p><strong>Marketing Strategy:</strong> Ensure your agent has a comprehensive marketing plan that includes online listings, social media, and traditional marketing methods.</p>
                
                <p><strong>Negotiation Preparation:</strong> Be prepared for negotiations on price, closing date, and other terms. Know your bottom line and be ready to compromise.</p>
                
                <p>Remember, every home and market is unique. Work closely with your real estate professional to develop a customized strategy that works for your specific situation.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'featured': False,
                'published': True
            },
            {
                'title': 'Understanding Property Taxes: A Homeowner\'s Guide',
                'author': 'David Thompson',
                'excerpt': 'Everything you need to know about property taxes, assessments, and how to potentially reduce your tax burden.',
                'content': '''
                <h3>Property Tax Fundamentals</h3>
                <p>Property taxes are a significant ongoing expense for homeowners. Understanding how they work can help you budget effectively and potentially reduce your tax burden.</p>
                
                <h4>How Property Taxes Are Calculated</h4>
                <p>Property taxes are typically calculated using this formula:</p>
                <p><strong>Assessed Value × Tax Rate = Annual Property Tax</strong></p>
                
                <p>The assessed value is determined by your local tax assessor, while the tax rate is set by local governments to fund services like schools, roads, and emergency services.</p>
                
                <h4>Assessment Process</h4>
                <p>Assessors evaluate properties based on:</p>
                <ul>
                    <li>Recent sales of similar properties</li>
                    <li>Property size and features</li>
                    <li>Location and neighborhood</li>
                    <li>Property condition</li>
                </ul>
                
                <h4>Understanding Your Assessment</h4>
                <p>Review your property assessment carefully. Look for:</p>
                <ul>
                    <li>Incorrect square footage</li>
                    <li>Wrong number of bedrooms/bathrooms</li>
                    <li>Inaccurate property features</li>
                    <li>Comparison to similar properties</li>
                </ul>
                
                <h4>Appealing Your Assessment</h4>
                <p>If you believe your assessment is too high, you can typically appeal. The process usually involves:</p>
                <ol>
                    <li>Filing an appeal within the deadline</li>
                    <li>Gathering evidence (comparable sales, photos, etc.)</li>
                    <li>Presenting your case to the appeals board</li>
                    <li>Receiving a decision</li>
                </ol>
                
                <h4>Tax Exemptions and Reductions</h4>
                <p>Many jurisdictions offer exemptions for:</p>
                <ul>
                    <li>Senior citizens</li>
                    <li>Veterans</li>
                    <li>Disabled homeowners</li>
                    <li>Homestead exemptions</li>
                </ul>
                
                <h4>Planning for Property Taxes</h4>
                <p>When budgeting for homeownership, consider:</p>
                <ul>
                    <li>Annual tax increases</li>
                    <li>Escrow account requirements</li>
                    <li>Payment due dates</li>
                    <li>Penalties for late payment</li>
                </ul>
                
                <h4>Tax Benefits of Homeownership</h4>
                <p>While you pay property taxes, homeownership also offers tax benefits:</p>
                <ul>
                    <li>Mortgage interest deduction</li>
                    <li>Property tax deduction</li>
                    <li>Capital gains exclusion (for primary residence)</li>
                </ul>
                
                <h4>Working with Professionals</h4>
                <p>Consider consulting with:</p>
                <ul>
                    <li>Tax professionals for deduction optimization</li>
                    <li>Real estate agents for market insights</li>
                    <li>Appraisers for assessment challenges</li>
                </ul>
                
                <p>Property taxes are a necessary part of homeownership, but understanding the system can help you manage this expense more effectively. Stay informed about local tax policies and take advantage of available exemptions and appeals processes.</p>
                ''',
                'image_url': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=400&h=300&fit=crop',
                'featured': False,
                'published': True
            }
        ]

        # Create blog posts
        created_count = 0
        for post_data in blog_posts:
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