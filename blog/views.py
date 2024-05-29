from django.shortcuts import render

from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image" : "ball.jfif",
        "author" : "Timi",
        "date" : date(21, 5, 23 ),
        "title": "Sport",
        "excerpt":"There is nothing like the rush you get playing your favourite sports",
        "content" : """
                   
I played football passionately for several years, showcasing my skills on the field. Although many coaches recognized my talent and encouraged me to continue, I made the decision to prioritize my education over club play. Football remains my love, and although i was scouted for Rangers FC I believe education is more important.

I'm passionate about basketball, thriving in the pickup games I play on weekends. Despite never joining a team, coaches have acknowledged my talent and skills. I prioritize my education, opting out of club commitments to focus on school. I relish the freedom of pickup basketball, where my love for the game truly flourishes.

                    """ 
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "TIMI'S BLOG",
        "date": date(21, 5, 23),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """I am a passionate coder who loves diving into the world of web development. With HTML, Python, and CSS as my trusty companions, I craft interactive and visually appealing websites. My confidence soars with Django, allowing me to build robust and dynamic web applications. Though my JavaScript knowledge may be minimal, I eagerly embrace opportunities to expand my skills. Coding is my canvas, and I paint with pixels and lines of code.       
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "TIMI'S BLOG",
        "date": date(21, 5, 23),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
      I have been captivated by the beauty of nature ever since I embarked on my Duke of Edinburgh Award journey. The outdoors became my sanctuary, and I developed an insatiable love for exploring the wonders that surround me. Now, I find immense joy in immersing myself in the natural world, observing its intricate details and discovering hidden treasures along the way.
        """
    }
]

def get_date(post):
    return post['date']
    

# Create your views here.

def starting_page(request):
    sorted_posts = sorted( all_posts, key = get_date )
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", { 
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html" , {
        "all_posts" : all_posts
    })

def post_detail(request , slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug )
    return render(request, "blog/post-detail.html" , {
        "post" : identified_post
    })