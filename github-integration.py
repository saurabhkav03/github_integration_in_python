import requests

# Define the URL for the GitHub API endpoint
url = f"https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Make a GET request to the GitHub API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    pull_requests = response.json()
    
    # Initialize an empty dictionary to store PR creators and their counts
    pr_creators = {}
    
    # Iterate through each pull request
    for pull in pull_requests:
        # Extract the creator's login username from the pull request data
        creator = pull['user']['login']
        
        # Increment the count for the creator in the dictionary
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    
    # Print the creators and their counts
    print("The creators and their counts:\n")
    for creator, count in pr_creators.items():
        print(creator, count)

# If the request was not successful, print an error message with the status code
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
