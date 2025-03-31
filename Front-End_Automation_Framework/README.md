# Front-End Automation Framework

## Overview
This framework is a simple and easy-to-use template for front-end automation. It's programmed in C# using Selenium and was originally designed to test WPAS's new Blazor front-end but can be easily adapted to test any other front-end system.

## Features
- Built with C# and Selenium WebDriver
- Supports cross-browser testing
- Easily extendable to new front-end applications
- Modular and maintainable test structure
- Integration with NUnit for test execution

## Prerequisites
Before you can use this framework, ensure you have the following installed:

- [Visual Studio](https://visualstudio.microsoft.com/)
- [.NET SDK](https://dotnet.microsoft.com/en-us/download)
- [Selenium WebDriver](https://www.selenium.dev/)
- [NuGet Packages:](https://www.nuget.org/)
  - Selenium.WebDriver
  - Selenium.WebDriver.ChromeDriver
  - NUnit
  - NUnit3TestAdapter
 
There is a pdf attached in the repo that can take you through this 

## Installation
1. Clone this repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd selenium-automation-framework
   ```
3. Restore dependencies:
   ```sh
   dotnet restore
   ```

## Writing a Test
To write a new test, follow these steps:
1. Create a new class in the `Tests` folder.
2. Copy and Paste Template and chagne the names of the test as appropriate 
3. Use `PatientSearchTools` classes in the Demo_Library to interact with elements.

Example:
```csharp
[Test]
public void LoginTest()
{
    patientSearch.EnterUsername("testuser");
    patientSearch.EnterPassword("password");
    patientSearch.ClickLogin();
    Assert.IsTrue(loginPage.IsLoggedIn());
}
```
