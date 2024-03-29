# Automatic Marks Entry System using Digit Recognition

Welcome to the README file for the Automatic Marks Entry System project! This project is designed to automate the process of calculating total marks scored by students on their test papers. The system scans the front sheet of the test paper, performs digit recognition using a pre-trained model (stored as `model.h5`), and calculates the total marks achieved by the student. The model is trained on the MNIST dataset for digit recognition. This project aims to assist teachers in reducing the time and effort required to manually calculate marks for each paper.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Automatic Marks Entry System project offers an innovative solution to automate the process of calculating total marks obtained by students on their test papers. By utilizing digit recognition technology, the system scans the front sheet of the test paper, recognizes the digits representing the marks, and calculates the total score achieved by the student. The underlying digit recognition model is trained using the MNIST dataset, and the trained model is stored as `model.h5`. This project is a step towards leveraging automation to enhance the efficiency of teachers in evaluating test papers.

## Features

The Automatic Marks Entry System project includes the following features:

- **Front Sheet Scanning**: The system allows teachers to scan the front sheet of a test paper containing digitized marks.

- **Digit Recognition**: The pre-trained digit recognition model (stored as `model.h5`) identifies the individual digits representing the marks.

- **Total Marks Calculation**: The system calculates the total marks scored by summing up the recognized digits.

- **Efficiency Enhancement**: The project assists teachers in automating the process of calculating marks, reducing manual effort and errors.

## Installation

To set up the Automatic Marks Entry System project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/marks-entry-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd marks-entry-system
   ```

3. Install the required dependencies (make sure to have the necessary libraries for digit recognition and model usage).

4. Ensure that the `model.h5` file containing the pre-trained digit recognition model is present.

## Usage

1. Launch the application.

2. Scan the front sheet of the test paper using a scanner or camera.

3. The system will process the scanned image and recognize the digits.

4. The recognized digits will be used to calculate the total marks achieved by the student.

## Future Enhancements

As a future enhancement, consider implementing mobile integration for the Automatic Marks Entry System. This would allow teachers to use their mobile devices to scan and process the front sheet of the test paper. Mobile apps could leverage the same digit recognition model and provide an even more convenient way for teachers to automate the marks calculation process.

## Contributing

We encourage contributions to the Automatic Marks Entry System project! If you wish to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them with clear commit messages.

4. Push your changes to your forked repository.

5. Create a pull request to the main repository's `develop` branch, explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore, utilize, and contribute to the Automatic Marks Entry System project. If you encounter any issues or have suggestions, please create an issue on the repository. Happy automating! 🚀
