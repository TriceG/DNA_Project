class UserData():
    #create a 2D list that contains all the user data
    global userList
    userList = [[0]]
    def __init__(self, name):
        self.name = name
        #is name input in the list?
        found = "no"
        for row in userList:
            if row[0] == name:
                found = "yes"
        if found != "yes":
            #add the new user to the list and initialize it's scores to 0
            userList.append([self.name,0,0,0,0,0,0])

    #Adding scores
    def addScore(self, score, game, level):
        s_index = 0
        for user in userList:
            if user[0] == self.name:
                if game == 1:
                    if level == 'b':
                        s_index = 1
                    elif level == 'i':
                        s_index = 2
                    else:
                        s_index = 3
                else:
                    if level == 'b':
                        s_index = 4
                    elif level == 'i':
                        s_index = 5
                    else:
                        s_index = 6
                user[s_index] = score
''' 
###Test Script###

a = UserData("Cat")
b = UserData("Horse")
c = UserData("Horse")
a.addScore(50, 1,'b')
a.addScore(60, 2,'i')

print (userList)
'''