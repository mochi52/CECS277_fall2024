#Author: Phuong Tran, Leslie Lopez Arjon, Robert Oceguera
#Date: 09/23/24
#Description: This program reads a file and creates a tasklist. The user can add, mark, remove, and save tasks. 

class Task:
    """
    Attributes:
		description: string description of the task
		date : due date of the task, format MM/DD/YYYY
		time: due time of the task, format HH:MM
    """
    def __init__ (self, desc = "", date = "01/01/2000", time = "00:00"):
        """ Set the description, date, and time of the task to the correct format
        """
        self.desc = desc
        month, day, year = map(int, date.split('/') )
        hour, minute = map(int, time.split(':'))

        if month < 10 :
            month = "0" + str(month)
        if day < 10:
            day = "0" + str(day)
        self.date = f"{month}/{day}/{year}"

        if hour < 10:
            hour = "0" + str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        self.time = f"{hour}:{minute}"

    def get_description(self):
        """ Return the description of the task
        """
        return self.desc

    def __str__ (self):
        """ Return the task as a string to display for user
        """
        return f"{self.desc} - Due: {self.date} at {self.time}"

    def __repr__ (self):
        """ Return the task as a string to write into file
        """
        return f"{self.desc},{self.date},{self.time}"
    
    def __lt__ (self, other) :
        """ Compare the two task by year, month, day, hour, minute, and description
        """
        #extract year, month, and day of the two objects and save them as int
        self_month, self_day, self_year = map(int, self.date.split('/'))
        other_month, other_day, other_year = map(int, other.date.split('/'))

        #extract hour and minute of the two objects and save them as int
        self_hour, self_minute = map(int, self.time.split(':'))
        other_hour, other_minute = map(int, other.time.split(':'))

        if self_year != other_year:
            return self_year < other_year
        if self_month != other_month:
            return self_month < other_month
        if self_day != other_day:
            return self_day < other_day
        if self_hour != other_hour:
            return self_hour < other_hour
        if self_minute != other_minute:
            return self_minute < other_minute
        
        return self.desc < other.desc
    
