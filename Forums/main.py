


import models
import stores


member1 =models.Member("John", 23) 
member2 = models.Member("Sara", 24)


post1 =models.Post("title1", "subject1")
post2 =models.Post("title2", "subject2")
post3 = models.Post("title3", "subject3")


member_store = MemberStore()
member_store.add(member1)
member_store.add(member2)

print (member_store.get_all())

post_store = PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

print (post_store.get_all())