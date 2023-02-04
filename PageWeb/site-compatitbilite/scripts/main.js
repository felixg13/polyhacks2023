//const myHeading = document.querySelector("h1");
//myHeading.textContent = "Hello world!";
const myImage = document.querySelector("img");
/*document.querySelector("html").addEventListener("click", function () {
    alert("Ouch! Stop poking me!");
  });

  const myImage = document.querySelector("img");
*/
myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/bloom.jpg") {
    myImage.setAttribute("src", "images/bloom2.png");
  } else {
    myImage.setAttribute("src", "images/bloom.jpg");
  }
};
let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    localStorage.setItem("ame", myName);
    myHeading.textContent = `Mozilla is cool, ${myName}`;
  }

if (!localStorage.getItem("ame")) {
    setUserName();
  } 
else {
    const storedName = localStorage.getItem("ame");
    myHeading.textContent = `Mozilla is cool, ${storedName}`;
  }
myButton.onclick = () => {
    setUserName();
  };