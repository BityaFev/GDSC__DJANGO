from .models import post, Comment

def CreatePost():
    post1 = post.objects.create(
        Title= "1st blog",
        Content="new content",
        Category="tech",
        Image="C:\Users\DELL\Pictures\pic.jpg"
        )
    post2 = post.objects.create(
        Title="2nd blog",
        Content="updatd content",
        Category="tech",
        Image="C:\Users\DELL\Pictures\pic.jpg"
    )
    post3 = post.objects.create(
        Title="3rd post",
        Content="most recent content",
        Category="info",
        Image="C:\Users\DELL\Pictures\pic.jpg"
    )
    return post1, post2, post3

def PostByCategory(Category):
    posts= post.objects.filter(Category=Category)
    for post in posts:
        print(f"Title:{post.Title}") 
        print(f"Title:{post.Content}") 
        print(f"Title:{post.Category}") 
        print(f"Title:{post.Image}") 

def UpdateContent(post, newContent):
    post.Content = newContent
    post.save()

def DeletePost(Title):
    post = post.objects.filter(Title = Title)
    post.delete()

#create post
post1, post2, post3 = CreatePost()

#display post in specific category
Category = "tech"
PostByCategory(Category)

#update the content
newContent = "updated post"
UpdateContent(post1, newContent)
