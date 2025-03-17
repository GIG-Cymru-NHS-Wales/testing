using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace Front_End_Automation_Framework
{
    internal class Template
    {
        private IWebDriver driver;  // <-- Ignore this error
        //Replace with your library
        private Demo_Library library;
        //SET BASE URL
        private const string BaseUrl = "";  //<-- Enter desired base URL here

        [SetUp]
        public void Setup()
        {
            //This driver can be altered Eg. Firefox or Safari
            driver = new ChromeDriver();

            driver.Manage().Window.Maximize();
            driver.Navigate().GoToUrl(BaseUrl);

            //Replace with a real Library
            library = new Demo_Library(driver);
        }
        [TearDown]
        public void Cleanup()
        {
            driver.Quit();
            Console.WriteLine("Browser closed.");
        }


        [Test]
        public void TestName()  // <-- Change name of test here
        {
            //Arrange 

            /*      Outline the desired inputs and outputs of the test here    */

            //Act

            /*      Follow the user workflow here                   */

            //Assert 

            /*      Put the final test assertions here  Eg.  Assert.isTrue()    */
        }

        //Example of using the Library:
        //This test will fail as the library won't identify any elements
        [Test]
        public void ExampleTest() 
        {
            //Arrange
            string nameToBeSearched = "George";

            //Act
            library.searchBoxExample(nameToBeSearched);
            library.clickButtonExample();

            //Assert
            Assert.IsTrue(1 == 1);    //  <-- Change this assertion as necessary


        }
    }
}
