
class Activity:

    def __init__(self, description, rating, date):
        self.description = description
        self.rating = rating
        self.date = date

    def getActivity(self):
        return self.description
    
    def getRating(self):
        return self.rating
    
    def getDate(self):
        return self.date
    
    def setRating(self, newRating):
        self.rating = newRating

class ActivityManager:

    def __init__(self):
        self.dict = {}

    # Add a new activity to the dictionary
    def addActivity(self, activity):
        if not isinstance(activity, Activity):
            raise ValueError("Invalid activity object!")

        # Check if rating is already in dictionary
        # if it is, add the value to the existing key
        # if it isn't, create a new key and value pair
        if activity.getRating() in self.dict:
            self.dict[activity.getRating()].append(activity)
        else:
            self.dict[activity.getRating()] = [activity]
    
    # Convert dictionary to string
    def toString(self):
        return str(self.dict)
    
    def getMin(self):
        if not self.dict:
            return None
        
        min_rating = min(self.dict.keys())
        return self.dict[min_rating]
    
    def updateActivityRating(self, activity, newRating):
        if not isinstance(activity, Activity):
            raise ValueError("Invalid activity object!")

        # Remove the activity from the old rating category
        if activity.getRating() in self.dict:
            self.dict[activity.getRating()].remove(activity)
            if not self.dict[activity.getRating()]:
                del self.dict[activity.getRating()]

        # Update the activity's rating and add it to the new rating category
        activity.setRating(newRating)
        if newRating not in self.dict:
            self.dict[newRating] = [activity]
        else:
            self.dict[newRating].append(activity)

    def toString(self):
        return str(self.dict)



if __name__ == "__main__":
    manager = ActivityManager()
    activity1 = Activity("test", 6)
    activity2 = Activity("test2", 4)
    activity3 = Activity("test3", 7)
    manager.addActivity(activity1)
    manager.addActivity(activity2)
    manager.addActivity(activity3)
    print(manager.toString())

    manager.updateActivityRating(activity1, 2)
    print(manager.toString())
    print(activity1.getRating())

