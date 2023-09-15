#### Minimum Requirements:
    A CLI application that solves a real-world problem and adheres to best practices. 
    - [] A database created and modified with SQLAlchemy ORM with 2+ related tables.
    - [] A well-maintained virtual environment using pipenv.
    - [] Proper package structure in your application.
    - [] Use of lists and dicts. 


#### Project Pitch Idea:
    Main Idea: Fitness Tracker Application

        User Story:
        The main goal of my application will be to allow users to track their weightlifting journey. By this, I mean their progress Personal Records, weight, etc. Hopefully, this will expand into a fitness app to keep track of both the physical and nutritional aspects of their journey.  

        Meeting the Project Requirements:
        Object-Oriented Python: I will use classes to model different components such as the User, Weight, and Workouts each containing attributes and methods for data management. 

        Database Tables: Using SQLAlchemy, I will create three tables, Users that will contain basic user information, a weight tracking table for tracking weight progress, and a Workout Table to track types of exercise. 

        Object relationships: The User class will have a relationship with the Weight Class, and Workouts connecting what their progress and completions are. This will show weight data and workout sessions they input. This info will be stored as they continue to log this information. 

        Aggregate and Associate Methods: Methods will be included in the User class to calculate how many exercises a user did, whether it was primarily focused on a body part, and the progression of their weight. 

        Use of Data Structures: I will be using lists to store and manage workouts weight goals, and workout details. these data structures will help organize information and make proper calculations. 

        What area will be the most challenging: I think the most challenging part of this project will be accurately calculating the weight tracking goals as you have to take into account the user's personal goals. Everyone's inputs will be different and we need to continuously add this kind of information in the long run to view a wide range of data. 