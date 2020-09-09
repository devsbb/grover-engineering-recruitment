# Coding Challenge - Checks and Balances

You are tasked with writing a piece of software to do Checks and Balances.
It must comprise an HTTP Server with two endpoints:

- One to insert a new monetary transaction, money in or out, for a given user;
- One to return a user's current balance.

## Requirements:

- It must not be possible to withdraw money for a given user when they don't have enough balance;
- You should take concurrency issues into consideration;
- It must be executable in Linux & macOS machines;
- You don't have to worry about databases; it's fine to use in-process, in-memory storage;
- It must be production quality according to your understanding of it - tests, README, etc.

## General notes:

- This challenge will be extended by you and a Grover engineer on a different step of the process;
- Please make sure to anonymize your submission by removing your name from file headers and such;
- Feel free to expand your design in writing;
- You will submit the source code for your solution to us as a compressed file containing all the code and possible documentation. Please make sure to not include unnecessary files such as the Git repository, compiled binaries, etc;
- Please do not upload your solution to public repositories in GitHub, BitBucket, etc.

## Things we're looking for:

- Immutability;
- Separation of concerns;
- Unit and integration tests;
- API design;
- Correct handling of decimal values;
- Error handling.
