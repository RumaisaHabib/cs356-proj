import pprint
import praw
from praw.models import MoreComments
import re
from tqdm import tqdm

url_regex = re.compile(r'\b(https?://\S+\.\S+)\b') 

# client_id fqxCGv6TR3f6fEm5AkvrKw
# secret akWGg_EdFNHk_9X6w61uCF-VL1WuUQ
# 

reddit = praw.Reddit(
    client_id="fqxCGv6TR3f6fEm5AkvrKw",
    client_secret="akWGg_EdFNHk_9X6w61uCF-VL1WuUQ",
    user_agent="my user agent",
)

# Construct a list of subreddits
SUBREDDIT_LIST = ["gaming", "music", "worldnews", "movies", "science", "videos", "food", "DIY", "books", "sports","television","travel","gardening","programming","soccer
"]
#SUBREDDIT_LIST = ["food"]

# Number of urls we want from each subreddit
NUM_URLS = 100


def main():

    # Loop through subreddits 
    for subred in SUBREDDIT_LIST:
        subreddit_urls = []
        subreddit = reddit.subreddit(subred)
        print(subreddit.title)

        # Loop thru posts in subreddit
        subreddit_parsed = False # bool to stop the extraction once 1000 urls reached

        for submission in tqdm(subreddit.top(limit=200)):
            # go through the main body of the submission
            this_submission = url_regex.findall(submission.selftext)

            # Going through all top level comments in submission
            for comment in submission.comments:
                if isinstance(comment, MoreComments):
                    continue
                if len(this_submission) > 10:
                	break
                
                this_submission += url_regex.findall(comment.body)
                this_submission = [x for x in this_submission if "imgur" not in x]
                
            count = min(len(this_submission),10)
            # only get 10 from each post
            subreddit_urls += this_submission[:count]
	        
            if len(subreddit_urls) >= NUM_URLS:
                subreddit_parsed = True
                subreddit_urls = subreddit_urls[:NUM_URLS] # truncate as appropriate
                break
            
            # End the parsing process for this subreddit
            if subreddit_parsed:
                break
        
        # By the end we want to append the subreddit urls to a txt file 
        fp = subred + "_urls.txt"
        with open(fp, 'w') as file:
            file.writelines("\n".join(subreddit_urls))



if __name__ == "__main__":
    main()
