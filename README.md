# coding-profile-api
A RESTful API designed using Django to get details about a user from a coding profile. It is implemented [here](https://charitra.netlify.app/).


## Using the api
    https://coding-profile-api.herokuapp.com/codingprofile/?&platform=<PLATFORM>&username=<USERNAME>

*Optional parameter* -> ```format=json``` for viewing a complete JSON format.

<br/>

## Supported Platforms
1. *__codechef__* -> For CodeChef data
2. *__gfg__* -> For GeeksForGeeks data
3. *__leetcode__* -> For LeetCode data
4. *__hackerrank__* -> For HackerRank data

Replace *\<PLATFORM\>* with any of the above. <br/>
Replace *\<USERNAME\>* with your user handle for the respective platforms.

<br/>

# Return Type
Returns JSON of the following format. Depends on platform.

1. CodeChef
        <p>
    ```
    {
        "username": "charitra1022",
        "platform": "codechef",
        "stars":    1,
        "rating":   1289,
        "status":   "200"
    }
    ```
</p>

2. GeeksForGeeks
        <p>
    ```
    {
        "username": "charitra1022",
        "platform": "gfg",
        "problems": 29,
        "status":   "200"
    }
    ```
</p>

3. LeetCode
        <p>
    ```
    {
        "username": "charitra1022",
        "platform": "leetcode",
        "problems": 45,
        "status":   "200"
    }
    ```
</p>


4. HackerRank
        <p>
    ```
    {
        "username": "charitra1022",
        "platform": "hackerrank",
        "badges":[
            "Problem Solving": {
                "stars": 2,
                "icon":  <SVG BADGE>,
            },
        ]

        "status":   "200"

    }
    ```
    Returns data of all badges you've earned
</p>


<br/>

## Implementation
This API is implemented on my portfolio site. See [here](https://charitra.netlify.app/).

<br/>

## References
1. [Vanilla JSON Path Picker](https://www.cssscript.com/json-viewer-path-picker/)
