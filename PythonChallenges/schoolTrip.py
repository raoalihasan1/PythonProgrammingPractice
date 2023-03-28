# A school teacher is organizing a school trip for the whole year group. He expects between 250 and 350 students to attend this
# trip. To estimate the cost of the trip, the school teacher has contacted a coach company to hire several coaches for a day.

# The school teacher would like a computer program that will:
# 1.  Ask for the number of students taking part in the trip.
# 2. Ask for the number of teachers taking part in the trip.
# 3. Calculate the total number of participants (by adding the number of students and the number of teachers).
# 4. Find out and output the number of large coaches that will be required.
# 5. Find out and output the number of small coaches that will be required.
# 6. Calculate and output the total cost of hiring these coaches for a day.

def main():
    numStudents = int(input("Enter The Number Of Students: "))
    numTeachers = int(input("Enter The Number Of Teachers: "))
    totalParticipants = numStudents + numTeachers
    largeBus = totalParticipants // 46
    smallBuses = (totalParticipants % 46) // 16
    if ((totalParticipants % 46) % 16) > 0:
        smallBuses += 1
    totalCost = (largeBus * 360) + (smallBuses * 140)
    print("Total Number Of Participants: ", totalParticipants)
    print("Number Of Large Buses Required: ", largeBus)
    print("Number Of Small Buses Required: ", smallBuses)
    print("Total Cost Of Hiring Buses:  £{}".format(totalCost))

# Extension Task #1
# You have noticed that it is more cost effective to hire a large bus (£360) instead of three small buses (3 * £140 = £420) even if the large bus is not full.
# So your task is to adapt the above algorithm so that, when calculating the number of large buses, if the number of pupils left (remainder) is greater than 32,
# your program will hire one extra large bus instead of 3 small buses. It will hence output the most cost effective solution for test


def main_ext():
    numStudents = int(input("Enter The Number Of Students: "))
    numTeachers = int(input("Enter The Number Of Teachers: "))
    totalParticipants = numStudents + numTeachers
    largeBus = totalParticipants // 46
    if ((totalParticipants % 46) > 32):
        largeBus += 1
        smallBuses = 0
    else:
        smallBuses = (totalParticipants % 46) // 16
        if ((totalParticipants % 46) % 16) > 0:
            smallBuses += 1
    totalCost = (largeBus * 360) + (smallBuses * 140)
    print("Total Number Of Participants: ", totalParticipants)
    print("Number Of Large Buses Required: ", largeBus)
    print("Number Of Small Buses Required: ", smallBuses)
    print("Total Cost Of Hiring Buses:  £{}".format(totalCost))
