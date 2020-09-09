# Grover Engineering

If you want to participate on the hiring process please sign up in this spreadsheet
[Hiring Process Sign Up](https://docs.google.com/spreadsheets/d/1hNMujeMNLtF1-e0np90cpJ3Lwt8w4ojZjma8CHzMmvQ/edit?usp=sharing)

# Grover Engineering Recruitment Test

Thank you for taking the time to do our technical test. Basically, it consists of two parts:

- [A coding test](#coding-test)
- [A few technical questions](#technical-questions)

Please, submit your results by sending a ZIP file to your Grover contact person and make this a **single** zip file named `{yourname}-{position-applied}.zip` containing:

1. a single markdown file (FOLLOW-UP.md) with the answers to the follow-up questions
2. one folder containing the technical test

## Context

Grover is a fresh alternative to the traditional product ownership model for consumers, providing a highly flexible monthly subscription service for everyday devices such as laptops, smartphones, tablets, digital cameras, and more!

We announced recently that consumers can now rent tech in every MediaMarkt store in Germany: 200+ locations, from Flensburg to Friedrichshafen, meaning, they can simply visit any of these stores, rent with Grover and walk away with tech in hand.

## Coding Test

The task is to create an application to show the consumer the products available in a given store. Remember that each store could have a different portfolio of products and different stock levels for the same product.

Basically, when querying the API the application should return a list of products containing:

- Name
- Brand
- Category
- Availability (in stock | out of stock)
- Quantity in stock

### Task requirements

Feel free to spend as much or as little time on the exercise as you like as long as the following requirements have been met.

- Please complete at least _one_ of the user stories below.
- Your code should compile and run in one step.
- Feel free to use whatever frameworks / libraries / packages you like.
- You **must** include tests
- Please avoid including artifacts from your local build (such as node_modules packages or the bin folder(s)) in your final ZIP file

### User Story

As a **consumer in store running the application**  
I can **view a list of products in this store (e.g. `grover-de`)**  
So that **I know which products are currently available to rent**

As a **consumer in store running the application**  
I can **chose to see unavailable products in this store**  
So that **I can subscribe for waiting list**

#### Acceptance criteria

- For the known store codes `grover-de` and `mm-berlin`, products are returned based on the availability filter
- Available products are shown by default, if no filter chosen
- Grover Germany (`grover-de`) is shown by default, if no store code passed
- The product Name, Brand, Category, Availability (in stock | out of stock) and quantity are displayed

### Platform Choice

You can create the application as either a command line application or web application in any of the following platforms:

- Python, Typescript, NodeJS, Ruby or JavaScript for web applications
- Python, Ruby, Golang or Rust for command line applications

Think about the type of work you would like to do at Grover and **choose an appropriate application type and platform**.

# Technical questions

Please answer the following questions in the markdown file called `FOLLOW-UP.md`.
It is ok if you don't know the answer for some of the questions, therefore don't copy/paste from Google.

1. How long did you spend on the coding test? What would you add to your solution if you had more time? _If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add._
2. What was the most useful feature added to the latest version of your chosen language? Please include a snippet of code that shows how you've used it.
3. How would you track down a performance issue in production? Have you ever had to do this?
4. How would you monitor and trace issues in a distributed systems environment?

#### Thanks for your time, we look forward to hearing from you!

_Inspiration for the test format taken with ❤️ from [Skyscanner recruitment test](https://github.com/Skyscanner/full-stack-recruitment-test/) & [JustEat's recruitment test](https://github.com/justeat/JustEat.RecruitmentTest)_
