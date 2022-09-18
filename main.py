import scratchconnect
import time

startTime = time.time()
login = scratchconnect.ScratchConnect()
user = login.connect_user(username="TimMcCool") # profile username goes here
user.update_data()

amntCommentsToScan = 1000 # feel free to change this, but values over 1000 don't seem to work

comment = ""
comments = []

def getComments(amount):
    for p in range(int(amount/20)):
        output = user.comments(limit=20, page=p+1) # gets comments in groups of 20 (any more tends to slow things down)

        for i in range(len(output)):
            try:
                comment = output[i]
                comments.append(comment['Content'])  # keeps only the contents of the comment and adds it to a list
                idx = (p * 20) + i + 1
                idx = round(idx / (amount / 100), 2)
                print(str(idx) + "% - " + str((p * 20) + i + 1) + "/" + str(amount))
            except:
                print("Something went wrong!")

    time.sleep(0.15)

print()
print("=== PART 1 - FETCH COMMENTS ===")

user.update_data()  # Update the data
print("Updating data...")

print("Fetching comments...")
getComments(amntCommentsToScan)

print(comments)

print()
print("=== PART 2 - SORT DATA ===")

advertisingKeywords = ["follow me", "f4f", "scratch.mit.edu", "look at my", "follow for follow"]
keywordsFound = {}
adverts = []

print("Preparing dictionary...")
for w in advertisingKeywords: # populates dictionary
    keywordsFound[w] = 0

def scanComments():
    for commentTest in comments: # the comment to test for keywords
        for keyword in advertisingKeywords: # the keyword being tested
            lowerKeywordIdx = commentTest.find(keyword)
            upperKeywordIdx = commentTest.find(keyword.upper())
            containsCheck = lowerKeywordIdx > -1 or upperKeywordIdx > -1
            if containsCheck: # checks if the comment contains a keyword
                keywordsFound[keyword] += 1
                print(str(sum(keywordsFound.values())) + " instances found! Keyword: " + keyword) # prints total instances of keywords
                adverts.append(commentTest)
                break

print("Scanning comments...")
scanComments()
print(keywordsFound)

print()
print("=== FINAL RESULTS ===")

print(str(sum(keywordsFound.values())) + " instances found!")

print("Distribution")
print(keywordsFound)
print()
print("Found adverts")
print(adverts)
print()
print("Process took " + str(time.time() - startTime) + " seconds")