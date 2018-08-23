from dotenv import load_dotenv
from slack import get_files, delete_files, DeleteFilesError
import datetime, math

def run():
    print("slack-deletefiles v2.0 (now with multithreading! probably)")
    print("developed by ChaoticWeg, with apologies to the RangerFam\n")

    # get time of oldest file to keep
    ts = get_oldest_ts()

    print("timestamp of oldest file left: %s" % ts)

    # track total number of files deleted
    total_ids = []
    bad_ids = []
    num_passes = 0

    # fetch/delete loop
    while True:
        print("\n-----\nPASS %d\n-----" % (num_passes + 1))
        print("grabbing files posted before %d" % ts);

        these_ids = get_files(ts_to=ts)
        print("got %d TOTAL files" % len(these_ids))
        
        good_ids = [ f for f in these_ids if not f in bad_ids ]
        num_ids = len(good_ids)
        print("got %d GOOD files" % num_ids)

        if num_ids < 1:
            break
        
        num_passes += 1
        total_ids.extend(good_ids)

        these_bad_ids = delete_files(good_ids)
        print("bad files this pass: [ %s ]" % (', '.join(these_bad_ids)))
        bad_ids.extend(these_bad_ids)
    
    print("\n-----\nlooks like we're done\n-----")
    print("deleted %d files on %d passes" % (len(total_ids), num_passes))
    print("files we were able to delete (%d): [ %s ]" % (len(total_ids), ', '.join(total_ids)))
    print("files we tried but failed to delete (%d): [ %s ]" % (len(bad_ids), ', '.join(bad_ids)))



def get_oldest_ts():
    now = datetime.datetime.utcnow()
    then = now - datetime.timedelta(days=30)
    return math.floor(then.timestamp())

if __name__ == "__main__":
    load_dotenv()
    run()
