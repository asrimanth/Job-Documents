# Job-Documents

A repo which automates documents related to job search and application

**Usage:**

For Cover letter:
To create a cover letter from the existing master cover letter, follow these steps:

+ Fix an ID number to begin. Let's call it <\<ID\>>. (Example: assume ID is 101)
+ Go to the JobRelevantContent folder.
    + Create Job address file in the following format: <\<ID\>>_address.txt (101_address.txt) and fill it with the mailing/email address.
    + Create Job content file in the following format: <\<ID\>>_content.txt (101_content.txt) and fill it with the core content needed to be catchy!
+ Now we need to run the python command. Let's define some parameters:
    + <\<CompanyName\>> (Ex: GitHub) as a string enclosed in "".
    + <\<JobTitle\>> (Ex: Data Scientist) as a string enclosed in "".
    + <\<Job_ID\>> (Ex: 101) as a number.
    + <\<RecruiterName\>> (Ex: XYZ) as a string enclosed in "".
    + <\<ContentJob_ID\>> (Ex: 1) as a number.
    + Note: ContentJob_ID can be used when we want to copy the contents of a previously applied job using this method. Also, the RecruiterName can be empty, if you are applying to a company in general.
+ Putting it all together, we run the following command:
```bash
python3 cover_letter_master_to_relevant.py  "<<CompanyName>>" "<<JobTitle>>" "<<Job_ID>>" "<<RecruiterName>>" "<<ContentJob_ID>>"
```
Example Commands:
To create a new cover letter from scratch, we do the following:
```bash
python3 cover_letter_master_to_relevant.py  "GitHub" "Data Scientist" 101 "XYZ"
```

To take the content from a previously written cover letter content, take the id of the previous (Ex: 100) and do the following:
```bash
python3 cover_letter_master_to_relevant.py  "GitHub" "Data Scientist" 101 "XYZ" 100
```
