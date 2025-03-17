using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;

namespace Front_End_Automation_Framework
{
    internal class Demo_Library
    {
        private readonly IWebDriver driver;
        private readonly WebDriverWait wait;
        public Demo_Library(IWebDriver driver)
        {
            this.driver = driver ?? throw new ArgumentNullException(nameof(driver));
            this.wait = new WebDriverWait(driver, TimeSpan.FromSeconds(30));
        }
        public void searchBoxExample(string inputString)
        {
            Thread.Sleep(2000);
            IWebElement inputBox = wait.Until(driver => driver.FindElement(/*ENTER IDENTIFIER HERE*/)));   //  <---- E.g.   driver.FindElement(By.Id("searchBox"));

            //This sends an input is a search box is selected
            inputBox.SendKeys(inputString);
        }
        public void clickButtonExample()
        {
            IWebElement button = wait.Until(driver => driver.FindElement(By.Id("exampleButton")));  //Change identifier as needed

            //This clicks on the selected element
            button.Click();
        }
    }
}
