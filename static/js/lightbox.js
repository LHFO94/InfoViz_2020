const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

const button = document.createElement('button')
button.id = 'dislike_button'

const images = document.querySelectorAll('img')
images.forEach(image => {
  image.addEventListener('click', e => {
    lightbox.classList.add('active')
    const img = document.createElement('img')
    img.src = image.src
    img.style.height = '200px'
    img.style.position = 'relative'
    img.style.top = '-200px'
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild)
    }
    lightbox.appendChild(img)

    var width = - ((img.clientWidth) / 2 + 25)
    lightbox.appendChild(button)
    button.style.left = width + 'px'
    button.style.top = '-75px'
    button.innerHTML = 'Dislike'
    button.classList.add('active')
  })
})

lightbox.addEventListener('click', e => {
  if (e.target !== e.currentTarget) return
  lightbox.classList.remove('active')
})

button.addEventListener("click", function(){
  var img = lightbox.firstChild;
  img.src = secondary_images[1]'
  lightbox.appendChild(button)
  secondary_images.shift()
});
