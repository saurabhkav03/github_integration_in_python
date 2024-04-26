# github_integration_in_python
 
# GitHub API Pull Requests

## Introduction
This program makes an API call to GitHub to retrieve information about pull requests for the Kubernetes repository. It uses the `requests` module in Python to perform the API request.

## Usage
1. Install the `requests` module using pip:
   ```
   pip install requests
   ```

2. Make an API call using the following URL:
   ```
   https://api.github.com/repos/kubernetes/kubernetes/pulls
   ```

3. The output will be in JSON format, which is converted into a dictionary using the `response.json()` function.

4. The program prints the username and the number of pull requests created.


