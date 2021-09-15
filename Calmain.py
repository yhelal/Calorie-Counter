# Command                      Description
# list eaten <name> <date>     List foods eaten on a given date.
# list weights <name>          List the weight history for a user.
# list dates <name>            List the dates for which there are calorie counts
# list foods                   List all calorie data for known foods
# lookup calories <food>       Look up calories for a given food.
# lookup weight <name> <date>  Look up weight for a given date.
# total <name> <date>          Calculate total calories for a given user and date.
# newuser <name>               Create a new user.
# eaten <name> <food> <weight> Add a food data for today.
# weighed <name> <weight>      Add weight data for today.

import sys
import calories

if len(sys.argv) > 1:
    cmd = sys.argv[1]
    if cmd == 'list':
        if len(sys.argv) > 3 and sys.argv[2] == 'eaten':
            calories.list_eaten(sys.argv[3], sys.argv[4])
        else:
            if sys.argv[2] == 'weights' and len(sys.argv) > 3:
                calories.list_weights(sys.argv[3])
            elif sys.argv[2] == 'dates' and len(sys.argv) > 3:
                calories.list_dates(sys.argv[3])
            elif sys.argv[2] == 'foods':
                calories.list_foods()
    elif cmd == 'lookup':
        if len(sys.argv) > 2:
            if sys.argv[2] == 'calories':
                calories.lookup_calories(sys.argv[3])
            elif sys.argv[2] == 'weight' and len(sys.argv) > 3:
                calories.lookup_weight(sys.argv[3], sys.argv[4])
    elif cmd == 'total':
        if len(sys.argv) > 2:
            calories.total_date(sys.argv[2], sys.argv[3])
    elif cmd == 'newuser':
        if len(sys.argv) > 2:
            calories.new_user(sys.argv[2])
    elif cmd == 'eaten':
        if len(sys.argv) > 4:
            calories.eaten(sys.argv[2], sys.argv[3], sys.argv[4])
    elif cmd == 'weighed':
        if len(sys.argv) > 3:
            calories.weighed(sys.argv[2], sys.argv[3])
    else:
        print('Command not understood')

