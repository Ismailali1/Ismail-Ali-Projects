import random
#ismail ali
#iti 1120
#student number: 300008883
# Sadiq abbas

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    friendsCopy = []
    numFriends = int(friends.pop(0))
    network = []

    for x in friends:
        nums = x.split()
        reverse = nums[1] + ' ' + nums[0]
        friendsCopy.append(reverse)

    friends = friends + friendsCopy

    sortedlist = sorted(friends)

    j = int(sortedlist[0][0])
    array = []

    #For testing
    file = open("testfile.txt", "w")

    #For i = 0 to numFriends - 2
    for i in sortedlist:
        num = i.split()
        if int(num[0]) == j:
            array.append(int(num[1]))

        elif int(num[0]) > j:

            temp = list(array)
            array = []
            network.append((j, temp))
            array.append(int(num[1]))
            #file.write(str(j) + " --- " + str(temp))
            j = int(num[0])

    #For last index, numFriends - 1
    network.append((j, array))
    file.close()

    network.sort()
    for x in network:
        x[1].sort()



    return network

    # YOUR CODE GOES HERE

    # return network


def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs,
    and friends of user 1 and user 2 sorted
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''

    common = []
    for friend in network:
        if user1 in friend[1] and user2 in friend[1]:
            common.append(friend[0])

    return common





def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.

    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    rec = 0
    connected = []
    flag = 0
    mutual = 0


    for i in range(0,len(network)):
        if network [i][0] == int(user):
            connected = network[i][1]

    for i in range(0, len(network)):
        flag = 0
        if network[i][0] != int(user) and int(user) not in network[i][1]:
            for j in range(0, len(connected)):
                if connected[j] in network[i][1]:
                    flag = flag + 1

            if flag > mutual:
                mutual = flag
                rec = network[i][0]
            if flag == mutual:
                rec = min(rec, network[i][0])
    if mutual != 0:
        return rec
    else:
        return None








def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    numberflag = 0
    for i in range(0, len(network)):
        if len(network[i][1]) >= k:
            numberflag = numberflag + 1
    return numberflag
    pass


def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    mostfriends = 0

    for friendship in network:
        mostfriends = max(mostfriends, len(friendship[1]))

    return mostfriends

    pass


def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends = []
    mostfriends2 = maximum_num_friends(network)
    for i in network:
        if len(i[1]) == mostfriends2:
            max_friends.append(i[0])

    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    totalfriends = 0

    for i in network:
        totalfriends += len(i[1])

    return totalfriends / len(network)
    pass


def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    knowseveryone = False

    for i in range(0,len(network)):
        if len(network[i][1]) == len(network)-1:
            knowseveryone = True

    return knowseveryone



####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    while True:
        try:
            uid = int(input("Enter an integer for a user ID: "))
        except:
            print("That was not an integer!.")
            continue;

        for i in network:
            if i[0] == uid:
                return uid;

        print("That user ID does not exist!")
    pass


##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name = get_file_name()
create_network(file_name)

net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")


print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

