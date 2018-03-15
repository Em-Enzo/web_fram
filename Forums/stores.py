
import datetime
import itertools
import copy



class MemberStore(object):
	 
    last_id = 1
    members =[]
    
    def add(self, element):
        # append member
        element.id = MemberStore.last_id
        MemberStore.members.append(element)
        MemberStore.last_id += 1

    def get_all(self):
      	# get all members
      	return MemberStore.members

    def get_by_id(self, id):
        # get member by id 
        all_members = self.get_all()
        result = None 
        for member in all_members:
          if member.id == id :
              result = member
              break  
        return result

    def entity_exists(self, member):
        # check if member exists or not
        result = True
        if get_by_id(member.id) == None:
          result = False
        return result

    def delete(self, id):
        # delete a member
        element = self.get_by_id(id)
        if element != None:
          MemberStore.members.remove(element)
          print ("member is deleted !")
        else:
          print ("member not found !")
      

    def update(self, member):
        # update the list or the DB
        all_members = self.get_all()
        for index, element in enumerate(all_members):
               if element.id == member.id:
                    all_members[index] = element
                    print ("updated ...!") 

    def get_by_name(self, name):
          # search and find the name in the list or the DB         
          all_members = self.get_all()
          #for element in all_members:
           #   if element.name == name:
            #      yield element 
          return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, all_posts):
      # returns all the members with thiere posts
      all_members = copy.deepcopy(MemberStore.get_all)
      for member, post in itertools.product(all_members, all_posts):
        if member.id == post.member_id:
          member.posts.append(post)
      for member in all_members:
          yield member

    def get_top_two():
      # returs the top two participation members
      all_members = list(self.get_members_with_posts(all_posts))
      all_members.sort(key= lambda element: len(element.posts), reveres= True) 
      yield all_members[0]
      yield all_members[1]



class PostStore(object):
	 
    posts = []
    def add(self, element):
        # add post
        PostStore.posts.append(element)

    def get_all(self):
      	# get all posts
      	return PostStore.posts



    