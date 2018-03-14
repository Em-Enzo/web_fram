

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
        result = all_members[id] 
        return result

    def entity_exists(self, member):
        # check if member exists or not
        result = True
        if get_by_id(id) == member.id:
          result = False
        return result

    def delete(self, id):
        # delete a member
        members.remove(get_by_id(id))

        

class PostStore(object):
	 
    posts = []
    def add(self, element):
        # add post
        PostStore.posts.append(element)

    def get_all(self):
      	# get all posts
      	return PostStore.posts



    