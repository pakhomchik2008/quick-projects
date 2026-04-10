class Graph:
    def __init__(self, directed=False):
        self.graph = {}      # adjacency list
        self.members = {}    # member details
        self.directed = directed

    # Add member
    def add_member(self, name, age, interests):
        if name not in self.graph:
            self.graph[name] = {}
            self.members[name] = {
                "age": age,
                "interests": interests
            }

    # Remove member
    def remove_member(self, name):
        if name in self.graph:
            # Remove all edges pointing to this member
            for person in self.graph:
                if name in self.graph[person]:
                    del self.graph[person][name]

            del self.graph[name]
            del self.members[name]

    # Add relationship
    def add_relationship(self, p1, p2, connection_rate=1):
        if p1 in self.graph and p2 in self.graph:
            self.graph[p1][p2] = connection_rate
            if not self.directed:
                self.graph[p2][p1] = connection_rate



    def friend_discovery(self, p1, p2):
        if p1 in self.graph and p2 in self.graph[p1]:
            strength = self.graph[p1][p2]

            if strength > 5:
                print("Strong friendship detected")
            elif strength > 0:
                print("Weak or normal friendship")

    def mutual_friends(self, p1, p2):
        if p1 in self.graph and p2 in self.graph:
            friends_p1 = set(self.graph[p1].keys())
            friends_p2 = set(self.graph[p2].keys())

            mutual = friends_p1.intersection(friends_p2)

            if mutual:
                print("Mutual friends:", mutual)
            else:
                print("No mutual friends")



    # Show graph
    def display(self):
        print("Members:", self.members)
        print("Connections:", self.graph)


network = Graph()   # Create empty social network

network.add_member("Gleb", 19, ["karate"])
network.add_member("John", 20, ["football"])
network.add_member("Tiago", 21, ["vooo"])
network.add_member("Lamine", 22, ["vv"])

network.add_relationship("Gleb", "John", 5)
network.add_relationship("Gleb", "Tiago", 7)
network.add_relationship("Tiago", "John", 8)

print('connection between Gleb and John')
network.friend_discovery("Gleb", "John")



print('connection between Tiago and Lamine')
network.friend_discovery("Tiago", "Lamine")

network.mutual_friends("Gleb", "Tiago")


network.remove_member("John")

network.display()