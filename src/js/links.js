export default class Links {
    constructor(selector = 'body', exclude=[]) {
        this.container = document.querySelector(selector)

        this.internalLinks = this.container.querySelectorAll('a[href^="/"]')
        this.externalLinks = this.container.querySelectorAll('a[href^="http"]')
        this.anchorLinks = this.container.querySelectorAll('a[href^="#"]')

        this.uri = window.location.pathname

        this.exclude = exclude

        if (this.internalLinks) this._internal()
        if (this.externalLinks) this._external()
        if (this.anchorLinks) this._anchor()
    }

    _internal() {
        // Add active class to link
        this.internalLinks.forEach((link, index) => {
            // Check if not in this.exclude
            if (link.classList.toString().split(/\s/).some(item => this.exclude.includes(item))) return
            let uri = link.getAttribute('href').split('?')[0]
            if (this.uri === uri) {
                link.classList.add('active')
                if (link.parentElement?.parentElement?.classList.contains("first")
                        && link.parentElement.parentElement.nodeName === 'UL') {
                    localStorage.setItem('selectedItemIndex', index);
                }
            } else if (this.uri === '/' && index === 0){
                link.classList.add('active')
                localStorage.setItem('selectedItemIndex', index);
            }
            let selectedItemIndex = localStorage.getItem('selectedItemIndex')
            if (selectedItemIndex && selectedItemIndex == index) {
                link.parentElement.classList.remove('parent')
            }
        })
    }

    _external() {
        // Open external link in new tab
        this.externalLinks.forEach(link => {
            link.setAttribute('targer', '_blank')
        })
    }

    _anchor() {
        //Scroll anchor links
        this.anchorLinks.forEach(link => {
            let href = link.getAttribute('href')
            link.addEventListener('click', e => {
                e.preventDefault()
                if (href !== '#' && document.querySelector(href)) {
                    $('body, html').animate({scrollTop: $(href).offset().top}, 250)
                }
            })
        })
    }
}