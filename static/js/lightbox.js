// create lightbox and append to body
const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

// create button
const button = document.createElement('button')
button.id = 'dislike_button'

// add lightbox if clicked on image
const js_images = document.querySelectorAll('img')
js_images.forEach(image => {
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
    lightbox.appendChild(button)
    button.innerHTML = 'Dislike'
    button.classList.add('active')
  })
})

// remove lightbox if clicked outside image
lightbox.addEventListener('click', e => {
  if (e.target !== e.currentTarget) return
  lightbox.classList.remove('active')
})

// update image if dislike button is pressed
button.addEventListener("click", function(){
  // find current img DOM
  var img = lightbox.firstChild;

  console.log(images)

  // src swap
  old_src = img.src
  img.src = secondary_images[1]

  // update primary image array
  for(var i = 0; i < images.length; i++) {
    console.log(images[i].slice(2))
    if (old_src.slice(21) == images[i].slice(2)) {
      console.log('foo')
      images[i] = img.src.slice(21)
    }
  }
  lightbox.appendChild(button)
  // remove used image from array
  secondary_images.shift()
  console.log(images)
})
