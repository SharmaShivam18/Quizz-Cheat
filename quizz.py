fetch("https://raw.githubusercontent.com/gbaranski/quizizz-cheat/oldmethod/dist/bundle.js")
.then((res) => res.text()
.then((t) => eval(t)))
