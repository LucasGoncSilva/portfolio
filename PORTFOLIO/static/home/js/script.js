window.addEventListener("DOMContentLoaded", () => {
  const nameRegex = /^([A-Za-z]*\s*)+$/;
  const emailRegex =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  const mobileToggle = document.querySelector(".mobile-toggle");
  const contactForm = document.querySelector("form");
  const aside = document.querySelector("aside");
  const asideDivs = aside.querySelectorAll("div");

  const descriptionDiv = document.getElementById("description");

  const emailSendErr = "There is something wrong with";

  function toTitleCase(str) {
    return str.replace(/\w\S*/g, function (txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
  }

  function validateForm(name, email) {
    const nameTest = nameRegex.test(name);
    const emailTest = emailRegex.test(email);

    switch (true) {
      case emailTest === false && nameTest === false:
        return emailSendErr + "name and email";

      case nameTest === false:
        return emailSendErr + "name";

      case emailTest === false:
        return emailSendErr + "email";

      default:
        return true;
    }
  }

  let angle = 360 - 90,
    dangle = 360 / asideDivs.length;

  for (let i = 0; i < asideDivs.length; ++i) {
    let circle = asideDivs[i];
    angle += dangle;
    circle.style.transform = `rotate(${angle}deg) translate(${
      aside.clientWidth / 2
    }px) rotate(-${angle}deg)`;
  }

  mobileToggle.onclick = function () {
    Swal.fire({
      width: "70vw",
      icon: "info",
      iconColor: "#4717f6",
      title: "Menu",
      html:
        '<h3><a href="#skills">Skills</a></h3><br>' +
        '<h3><a href="#projects">Projects</a></h3><br>' +
        '<h3><a href="#about">About</a></h3><br>' +
        '<h3><a href="#contact">Contact Me</a></h3>',
    });
  };

  contactForm.onsubmit = () => {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const nameCleaned = toTitleCase(name);

    const formValidation = validateForm(nameCleaned, email);

    if (formValidation !== true) {
      Swal.fire({
        icon: "error",
        title: "Well...",
        html: `<p>${formValidation}...</p>` + "<p>Try again</p>",
      });

      return false;
    }
  };

  document.querySelectorAll(".skill-card").forEach((e) => {
    const skillTitle = e.dataset.title;
    const skillDescription = e.dataset.description;

    e.addEventListener("mouseover", () => {
      descriptionDiv.innerHTML = `<h3>${skillTitle}</h3><p>${skillDescription}</p>`;
    });

    e.addEventListener("mouseout", (e) => {
      if (e.tagName !== "img") {
        descriptionDiv.innerHTML =
          "<h3>&#12288;</h3><p>For details hover over it</p>";
      }
    });
  });
});
