# flatiron-phase-3-project
#Fitness App Tracker
version 1.10

The Fitness Tracker CLI is a command-line tool that lets users track their fitness progress. This includes access to personal user accounts, logging workouts, and tracking weight changes.
## Table of Contents

- [flatiron-phase-3-project](#flatiron-phase-3-project)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Commands](#commands)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To use the Fitness Tracker CLI, follow these steps:

1. **Clone the Repository**
   Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/saulceja08/flatiron-phase-3-project

2. **Install necessary dependencies**
   cd flatiron-phase-3-project
   pip install -r requirements.txt

3. **Run in Terminal**
   Open your terminal, open the file directory and call the scripty using "python main.py"

4. **Interact with the Terminal**
   User will now be able to interact with the terminal once steps 1-3 are complete!

## Commands
    - create_user: Create a new user account by filling out --> username, password, first name, last name, birth date, and email.

    - log_workout: Log a workout session by choosing username and the duration of the workout in minutes.

    - log_weight: Log weight changes by providing a weight for pre and pots workout. 

    - delete_workout: Delete a workout session by choosing username and the workout ID.
  
## Project Structure
    The project structure is organized as follows:

    main.py: The entry point of the CLI application, which provides the user interface for interaction.

    app/models.py: Defines the database models using SQLAlchemy, including User, Workout, and WeightTracker.

    commands/: Contains Python code for each CLI command 

    database/: Stores the SQLite database file (fitness.db) used for storing all data

## Contributing
    Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests. Please follow the code of conduct and contributing guidelines.

## License
    This project is licensed under the MIT License - see the LICENSE file for details.

