import random
from graph import Graph
from util import Stack, Queue  # These may come in handy


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        numberOfUsers=num_users
        while num_users:
            self.add_user(num_users)
            num_users-=1
        
        DistributionOfFriendships=[]

        while len(DistributionOfFriendships)<len(self.users):
            if DistributionOfFriendships!=True:
                DistributionOfFriendships.append(random.randrange(0,5))
            if len(DistributionOfFriendships)==len(self.users):
                break
            while sum(DistributionOfFriendships)/len(DistributionOfFriendships)!=avg_friendships:
                randomNum=random.randrange(0,5)
                if (sum(DistributionOfFriendships)+randomNum)/(len(DistributionOfFriendships)+1) == avg_friendships:
                    DistributionOfFriendships.append(randomNum)
        # Create friendships

        print(DistributionOfFriendships)
        for i in self.users:
            count=len(self.friendships[i])
            print("HELLLO",i,self.friendships[i])
            # print("COUNT", count, self.friendships[i], len(self.friendships[i]),i)     
            if DistributionOfFriendships[i-1]>0:                
                if count <DistributionOfFriendships[i-1]:
                    while count!=DistributionOfFriendships[i-1]:
                        randomNum=random.randrange(1,numberOfUsers+1)
                        print(DistributionOfFriendships,randomNum, i,len(self.friendships[randomNum]), DistributionOfFriendships[randomNum-1],self.friendships)
                        if len(self.friendships[randomNum])<DistributionOfFriendships[randomNum-1] and randomNum!=i:
                            # print("randomNum",randomNum ,"i",i,"friendships",self.friendships[i], "count", count,DistributionOfFriendships[i-1], self.friendships)
                            if randomNum not in self.friendships[i]:
                                count+=1
                                # print("III",i,"Distribution",DistributionOfFriendships[i-1],"randomNum",randomNum,"count",count)
                                self.add_friendship(i,randomNum)
                                # print("after")
  
  
                
        print(random.randrange(numberOfUsers+1))
        print(DistributionOfFriendships,DistributionOfFriendships[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        graphs=Graph()
        for i in self.users:
            graphs.add_vertex(i)
        
        for i in self.users:
            for x in self.friendships[i]:
                graphs.add_edge(i,x)

        for i in graphs.vertices:
            print(i)
            if graphs.bfs(i,user_id):
                visited[i]=graphs.bfs(i,user_id)
        print("Wow", visited)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
