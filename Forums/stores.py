

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
        element = member.id
        for elem in MemberStore.members:
               if elem.id == element:
                    elem.name = member.name
                    elem.age = member.age
                    print ("updated ...!")     

class PostStore(object):
	 
    posts = []
    def add(self, element):
        # add post
        PostStore.posts.append(element)

    def get_all(self):
      	# get all posts
      	return PostStore.posts



    