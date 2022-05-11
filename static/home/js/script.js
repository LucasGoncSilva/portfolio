window.addEventListener('DOMContentLoaded', () => {
  const nameRegex = /^([A-Za-z]*\s*)+$/
  const emailRegex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

  const mobileToggle = document.querySelector('.mobile-toggle')
  const contactForm = document.querySelector('form')
  const aside = document.querySelector('aside')
  const imgs = aside.querySelectorAll('img')


  function toTitleCase(str) {
    return str.replace(
      /\w\S*/g,
      function (txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      }
    );
  }

  function validateForm(name, email) {
    const nameTest = nameRegex.test(name)
    const emailTest = emailRegex.test(email)

    switch (true) {
      case (emailTest === false && nameTest === false):
        return 'Há algo de errado com a inserção do nome e do email'

      case (nameTest === false):
        return 'Há algo de errado com a inserção do nome'

      case (emailTest === false):
        return 'Há algo de errado com a inserção do email'

      default:
        return true
    }
  }


  let angle = 360 - 90, dangle = 360 / imgs.length

  for (let i = 0; i < imgs.length; ++i) {
    let circle = imgs[i]
    angle += dangle
    circle.style.transform = `rotate(${angle}deg) translate(${aside.clientWidth / 2}px) rotate(-${angle}deg)`
  }


  mobileToggle.onclick = function () {
    Swal.fire({
      width: '70vw',
      icon: 'info',
      iconColor: '#4717f6',
      title: 'Menu',
      html: '<h3><a href="#skills">Skills</a></h3><br><br>' +
        '<h3><a href="#projects">Projetos</a></h3><br><br>' +
        '<h3><a href="#about">Sobre</a></h3><br><br>' +
        '<h3><a href="#contact">Contato</a></h3>'
    })
  }

  contactForm.onsubmit = () => {
    const name = document.getElementById('name').value
    const email = document.getElementById('email').value

    const nameCleaned = toTitleCase(name)

    const formValidation = validateForm(nameCleaned, email)

    if (formValidation !== true) {
      Swal.fire({
        icon: 'error',
        title: 'Então...',
        html: `<p>${formValidation}...</p>` +
          '<p>Tente novamente :)</p>'
      })

      return false

    }
  }
})