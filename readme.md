# Version Comparison application
Hello welcome to Version Comparison API endpoint application.
The compare endpoint is used for comparing versions in this application.

## Assumptions
For this application I am making an assumption that the values in the versions are always numeric.
If we see any alphabetic values or they don't follow the format of versioning (i.e. it contains commas or other delimiter than `.` it will raise an error)

## "/compare/version1/version2"
This will compare the version1 with version2 and return if it is `"before"`, `"after"` or `"equal"`

## Example to see the results for the endpoints
`http://localhost:5000/`: This will show the homepage of the application

`http://localhost:5000/compare/1.0/1.0`: This call will return 1.0 is "equal" 1.0

`http://localhost:5000/compare/1.0/1.0.1`: This call will return 1.0 is "before" 1.0.1

`http://localhost:5000/compare/1.0.1/1.0`: This call will return 1.0.1 is "after" 1.0

`http://localhost:5000/compare/1.0.1/1.a`: This type of call violates our assumption so it shows the following message `Enter the version numbers in with only numeric values and "." in it and nothing else`

## Steps to execute the following Docker code
If you have python and flask installed in your system you can choose to follow below steps:
1) go the folder where the application is saved
2) run the command on the shell or PowerShell or CMD `$ python app.py`

If you want to run docker file follow the below steps:
1) `$ docker build -t version-comparison-application .`
2) `$ docker run -d -p 5000:5000 version-comparison-application`

Note:
1) To install flaks in your system use `$ pip install flask` or use https://flask.palletsprojects.com/en/1.1.x/installation/ this link for it
2) Install python too in the system
3) If using Docker use `.` or provide the file path for the docker to build
