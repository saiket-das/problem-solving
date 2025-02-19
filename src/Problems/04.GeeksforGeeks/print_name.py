# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times

# Print name "Saiket Das" 5 times
def print_name_5_time (start, end):
    if (start == end):
        return
    print("%s" % ("Ahan Bryan"))
    print_name_5_time(start + 1, end)

print_name_5_time(0, 5)