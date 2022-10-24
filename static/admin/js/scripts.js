const btn = document.getElementById("#send")

btn.addEventListener("click", function(e) {
    e.preventDefault()
    const dataType = document.getElementById("#dataType").value
    const name = document.getElementById("#name").value
    const content = document.getElementById("#content").value
    console.log(dataType)
    console.log(name)
    console.log(content)
}) 