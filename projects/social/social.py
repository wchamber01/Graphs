from util import Stack, Queue
from graph import Graph
import random


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
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = []
        # Avoid duplicates by ensuring the first number
        # is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # print(range(user_id + 1, self.last_id + 1))
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # print('self.users:', random.shuffle(possible_friendships))

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        starting_person = user_id
        q.enqueue([starting_person])
        visited = {}  # Note that this is a dictionary, not a set

        # Repeat until queue is empty
        while q.size() > 0:

            # Dequeue first person i.e: remove from queue
            person = q.dequeue()  # This is my path
            # print('person:', person)
            # Grab the last person (vertex) from the path and set it to our current_person
            current_person = person[-1]
            # print('current:', current_person)

            # Have we visited the person yet? If not then visit it.
            if current_person not in visited:
                # print('visited:', visited)

                # Set currently visited person to the person position currently at
                visited[current_person] = person

            # For each friend of the starting_person...
            for friend in self.friendships[current_person]:
                # If the friend has not been visited yet...
                if friend not in visited:
                    # Make a *copy* of person
                    next_person = list(person)
                    # Add current friend to next_person
                    next_person.append(friend)
                    # Make this friend the next starting_person
                    q.enqueue(next_person)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('sg.friendships:', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('connections:', connections)
