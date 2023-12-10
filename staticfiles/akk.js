document.addEventListener('DOMContentLoaded', function() {
    console.log('Auctions.js loaded successfully!'); // to debug
    const watchlistIcon = document.getElementById('watchlist-icon');

    if (watchlistIcon) {
        watchlistIcon.addEventListener('click', function() {

            if (header.innerHTML === "<i class='far fa-heart'></i>Add to Watchlist") {
                header.innerHTML = "<i class='fas fa-heart'></i>Added to Watchlist"
            }
            else {
                header.innerHTML = "<i class='far fa-heart'></i>Add to Watchlist"
            }
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const commentForm = document.getElementById('comment-form');
    console.log(commentForm)
    const commentsContainer = document.getElementById('comment-container');
    console.log(commentsContainer)

    if (commentForm) {
        commentForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(commentForm);

            fetch(commentForm.action, {
                method: 'POST',
                body: formData,
            })
                .then(response => response.text())
                .then(data => {
                    var comment = JSON.parse(data)
                    comment = comment.text
                    console.log(comment)
                    commentsContainer.innerHTML += 'You commented: '+comment+'<br>';
                    commentForm.reset();//clear whats written in the text box
                })
                .catch(error => console.error('Error:', error));
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const header = document.getElementById('watchlist-image')
    const add = document.getElementById('wishlist')
    console.log(add)
    const remove = document.getElementById('watchlist')
    console.log(remove)

    header.addEventListener('click', function(event) {
        event.preventDefault();
        const listingId = header.innerHTML.href;
        console.log(header.innerHTML)
        if (document.querySelector('#foo').src === "https://cdn-icons-png.flaticon.com/512/73/73814.png") {
            document.querySelector('#foo').src = "https://cdn.icon-icons.com/icons2/1369/PNG/512/-favorite_90527.png"
            fetch(add.href)
            .then(response => response.text())
            .then(data => {
                console.log(data)
            })
        }
        else {
            document.querySelector('#foo').src = "https://cdn-icons-png.flaticon.com/512/73/73814.png"            
            console.log(remove.href)
            fetch(remove.href)
            .then(response => response.text())
            .then(data => {
                console.log(data)
            })
        }
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const header = document.getElementById('watchlist-cart')
    const add = document.getElementById('cart-wishlist')
    console.log(add)
    const remove = document.getElementById('cart-watchlist')
    console.log(remove)

    header.addEventListener('click', function(event) {
        event.preventDefault();
        const listingId = header.innerHTML.href;
        console.log(header.innerHTML)
        if (document.querySelector('#doo').innerHTML === "<a id='cart-wishlist' href='{% url 'cart-view' book.id %}'></a>Add To Cart") {
            document.querySelector('#doo').innerHTML = "<a id='cart-wishlist' href='{% url 'removecart-view' book.id %}'></a>Remove From Cart"
            fetch(add.href)
            .then(response => response.text())
            .then(data => {
                console.log(data)
            })
        }
        else {
            document.querySelector('#doo').innerHTML = "<a id='cart-wishlist' href='{% url 'cart-view' book.id %}'></a>Add To Cart"            
            console.log(remove.href)
            fetch(remove.href)
            .then(response => response.text())
            .then(data => {
                console.log(data)
            })
        }
    });
});