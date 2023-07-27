# Employee-Retention
https://employee-retention.onrender.com

# Business Problem
## Context
Our client is the HR department at a large software company.
* They are rolling out a new initiative that they call "Proactive Retention."
* The idea is to use data to predict whether and employee is likely to leave.
* Once these employees are identified, HR can be more proactive in reaching out to them before it's too late.
* For this initiative, they only care about permanent (non-temp) employees.

## Current approach
Currently, their employee retention process is very retroactive. Once an employee leaves, he or she takes an "exit interview" and shares reasons for leaving. HR then tries to learn insights from that interview and make changes around the company accordingly.

This suffers from 3 main problems:
* The first problem with this approach is that it's too haphazard. The quality of insight gained from an interview depends heavily on the skill of the interviewer.
* The second problem is that they can't systematically aggregate insights across all employees who have left.
* The third problem is that they can't be proactive because they are using exit interviews to drive policy changes.

## Problem Statement
* The HR department has hired us as data science consultants. They want to supplement their exit interviews with a more proactive approach.
* They've asked their business intelligence analysts to provide us a dataset of past employees and their status (still employed or already left).

## Business Objectives and Constraints
* Deliverable: Trained model file
* Model interprtability is very important
* Ouput Probabilities along with the prediction
* No latency constraints
